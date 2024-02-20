from poetry.plugins.application_plugin import ApplicationPlugin

from poetry_pyrightconfig.command import PyrightConfigCommand


class PyrightConfigPlugin(ApplicationPlugin):
    def activate(self, application):
        application.command_loader.register_factory(
            PyrightConfigCommand.name, PyrightConfigCommand.factory
        )
