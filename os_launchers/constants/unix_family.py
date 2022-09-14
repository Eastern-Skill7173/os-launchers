import os
from typing import Final

__all__ = (
    "EXECUTABLES_DIRECTORY",
    "OPEN_DIRECTORY",
    "DESKTOP_ENVIRONMENT",
    "XDG_OPEN_DIRECTORY",
    "SUPPORTED_DE_FILE_BROWSERS",
    "SUPPORTED_DE_TERMINALS",
)


EXECUTABLES_DIRECTORY: Final = os.path.join(os.sep, "usr", "bin")
# OSX related info
OPEN_DIRECTORY: Final = os.path.join(EXECUTABLES_DIRECTORY, "open")
# Linux & Other OS info
DESKTOP_ENVIRONMENT: Final = os.getenv("DESKTOP_SESSION")
XDG_OPEN_DIRECTORY: Final = os.path.join(EXECUTABLES_DIRECTORY, "xdg-open")
_NAUTILUS_DIRECTORY: Final = os.path.join(EXECUTABLES_DIRECTORY, "nautilus")
_GNOME_TERMINAL_DIRECTORY: Final = os.path.join(
    EXECUTABLES_DIRECTORY,
    "gnome-terminal",
)
SUPPORTED_DE_FILE_BROWSERS: Final = {
    "plasma": [
        os.path.join(EXECUTABLES_DIRECTORY, "dolphin"),
        "--select"
    ],
    "gnome": [
        _NAUTILUS_DIRECTORY,
        "--select"
    ],
    "zorin": [
        _NAUTILUS_DIRECTORY,
        "--select"
    ],
}
SUPPORTED_DE_TERMINALS: Final = {
    "plasma": [
        os.path.join(EXECUTABLES_DIRECTORY, "konsole"),
        "--workdir"
    ],
    "xfce": [
        os.path.join(EXECUTABLES_DIRECTORY, "xfce4-terminal"),
        "--default-working-directory"
    ],
    "gnome": [
        _GNOME_TERMINAL_DIRECTORY,
        "--working-directory"
    ],
    "zorin": [
        _GNOME_TERMINAL_DIRECTORY,
        "--working-directory"
    ]
}
