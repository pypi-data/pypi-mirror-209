from __future__ import annotations

import typing as t
from argparse import Namespace
from collections import defaultdict
from pathlib import Path

from dbt import flags
from dbt.adapters.factory import register_adapter, reset_adapters
from dbt.config import Profile, Project, RuntimeConfig
from dbt.config.profile import read_profile
from dbt.config.renderer import DbtProjectYamlRenderer, ProfileRenderer
from dbt.parser.manifest import ManifestLoader
from dbt.tracking import do_not_track
from dbt.version import get_installed_version

from sqlmesh.dbt.basemodel import Dependencies
from sqlmesh.dbt.model import ModelConfig
from sqlmesh.dbt.package import MacroConfig
from sqlmesh.dbt.seed import SeedConfig
from sqlmesh.dbt.source import SourceConfig
from sqlmesh.utils.jinja import MacroInfo, MacroReference

if t.TYPE_CHECKING:
    from dbt.contracts.graph.manifest import Macro, Manifest
    from dbt.contracts.graph.nodes import ManifestNode, SourceDefinition

ModelConfigs = t.Dict[str, ModelConfig]
SeedConfigs = t.Dict[str, SeedConfig]
SourceConfigs = t.Dict[str, SourceConfig]
MacroConfigs = t.Dict[str, MacroConfig]


class ManifestHelper:
    def __init__(
        self,
        project_path: Path,
        profiles_path: Path,
        profile_name: str,
        target: t.Optional[str] = None,
    ):
        self.project_path = project_path
        self.profiles_path = profiles_path
        self.profile_name = profile_name
        self.target = target

        self.__manifest: t.Optional[Manifest] = None
        self._project_name: str = ""

        self._is_loaded: bool = False
        self._models_per_package: t.Dict[str, ModelConfigs] = defaultdict(dict)
        self._seeds_per_package: t.Dict[str, SeedConfigs] = defaultdict(dict)
        self._sources_per_package: t.Dict[str, SourceConfigs] = defaultdict(dict)
        self._macros_per_package: t.Dict[str, MacroConfigs] = defaultdict(dict)

    def models(self, package_name: t.Optional[str] = None) -> ModelConfigs:
        self._load_all()
        return self._models_per_package[package_name or self._project_name]

    def seeds(self, package_name: t.Optional[str] = None) -> SeedConfigs:
        self._load_all()
        return self._seeds_per_package[package_name or self._project_name]

    def sources(self, package_name: t.Optional[str] = None) -> SourceConfigs:
        self._load_all()
        return self._sources_per_package[package_name or self._project_name]

    def macros(self, package_name: t.Optional[str] = None) -> MacroConfigs:
        self._load_all()
        return self._macros_per_package[package_name or self._project_name]

    @property
    def all_macros(self) -> t.Dict[str, t.Dict[str, MacroInfo]]:
        self._load_all()
        result: t.Dict[str, t.Dict[str, MacroInfo]] = defaultdict(dict)
        for package_name, macro_configs in self._macros_per_package.items():
            for macro_name, macro_config in macro_configs.items():
                result[package_name][macro_name] = macro_config.info
        return result

    def _load_all(self) -> None:
        if self._is_loaded:
            return
        self._load_models_and_seeds()
        self._load_sources()
        self._load_macros()
        self._is_loaded = True

    def _load_sources(self) -> None:
        for source in self._manifest.sources.values():
            source_dict = source.to_dict()
            source_dict.pop("database", None)  # picked up from the `config` attribute

            source_config = SourceConfig(
                **_config(source),
                **source_dict,
            )
            self._sources_per_package[source.package_name][
                source_config.source_name
            ] = source_config

    def _load_macros(self) -> None:
        for macro in self._manifest.macros.values():
            if macro.name.startswith("test_"):
                continue

            self._macros_per_package[macro.package_name][macro.name] = MacroConfig(
                info=MacroInfo(
                    definition=macro.macro_sql,
                    depends_on=list(_macro_references(self._manifest, macro)),
                ),
                path=Path(macro.original_file_path),
            )

    def _load_models_and_seeds(self) -> None:
        for node in self._manifest.nodes.values():
            if node.resource_type not in ("model", "seed"):
                continue

            macro_references = _macro_references(self._manifest, node)

            node_dict = node.to_dict()
            node_dict.pop("database", None)  # picked up from the `config` attribute
            base_config = {**_config(node), **node_dict, "path": Path(node.original_file_path)}

            if node.resource_type == "model":
                self._models_per_package[node.package_name][node.name] = ModelConfig(
                    sql=node.raw_code if DBT_VERSION >= (1, 3) else node.raw_sql,  # type: ignore
                    dependencies=Dependencies(
                        macros=macro_references,
                        refs=_refs(node),
                        sources=_sources(node),
                    ),
                    **base_config,
                )
            else:
                self._seeds_per_package[node.package_name][node.name] = SeedConfig(
                    dependencies=Dependencies(macros=macro_references),
                    **base_config,
                )

    @property
    def _manifest(self) -> Manifest:
        if not self.__manifest:
            self.__manifest = self._load_manifest()
        return self.__manifest

    def _load_manifest(self) -> Manifest:
        do_not_track()

        args: Namespace = Namespace(
            vars={} if DBT_VERSION >= (1, 5) else "{}",
            profile=self.profile_name,
            profiles_dir=str(self.profiles_path),
            target=self.target,
            macro_debugging=False,
        )
        flags.set_from_args(args, None)

        profile = self._load_profile()
        project = self._load_project(profile)
        runtime_config = RuntimeConfig.from_parts(project, profile, args)

        self._project_name = project.project_name

        register_adapter(runtime_config)
        manifest = ManifestLoader.get_full_manifest(runtime_config)
        reset_adapters()
        return manifest

    def _load_project(self, profile: Profile) -> Project:
        project_renderer = DbtProjectYamlRenderer(profile)
        return Project.from_project_root(str(self.project_path), project_renderer)

    def _load_profile(self) -> Profile:
        profile_renderer = ProfileRenderer({})
        raw_profiles = read_profile(str(self.profiles_path))
        return Profile.from_raw_profiles(
            raw_profiles=raw_profiles,
            profile_name=self.profile_name,
            renderer=profile_renderer,
            target_override=self.target,
        )


def _config(node: t.Union[ManifestNode, SourceDefinition]) -> t.Dict[str, t.Any]:
    return node.config.to_dict()


def _macro_references(
    manifest: Manifest, node: t.Union[ManifestNode, Macro]
) -> t.Set[MacroReference]:
    result = set()
    for macro_node_id in node.depends_on.macros:
        macro_node = manifest.macros[macro_node_id]
        macro_name = macro_node.name
        macro_package = (
            macro_node.package_name if macro_node.package_name != node.package_name else None
        )
        result.add(MacroReference(package=macro_package, name=macro_name))
    return result


def _refs(node: ManifestNode) -> t.Set[str]:
    if DBT_VERSION >= (1, 5):
        return {r.name for r in node.refs}  # type: ignore
    else:
        return {r[1] if len(r) > 1 else r[0] for r in node.refs}  # type: ignore


def _sources(node: ManifestNode) -> t.Set[str]:
    return {".".join(s) for s in node.sources}


def _model_node_id(model_name: str, package: str) -> str:
    return f"model.{package}.{model_name}"


def _get_dbt_version() -> t.Tuple[int, int]:
    dbt_version = get_installed_version()
    return (int(dbt_version.major or "0"), int(dbt_version.minor or "0"))


DBT_VERSION = _get_dbt_version()
