import os
from typing import Final

__all__ = (
    "WINDOWS_DIRECTORY",
    "EXPLORER_DIRECTORY",
    "POWERSHELL_DIRECTORY",
    "CMD_DIRECTORY",
)


WINDOWS_DIRECTORY: Final = os.getenv("WINDIR")
EXPLORER_DIRECTORY: Final = os.path.join(WINDOWS_DIRECTORY, "explorer.exe")
POWERSHELL_DIRECTORY: Final = os.path.join(
    WINDOWS_DIRECTORY,
    "System32",
    "WindowPowerShell",
    "v1.0",
    "powershell.exe",
)
CMD_DIRECTORY: Final = os.path.join(
    WINDOWS_DIRECTORY,
    "System32",
    "cmd.exe",
)
