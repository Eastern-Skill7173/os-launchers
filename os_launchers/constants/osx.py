import os
from typing import Final

__all__ = (
    "EXECUTABLE_DIRECTORY",
    "OPEN_DIRECTORY",
)


EXECUTABLE_DIRECTORY: Final = os.path.join(
    os.sep,
    "Applications",
    "Utilites"
)
OPEN_DIRECTORY: Final = os.path.join(EXECUTABLE_DIRECTORY, "open")
