from requests import exceptions as requests_exceptions

from briefcase.exceptions import CorruptToolError, MissingToolError, NetworkFailure

ELF_PATCH_OFFSET = 0x08
ELF_PATCH_ORIGINAL_BYTES = bytes.fromhex("414902")
ELF_PATCH_PATCHED_BYTES = bytes.fromhex("000000")


class LinuxDeploy:
    name = "linuxdeploy"
    full_name = "linuxdeploy"

    def __init__(self, command):
        self.command = command

    @property
    def appimage_name(self):
        return f"linuxdeploy-{self.command.host_arch}.AppImage"

    @property
    def linuxdeploy_download_url(self):
        return (
            "https://github.com/linuxdeploy/linuxdeploy/"
            f"releases/download/continuous/{self.appimage_name}"
        )

    @property
    def appimage_path(self):
        return self.command.tools_path / self.appimage_name

    @classmethod
    def verify(cls, command, install=True):
        """Verify that linuxdeploy is available.

        :param command: The command that needs to use linuxdeploy
        :param install: Should the tool be installed if it is not found?
        :returns: A valid linuxdeploy tool wrapper. If linuxdeploy is not
            available, and was not installed, raises MissingToolError.
        """
        linuxdeploy = LinuxDeploy(command)

        if not linuxdeploy.exists():
            if install:
                command.logger.info(
                    "The linuxdeploy tool was not found; downloading and installing...",
                    prefix=cls.name,
                )
                linuxdeploy.install()
            else:
                raise MissingToolError("linuxdeploy")

        return LinuxDeploy(command)

    def exists(self):
        return self.appimage_path.exists()

    @property
    def managed_install(self):
        return True

    def install(self):
        """Download and install linuxdeploy."""
        try:
            linuxdeploy_appimage_path = self.command.download_url(
                url=self.linuxdeploy_download_url, download_path=self.command.tools_path
            )
        except requests_exceptions.ConnectionError as e:
            raise NetworkFailure("downloading linuxdeploy AppImage") from e

        with self.command.input.wait_bar("Installing linuxdeploy..."):
            self.command.os.chmod(linuxdeploy_appimage_path, 0o755)
            self.patch_elf_header()

    def uninstall(self):
        """Uninstall linuxdeploy."""
        with self.command.input.wait_bar("Removing old linuxdeploy install..."):
            self.appimage_path.unlink()

    def upgrade(self):
        """Upgrade an existing linuxdeploy install."""
        if not self.exists():
            raise MissingToolError("linuxdeploy")

        self.uninstall()
        self.install()

    def patch_elf_header(self):
        """Patch the ELF header of the AppImage to ensure it's always
        executable.

        This patch is necessary on Linux hosts that use AppImageLauncher.
        AppImages use a modified ELF binary header starting at offset 0x08
        for additional identification. If a system has AppImageLauncher,
        the Linux kernel module `binfmt-misc` will try to load the AppImage
        with AppImageLauncher. As this binary does not exist in the Docker
        container context, we patch the ELF header of linuxdeploy to remove
        the AppImage bits, thus making all systems treat it like a regular
        ELF binary.

        Citations:
        - https://github.com/AppImage/AppImageKit/issues/1027#issuecomment-1028232809
        - https://github.com/AppImage/AppImageKit/issues/828
        """

        if not self.exists():
            raise MissingToolError("linuxdeploy")
        with open(self.appimage_path, "r+b") as appimage:
            appimage.seek(ELF_PATCH_OFFSET)
            # Check if the header at the offset is the original value
            # If so, patch it.
            if appimage.read(len(ELF_PATCH_ORIGINAL_BYTES)) == ELF_PATCH_ORIGINAL_BYTES:
                appimage.seek(ELF_PATCH_OFFSET)
                appimage.write(ELF_PATCH_PATCHED_BYTES)
                appimage.flush()
                appimage.seek(0)
                self.command.logger.info("Patched ELF header of linuxdeploy AppImage.")
            # Else if the header is the patched value, do nothing.
            elif (
                appimage.read(len(ELF_PATCH_ORIGINAL_BYTES)) == ELF_PATCH_PATCHED_BYTES
            ):
                self.command.logger.info(
                    "ELF header of linuxdeploy AppImage is already patched."
                )
            else:
                # We should only get here if the file at the AppImage patch doesn't have
                # The original or patched value. If this is the case, the file is likely
                # wrong and we should raise an exception.
                raise CorruptToolError("linuxdeploy")
