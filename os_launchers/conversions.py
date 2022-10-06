import re
from pathlib import Path
from typing import Tuple
from os_launchers.type_hints import PathType, RegexPattern

__all__ = (
    "PathTypeConversion",
    "RegexPatternConversion",
)


class _TypeHintConversion:
    """
    Class for storing information about a type (hint)
    such as:

        * the allowed types (can be accessed by `cls.allowed_types()`)
        * the conversion methods between the allowed types
        (defined by the subclasses not this base class)

    This base class does not define the conversion methods itself
    the extra methods must be declared inside of each individual subclass
    """
    _allowed_types = ()

    @classmethod
    def allowed_types(cls) -> Tuple[type, ...]:
        """
        Classmethod to return the designated allowd types

        Returns
        -------
        Tuple[type, ....]
            A tuple containing the allowed and designated types
        """
        return cls._allowed_types


class PathTypeConversion(_TypeHintConversion):
    """
    Class for storing information about the `PathType` type hint,
    containing the conversion methods:

        * `as_str` classmethod to convert a path type to a string
        * `as_path_obj` classmethod to convert a path type to a path obj

    """
    _allowed_types = (str, Path)

    @classmethod
    def as_str(cls, path: PathType) -> str:
        """
        Classmethod to convert any path type (eiter `str` or `pathlib.Path`)
        to the equivalent string

        Parameters
        ----------
        path : PathType
            path type (`str` or `pathlib.Path`) to be converted

        Returns
        -------
        str
            A string representing the equivalent path
        """
        return str(path)

    @classmethod
    def as_path_obj(cls, path: PathType) -> Path:
        """
        Classmethod to convert any path type (either `str` or `pathlib.Path`)
        to the equivalent path object

        Parameters
        ----------
        path : PathType
            path type (`str` or `pathlib.Path`) to be converted

        Returns
        -------
        pathlib.Path
            A pathlib.Path object representing the equivalent path
        """
        return Path(path)


class RegexPatternConversion(_TypeHintConversion):
    """
    Class for storing information about the `RegexPattern` type hint,
    containing the conversion methods:

        * `as_str` classmethod to convert a regex pattern to a string
        * `as_regex_pattern_obj` classmethod to convert a regex pattern
        to a regex pattern obj (re.Pattern)

    """
    _allowed_types = (str, re.Pattern)

    @classmethod
    def as_str(cls, regex_pattern: RegexPattern) -> str:
        """
        Classmethod to convert any regex pattern (either `str` or `re.Pattern`)
        to the equivalent string

        Parameters
        ----------
        regex_pattern : RegexPattern
            regex pattern (`str` or `re.Pattern`) to be converted

        Returns
        -------
        str
            A string representing the equivalent regex pattern
        """
        if isinstance(regex_pattern, re.Pattern):
            return regex_pattern.pattern
        return regex_pattern

    @classmethod
    def as_regex_pattern_obj(cls, regex_pattern: RegexPattern) -> re.Pattern:
        """
        Classmethod to convert any regex pattern (either `str` or `re.Pattern`)
        to the equivalent regex pattern object

        Parameters
        ----------
        regex_pattern : RegexPattern
            regex pattern (`str` or `re.Pattern`) to be converted

        Returns
        -------
        re.Pattern
            A re.Pattern object representing the equivalent regex pattern
        """
        return re.compile(regex_pattern)
