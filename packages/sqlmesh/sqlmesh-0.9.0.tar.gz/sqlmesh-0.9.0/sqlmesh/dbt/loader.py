from __future__ import annotations

import logging
import typing as t
from pathlib import Path

from sqlmesh.core import constants as c
from sqlmesh.core.audit import Audit
from sqlmesh.core.config import Config, GatewayConfig
from sqlmesh.core.hooks import HookRegistry
from sqlmesh.core.loader import Loader
from sqlmesh.core.macros import MacroRegistry
from sqlmesh.core.model import Model, ModelCache
from sqlmesh.dbt.basemodel import BMC, BaseModelConfig
from sqlmesh.dbt.context import DbtContext
from sqlmesh.dbt.profile import Profile
from sqlmesh.dbt.project import Project
from sqlmesh.dbt.target import TargetConfig
from sqlmesh.utils import UniqueKeyDict
from sqlmesh.utils.jinja import JinjaMacroRegistry

logger = logging.getLogger(__name__)


def sqlmesh_config(project_root: t.Optional[Path] = None, **kwargs: t.Any) -> Config:
    project_root = project_root or Path()
    context = DbtContext(project_root=project_root)
    profile = Profile.load(context)

    return Config(
        default_gateway=profile.target_name,
        gateways={profile.target_name: GatewayConfig(connection=profile.target.to_sqlmesh())},  # type: ignore
        loader=DbtLoader,
        **kwargs,
    )


class DbtLoader(Loader):
    def _load_scripts(self) -> t.Tuple[MacroRegistry, HookRegistry, JinjaMacroRegistry]:
        macro_files = list(Path(self._context.path, "macros").glob("**/*.sql"))

        for file in macro_files:
            self._track_file(file)

        # This doesn't do anything, the actual content will be loaded from the manifest
        return (
            UniqueKeyDict("macros"),
            UniqueKeyDict("hooks"),
            JinjaMacroRegistry(),
        )

    def _load_models(
        self, macros: MacroRegistry, hooks: HookRegistry, jinja_macros: JinjaMacroRegistry
    ) -> UniqueKeyDict[str, Model]:
        models: UniqueKeyDict = UniqueKeyDict("models")

        project = Project.load(
            DbtContext(project_root=self._context.path, target_name=self._context.gateway)
        )
        for path in project.project_files:
            self._track_file(path)

        context = project.context.copy()

        macros_mtimes: t.List[float] = []

        for package_name, package in project.packages.items():
            context.variables = package.variables
            context.add_sources(package.sources)
            context.add_seeds(package.seeds)
            context.add_models(package.models)
            macros_mtimes.extend(
                [
                    self._path_mtimes[m.path]
                    for m in package.macros.values()
                    if m.path in self._path_mtimes
                ]
            )

        for package_name, macro_infos in context.manifest.all_macros.items():
            context.jinja_macros.add_macros(
                macro_infos,
                package=package_name if package_name != context.project_name else None,
            )

        macros_max_mtime = max(macros_mtimes) if macros_mtimes else None
        yaml_max_mtimes = self._compute_yaml_max_mtime_per_subfolder(self._context.path)
        cache = DbtLoader._Cache(self, project, macros_max_mtime, yaml_max_mtimes)

        logger.info("Converting models to sqlmesh")
        # Now that config is rendered, create the sqlmesh models
        for package in project.packages.values():
            context.variables = package.variables
            package_models: t.Dict[str, BaseModelConfig] = {**package.models, **package.seeds}

            models.update(
                {
                    model.model_name: cache.get_or_load_model(
                        model.path, lambda: self._to_sqlmesh(model, context)
                    )
                    for model in package_models.values()
                }
            )

        return models

    def _load_audits(self) -> UniqueKeyDict[str, Audit]:
        return UniqueKeyDict("audits")

    @classmethod
    def _to_sqlmesh(cls, config: BMC, context: DbtContext) -> Model:
        logger.info(f"Converting {config.model_name} to sqlmesh format")
        return config.to_sqlmesh(context)

    def _compute_yaml_max_mtime_per_subfolder(self, root: Path) -> t.Dict[Path, float]:
        if not root.is_dir():
            return {}

        result = {}
        max_mtime: t.Optional[float] = None

        for nested in root.iterdir():
            if nested.is_dir():
                result.update(self._compute_yaml_max_mtime_per_subfolder(nested))
            elif nested.suffix.lower() in (".yaml", ".yml"):
                yaml_mtime = self._path_mtimes.get(nested)
                if yaml_mtime:
                    max_mtime = max(max_mtime, yaml_mtime) if max_mtime is not None else yaml_mtime

        if max_mtime is not None:
            result[root] = max_mtime

        return result

    class _Cache:
        def __init__(
            self,
            loader: DbtLoader,
            project: Project,
            macros_max_mtime: t.Optional[float],
            yaml_max_mtimes: t.Dict[Path, float],
        ):
            self._loader = loader
            self._project = project
            self._macros_max_mtime = macros_max_mtime
            self._yaml_max_mtimes = yaml_max_mtimes

            target = t.cast(TargetConfig, project.context.target)
            cache_path = loader._context.path / c.CACHE / target.name
            self._model_cache = ModelCache(cache_path)

        def get_or_load_model(self, target_path: Path, loader: t.Callable[[], Model]) -> Model:
            return self._model_cache.get_or_load(
                self._cache_entry_name(target_path), self._cache_entry_id(target_path), loader
            )

        def _cache_entry_name(self, target_path: Path) -> str:
            try:
                path_for_name = target_path.absolute().relative_to(
                    self._project.context.project_root.absolute()
                )
            except ValueError:
                path_for_name = target_path
            return "__".join(path_for_name.parts).replace(path_for_name.suffix, "")

        def _cache_entry_id(self, target_path: Path) -> str:
            max_mtime = self._max_mtime_for_path(target_path)
            return str(int(max_mtime)) if max_mtime is not None else "na"

        def _max_mtime_for_path(self, target_path: Path) -> t.Optional[float]:
            project_root = self._project.context.project_root

            try:
                target_path.absolute().relative_to(project_root.absolute())
            except ValueError:
                return None

            mtimes = [
                self._loader._path_mtimes.get(target_path),
                self._loader._path_mtimes.get(self._project.profile.path),
                # FIXME: take into account which macros are actually referenced in the target model.
                self._macros_max_mtime,
            ]

            cursor = target_path
            while cursor != project_root:
                cursor = cursor.parent
                mtimes.append(self._yaml_max_mtimes.get(cursor))

            non_null_mtimes = [t for t in mtimes if t is not None]
            return max(non_null_mtimes) if non_null_mtimes else None
