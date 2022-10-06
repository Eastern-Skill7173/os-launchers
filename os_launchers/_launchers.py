import os
import subprocess
import webbrowser
from typing import Optional, Literal
from os_launchers.type_hints import PathType
from os_launchers.conversions import PathTypeConversion
from os_launchers.constants import CURRENT_MACHINE, USER_DIRECTORY
from os_launchers import exceptions

__all__ = (
    "open_url",
    "open_terminal",
    "open_with_associated_program",
    "open_file_manager",
)


def open_url(
        url: str,
        new: Literal[1, 2, 3] = 2,
        auto_raise: bool = True) -> bool:
    """
    Function to open the passed url in user's default browser

    Parameters
    ----------
    url : str
        URL Address to be opened
    new : int
        Where to open the url inside of the browser (default is 2)
        - 0: the same browser window (the default).
        - 1: a new browser window.
        - 2: a new browser page ("tab").
    auto_raise : bool
        Whether to raise the browser window or not (default is False)

    Returns
    -------
    bool
        Boolean returned by `webbrowser.open`
    """
    return webbrowser.open(url, new=new, autoraise=auto_raise)


def open_terminal(
        directory: PathType = USER_DIRECTORY,
        if_windows_launch_cmd: bool = False,
        **popen_kwargs) -> Optional[subprocess.Popen]:
    """
    Function to launch the terminal with the given directory

    Parameters
    ----------
    directory : PathType
        Directory to launch the terminal with
    if_windows_launch_cmd : bool
        If the OS is of `Windows` Family,
        launch Cmd instead of PowerShell (default is False)

    Returns
    -------
    subprocess.Popen
        The Popen subprocess used to launch the terminal
    """
    directory = PathTypeConversion.as_str(directory)
    command_list = None
    if CURRENT_MACHINE == "Windows":
        from os_launchers.constants import windows
        command_list = [
            windows.POWERSHELL_DIRECTORY,
            "Start-Process",
            "-WorkingDirectory",
            directory,
            windows.POWERSHELL_DIRECTORY if not if_windows_launch_cmd
            else windows.CMD_DIRECTORY
        ]
    elif CURRENT_MACHINE == "Darwin":
        from os_launchers.constants import unix_family
        command_list = [
            unix_family.OPEN_DIRECTORY,
            "-a",
            "Terminal",
            directory
        ]
    elif CURRENT_MACHINE in ("Linux", "FreeBSD"):
        from os_launchers.constants import unix_family
        from os_launchers.profiles.unix_family.des import registered_des
        for name_pattern, desktop_environment in registered_des.items():
            if name_pattern.search(unix_family.USER_DESKTOP_ENVIRONMENT):
                return desktop_environment.terminal(
                    working_directory=directory,
                    **popen_kwargs
                )
        else:
            raise exceptions.UnsupportedDesktopEnvironment(
                "{0} is not a supported desktop environment"
                .format(unix_family.USER_DESKTOP_ENVIRONMENT)
            )
    else:
        raise exceptions.UnsupportedOperatingSystem(
            "{0} is not a supported operating system"
            .format(CURRENT_MACHINE)
        )
    return subprocess.Popen(command_list, **popen_kwargs)


def open_with_associated_program(
        path: PathType,
        **popen_kwargs) -> Optional[subprocess.Popen]:
    """
    Function to open the given path with the associated program

    Parameters
    ----------
    path : PathType
        Path to the file or directory to be opened

    Returns
    -------
    None, subprocess.Popen
        If on `Windows` the `os.startfile` will be used which
        returns nothing.
        On other operating systems, the Popen subprocess
        used to launch the file will be returned
    """
    path = PathTypeConversion.as_str(path)
    command_list = None
    if CURRENT_MACHINE == "Windows":
        os.startfile(path)
        return
    elif CURRENT_MACHINE == "Darwin":
        from os_launchers.constants import unix_family
        command_list = [unix_family.OPEN_DIRECTORY, path]
    elif CURRENT_MACHINE in ("Linux", "FreeBSD"):
        from os_launchers.constants import unix_family
        command_list = [unix_family.XDG_OPEN_DIRECTORY, path]
    else:
        raise exceptions.UnsupportedOperatingSystem(
            "{0} is not a supported operating system"
            .format(CURRENT_MACHINE)
        )
    return subprocess.Popen(command_list, **popen_kwargs)


def open_file_manager(
        path: PathType = USER_DIRECTORY,
        highlight: bool = False,
        **popen_kwargs) -> Optional[subprocess.Popen]:
    """
    Function to open the file manager in the
    parent directory of the given path and highlighting it
    if supported by the file manager
    NOTE: THIS FUNCTION IS NOT FULLY TESTED
    ESPECIALLY AGAINST THE BSD FAMILY

    Parameters
    ----------
    path : PathType
        Path to the file or directory to be opened
        in the file manager (default is `USER_DIRECTORY`)
    hightlight : bool
        If True, open the file manager in the parent directory,
        highlight the file and scroll to its position
        (default is False)
    always_open_parent_dir : bool
        On the supported platforms and DE, this option will make
        no difference, however, on an unsupported DE instead of
        raising `UnsupportedDesktopEnvironment`,
        will just open the parent path with no highlighting or selection
        (Will only be considered if highlight is True)
        (default is False)

    Returns
    -------
    subporcess.Popen
        The Popen subprocess used to launch the file manager
    """
    path = PathTypeConversion.as_str(path)
    command_list = None
    if CURRENT_MACHINE == "Windows":
        from os_launchers.constants import windows
        command_list = [
            windows.EXPLORER_DIRECTORY,
            "{0}{1}".format("/select," if highlight else '', path)
        ]
    elif CURRENT_MACHINE == "Darwin":
        from os_launchers.constants import unix_family
        command_list = [
            unix_family.OPEN_DIRECTORY, path
        ]
        if highlight:
            command_list.insert(1, "-R")
    elif CURRENT_MACHINE in ("Linux", "FreeBSD"):
        # Many file managers do not support highlighting a file or folder
        # In unsupported file manager the parent directory will be opened
        from os_launchers.constants import unix_family
        from os_launchers.profiles.unix_family import registered_des
        for name_pattern, desktop_environment in registered_des.items():
            if name_pattern.search(unix_family.USER_DESKTOP_ENVIRONMENT):
                return desktop_environment.file_manager(
                    path=path,
                    highlight=highlight,
                    **popen_kwargs
                )
        else:
            raise exceptions.UnsupportedDesktopEnvironment(
                "{} is not a supported desktop environment"
                .format(unix_family.DESKTOP_ENVIRONMENT)
            )
    else:
        raise exceptions.UnsupportedOperatingSystem(
            "{0} is not a supported operating system"
            .format(CURRENT_MACHINE)
        )
    return subprocess.Popen(command_list, **popen_kwargs)
