import re
from typing import Dict
from os_launchers.type_hints import RegexPattern
from os_launchers.profiles.unix_family.des import terminals
from os_launchers.profiles.unix_family.des import file_managers


__all__ = (
    "registered_des",
    "plasma",
    "xfce",
    "mate",
    "gnome",
    "cinnamon",
    "zorin",
)


registered_des: Dict[re.Pattern, "_DesktopEnvironment"] = {}
"""
A read-only dictionary containing desktop environments'
name patterns as keys and `_DesktopEnvironment` instances
as their values
"""


class _DesktopEnvironment:
    """
    Class containing information about a (unix) desktop
    environment in an object such as:
        * its name pattern
            (
            e.g KDE plasma on linux: `plasma`,
            KDE plasma on FreeBSD: `/usr/local/share/xsessions/plasma`
            )
        * the pre-packaged terminal
        * the pre-packaged file manager
    """

    def __init__(
        self,
        name_pattern: RegexPattern,
        terminal: terminals.TerminalProfile,
        file_manager: file_managers.FileManagerProfile,
    ):
        self._name_pattern = re.compile(name_pattern)
        self._terminal = terminal
        self._file_manager = file_manager
        registered_des[self._name_pattern] = self

    def __repr__(self) -> str:
        return "{0}(name_pattern={1})".format(
            type(self).__name__,
            repr(self._name_pattern),
        )

    @property
    def name_pattern(self) -> re.Pattern:
        return self._name_pattern

    @property
    def terminal(self) -> terminals.TerminalProfile:
        return self._terminal

    @property
    def file_manager(self) -> file_managers.FileManagerProfile:
        return self._file_manager


plasma = _DesktopEnvironment(
    "plasma$",
    terminals.konsole,
    file_managers.dolphin,
)
xfce = _DesktopEnvironment(
    "xfce$",
    terminals.xfce4_terminal,
    file_managers.thunar
)
mate = _DesktopEnvironment(
    "mate$",
    terminals.mate_terminal,
    file_managers.caja
)
gnome = _DesktopEnvironment(
    "gnome$",
    terminals.gnome_terminal,
    file_managers.nautilus
)
cinnamon = _DesktopEnvironment(
    "cinnamon$",
    terminals.gnome_terminal,
    file_managers.nemo
)
zorin = _DesktopEnvironment(
    "zorin$",
    terminals.gnome_terminal,
    file_managers.nautilus
)
