import json

from poetry.console.commands.command import Command


class PyrightConfigCommand(Command):

    name: str = "env pyrightconfig"
    description: str = "Generate a pyrightconfig.json file for the current environment"

    def handle(self) -> int:
        from poetry.utils.env import EnvManager

        env = EnvManager(self.poetry).get()
        res = {
            "venv": env.path.name,
            "venvPath": str(env.path.parent.absolute()),
        }

        with open("pyrightconfig.json", "w") as f:
            json.dump(f, res, indent="  ")

        return 0

    @staticmethod
    def factory():
        return PyrightConfigCommand()
