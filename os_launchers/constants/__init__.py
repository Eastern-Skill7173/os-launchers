import os
import platform
from typing import Final

__all__ = (
    "CURRENT_MACHINE",
    "USER_DIRECTORY",
)


CURRENT_MACHINE: Final = platform.system()
USER_DIRECTORY: Final = os.path.expanduser('~')
