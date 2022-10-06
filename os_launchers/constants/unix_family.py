import os
from typing import Final

__all__ = (
    "EXECUTABLES_DIRECTORY",
    "OPEN_DIRECTORY",
    "USER_DESKTOP_ENVIRONMENT",
    "XDG_OPEN_DIRECTORY",
)


EXECUTABLES_DIRECTORY: Final = os.path.join(os.sep, "usr", "bin")
# OSX related info
OPEN_DIRECTORY: Final = os.path.join(EXECUTABLES_DIRECTORY, "open")
# Linux & Other OS info
USER_DESKTOP_ENVIRONMENT: Final = os.getenv("DESKTOP_SESSION")
XDG_OPEN_DIRECTORY: Final = os.path.join(EXECUTABLES_DIRECTORY, "xdg-open")
