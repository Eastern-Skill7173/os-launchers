import os
import subprocess
from os_launchers.type_hints import PathType
from os_launchers.conversions import PathTypeConversion
from os_launchers.constants.unix_family import EXECUTABLES_DIRECTORY

__all__ = (
    "TerminalProfile",
    "konsole",
    "xfce4_terminal",
    "mate_terminal",
    "gnome_terminal",
)


class TerminalProfile:
    """
    Class containing information about a (unix) desktop
    environments' terminal inside of an object
    """

    def __init__(
        self,
        executable_path: PathType,
        working_directory_arg: str
    ):
        self._executable_path = PathTypeConversion.as_str(executable_path)
        self._working_directory_arg = str(working_directory_arg)

    def __repr__(self) -> str:
        return "{0}(executable_path={1})".format(
            type(self).__name__,
            repr(self._executable_path),
        )

    def __call__(
        self,
        working_directory: PathType,
        **popen_kwargs
    ) -> subprocess.Popen:
        working_directory = PathTypeConversion.as_str(working_directory)
        command_list = [
            self._executable_path,
            self._working_directory_arg,
            working_directory,
        ]
        return subprocess.Popen(
            command_list,
            **popen_kwargs
        )

    @property
    def executable_path(self) -> str:
        return self._executable_path

    @property
    def working_directory_arg(self) -> str:
        return self._working_directory_arg


konsole = TerminalProfile(
    os.path.join(EXECUTABLES_DIRECTORY, "konsole"),
    "--workdir"
)
xfce4_terminal = TerminalProfile(
    os.path.join(EXECUTABLES_DIRECTORY, "xfce4-terminal"),
    "--default-working-directory"
)
mate_terminal = TerminalProfile(
    os.path.join(EXECUTABLES_DIRECTORY, "mate-terminal"),
    "--working-directory"
)
gnome_terminal = TerminalProfile(
    os.path.join(EXECUTABLES_DIRECTORY, "gnome-terminal"),
    "--working-directory"
)
