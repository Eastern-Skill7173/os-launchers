import os
import platform
from typing import Final

__all__ = (
    "CURRENT_MACHINE",
    "DESKTOP_ENVIRONMENT",
    "SUPPORTED_DE_FILE_BROWSERS",
    "SUPPORTED_DE_TERMINALS",
)


CURRENT_MACHINE: Final = platform.system()
DESKTOP_ENVIRONMENT: Final = os.getenv("DESKTOP_SESSION")
SUPPORTED_DE_FILE_BROWSERS: Final = {
    "plasma": ["dolphin", "--select"],
    "gnome": ["nuatilus", "--select"],
    "zorin": ["nuatilus", "--select"],
}
SUPPORTED_DE_TERMINALS: Final = {
    "plasma": ["konsole", "--workdir"],
    "xfce": ["xfce4-terminal", "--default-working-directory"],
    "gnome": ["gnome-terminal", "--working-directory"],
    "zorin": ["gnome-terminal", "--working-directory"]
}
