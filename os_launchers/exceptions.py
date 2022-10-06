__all__ = (
    "UnsupportedOperatingSystem",
    "UnsupportedDesktopEnvironment",
    "UnsupportedArgRequest",
)


class UnsupportedOperatingSystem(Exception):
    """
    An exception to be raised when launcher is
    called on an unsupported operating system
    """


class UnsupportedDesktopEnvironment(Exception):
    """
    An exception to be raised when launcher is
    called on an unsupported desktop environment
    (unix family exception only)
    """


class UnsupportedArgRequest(Exception):
    """
    An exception to be raised when launcher is
    called with an unsupported shell arg
    """
