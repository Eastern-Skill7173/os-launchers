import os
import subprocess
from typing import Optional
from os_launchers.type_hints import PathType
from os_launchers.conversions import PathTypeConversion
from os_launchers.exceptions import UnsupportedArgRequest
from os_launchers.constants.unix_family import EXECUTABLES_DIRECTORY

__all__ = (
    "FileManagerProfile",
    "dolphin",
    "thunar",
    "caja",
    "nautilus",
    "nemo",
)


class FileManagerProfile:
    """
    Class containing information about a (unix) desktop
    environments' file manager inside of an object
    """

    def __init__(
        self,
        executable_path: PathType,
        highlight_flag: Optional[str] = None
    ):
        self._executable_path = PathTypeConversion.as_str(executable_path)
        if highlight_flag:
            self._higlight_flag = PathTypeConversion.as_str(highlight_flag)
        else:
            self._higlight_flag = None

    def __repr__(self) -> str:
        return "{0}(executable_path={1})".format(
            type(self).__name__,
            repr(self._executable_path),
        )

    def __call__(
        self,
        path: PathType,
        highlight: bool,
        **popen_kwargs
    ) -> subprocess.Popen:
        path = PathTypeConversion.as_str(path)
        command_list = [self._executable_path, path]
        if highlight:
            if self._higlight_flag:
                command_list.insert(1, self._higlight_flag)
            else:
                raise UnsupportedArgRequest(
                    "{0} does not have the supported argument: {1}"
                    .format(repr(self), repr("highlight_flag"))
                )
        return subprocess.Popen(command_list, **popen_kwargs)

    @property
    def executable_path(self) -> str:
        return self._executable_path

    @property
    def highlight_flag(self) -> Optional[str]:
        return self._higlight_flag


dolphin = FileManagerProfile(
    os.path.join(EXECUTABLES_DIRECTORY, "dolphin"),
    "--select"
)
thunar = FileManagerProfile(
    os.path.join(EXECUTABLES_DIRECTORY, "thunar")
)
caja = FileManagerProfile(
    os.path.join(EXECUTABLES_DIRECTORY, "caja")
)
nautilus = FileManagerProfile(
    os.path.join(EXECUTABLES_DIRECTORY, "nautilus"),
    "--select"
)
nemo = FileManagerProfile(
    os.path.join(EXECUTABLES_DIRECTORY, "nemo")
)
