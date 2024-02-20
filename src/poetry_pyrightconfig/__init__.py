import json

from cleo.commands.command import Command
from poetry.plugins.application_plugin import ApplicationPlugin


class PluginCommand(Command):

    name: str = "env pyrightconfig"

    def handle(self) -> int:
        from poetry.utils.env import EnvManager

        env = EnvManager(self.poetry).get()
        path = env.path
        res = {"venv": path.stem, "venvPath": str(path.parent.absolute())}
        self.line(json.dumps(res, indent="  "))

        return 0


def factory():
    return PluginCommand()


class PyrightConfigPlugin(ApplicationPlugin):
    def activate(self, application):
        application.command_loader.register_factory(PluginCommand.name, factory)
