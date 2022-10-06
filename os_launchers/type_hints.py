import re
from typing import Union
from pathlib import Path

__all__ = (
    "PathType",
    "RegexPattern",
)


PathType = Union[str, Path]
RegexPattern = Union[str, re.Pattern]
