import os
from typing import Final

__all__ = (
    "EXECUTABLES_DIRECTORY",
    "OPEN_DIRECTORY",
    "DESKTOP_ENVIRONMENT",
    "XDG_OPEN_DIRECTORY",
    "SUPPORTED_FILE_MANAGERS",
    "SUPPORTED_FILE_MANAGERS_HIGHLIGHT_FLAGS",
    "SUPPORTED_TERMINALS",
    "SUPPORTED_TERMINALS_WORKDIR_FLAG",
)


EXECUTABLES_DIRECTORY: Final = os.path.join(os.sep, "usr", "bin")
# OSX related info
OPEN_DIRECTORY: Final = os.path.join(EXECUTABLES_DIRECTORY, "open")
# Linux & Other OS info
DESKTOP_ENVIRONMENT: Final = os.getenv("DESKTOP_SESSION")
XDG_OPEN_DIRECTORY: Final = os.path.join(EXECUTABLES_DIRECTORY, "xdg-open")
# DE specific info
_NAUTILUS_DIRECTORY: Final = os.path.join(EXECUTABLES_DIRECTORY, "nautilus")
_GNOME_TERMINAL_DIRECTORY: Final = os.path.join(
    EXECUTABLES_DIRECTORY,
    "gnome-terminal",
)
SUPPORTED_FILE_MANAGERS: Final = {
    "plasma": os.path.join(EXECUTABLES_DIRECTORY, "dolphin"),
    "xfce": os.path.join(EXECUTABLES_DIRECTORY, "thunar"),
    "mate": os.path.join(EXECUTABLES_DIRECTORY, "caja"),
    "gnome": _NAUTILUS_DIRECTORY,
    "zorin": _NAUTILUS_DIRECTORY,
}
SUPPORTED_FILE_MANAGERS_HIGHLIGHT_FLAGS: Final = {
    "plasma": "--select",
    "gnome": "--select",
    "zorin": "--select",
}
SUPPORTED_TERMINALS: Final = {
    "plasma": os.path.join(EXECUTABLES_DIRECTORY, "konsole"),
    "xfce": os.path.join(EXECUTABLES_DIRECTORY, "xfce4-terminal"),
    "mate": os.path.join(EXECUTABLES_DIRECTORY, "mate-terminal"),
    "gnome": _GNOME_TERMINAL_DIRECTORY,
    "zorin": _GNOME_TERMINAL_DIRECTORY,
}
SUPPORTED_TERMINALS_WORKDIR_FLAG: Final = {
    "plasma": "--workdir",
    "xfce": "--default-working-directory",
    "mate": "--working-directory",
    "gnome": "--working-directory",
    "zorin": "--working-driectory",
}
