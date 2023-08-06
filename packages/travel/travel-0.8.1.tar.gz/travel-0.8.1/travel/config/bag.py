import logging
import os

from travel.config.sanitizers import python_sanitizer, pip_sanitizer
from travel.config.subconfigs.pip import PipConfig
from travel.config.subconfigs.scopes import ScopeConfig
from travel.custom.tasks.task import Task

logger = logging.getLogger(__name__)


class Bag:

    def __init__(self, location: str, yml: dict, root_context: str = None):
        self.location = location
        self.root_context = root_context
        self.name = os.path.basename(os.path.normpath(location))
        self.group = []

        # Pop the config entries
        config = yml.copy()
        self.python = python_sanitizer.sanitize_version(config.pop("python", None), nullable=True)
        self.pip = PipConfig(config.pop("pip", {}))
        self.dependencies = {pip_sanitizer.sanitize_package(dep): None for dep in config.pop("dependencies", [])}  # To be filled later
        self.requirements = [pip_sanitizer.sanitize_versioned_package(req) for req in config.pop("requirements", {})]
        self.tasks = {
            phase: {
                step: [Task(definition) for definition in tasks]
                for step, tasks in steps.items()
            }
            for phase, steps in config.pop("tasks", {}).items()
        }
        self.scopes = {
            scope: ScopeConfig(scope, scope_config)
            for scope, scope_config in config.pop("scopes", {}).items()
        }

        # Extra utils
        # self.package = self.name  # But could be different  # TODO: cannot be inferred here
        self.setup_py_folder = os.path.join(self.location, "package")  # But could be different
        self.build_folder = os.path.join(self.location, "build")  # But could be different
        self.dist_folder = os.path.join(self.build_folder, "package", "dist")  # But could be different
        self.tasks_folder = os.path.join(self.build_folder, "tasks")
        self.requirements_file = os.path.join(self.setup_py_folder, "requirements.txt")

        # If there are still configs, they are unknown. Print a warning (for retro-compatibility)
        if config:
            logger.warning(f"Unknown configuration in bag file \"{self.name}\": {config}")

    def fill_dependency_with_bag(self, bag):
        self.dependencies[bag.name] = bag

    def flat_dependencies(self, with_current: bool = False):

        def visit(bag, visited, level=0):
            for dep in bag.dependencies.values():
                visited[dep] = max(level, visited.get(dep, level))
                visit(dep, visited, level=level+1)
            return visited

        bags = visit(self, {})
        dependencies = [bag for bag, level in sorted(bags.items(), key=lambda x: x[1], reverse=True)]
        if with_current:
            dependencies.append(self)
        return dependencies

    def __str__(self):
        return str(vars(self))

    def __repr__(self):
        return str(self)
