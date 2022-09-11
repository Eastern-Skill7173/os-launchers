__all__ = (
    "UnsupportedDesktopEnvironment",
)


class UnsupportedDesktopEnvironment(Exception):
    """
    An exception to be raised when launcher is
    called on an unsupported desktop environment
    """
