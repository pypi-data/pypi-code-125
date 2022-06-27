from typing import Optional

from briefcase.config import BaseConfig

from .base import full_options
from .create import CreateCommand


class UpdateCommand(CreateCommand):
    command = "update"

    def add_options(self, parser):
        parser.add_argument(
            "-d",
            "--update-dependencies",
            action="store_true",
            help="Update dependencies for app",
        )
        parser.add_argument(
            "-r",
            "--update-resources",
            action="store_true",
            help="Update app resources (icons, splash screens, etc)",
        )

    def update_app(
        self,
        app: BaseConfig,
        update_dependencies=False,
        update_resources=False,
        **options,
    ):
        """Update an existing application bundle.

        :param app: The config object for the app
        :param update_dependencies: Should dependencies be updated? (default: False)
        :param update_resources: Should extra resources be updated? (default: False)
        """

        bundle_path = self.bundle_path(app)
        if not bundle_path.exists():
            self.logger.error(
                "Application does not exist; call create first!", prefix=app.app_name
            )
            return

        if update_dependencies:
            self.logger.info("Updating dependencies...", prefix=app.app_name)
            self.install_app_dependencies(app=app)

        self.logger.info("Updating application code...", prefix=app.app_name)
        self.install_app_code(app=app)

        if update_resources:
            self.logger.info(
                "Updating extra application resources...", prefix=app.app_name
            )
            self.install_app_resources(app=app)

        self.logger.info("Application updated.", prefix=app.app_name)

    def __call__(
        self,
        app: Optional[BaseConfig] = None,
        update_dependencies: bool = False,
        update_resources: bool = False,
        **options,
    ):
        # Confirm all required tools are available
        self.verify_tools()

        if app:
            state = self.update_app(
                app,
                update_dependencies=update_dependencies,
                update_resources=update_resources,
                **options,
            )
        else:
            state = None
            for app_name, app in sorted(self.apps.items()):
                state = self.update_app(
                    app,
                    update_dependencies=update_dependencies,
                    update_resources=update_resources,
                    **full_options(state, options),
                )

        return state
