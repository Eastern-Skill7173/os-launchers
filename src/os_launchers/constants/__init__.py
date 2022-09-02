import platform
from typing import Final

__all__ = (
    "CURRENT_MACHINE",
)


CURRENT_MACHINE: Final = platform.system()
