import os
import subprocess
import webbrowser
from typing import Union, Optional, Literal
from os_launchers.constants import CURRENT_MACHINE
from os_launchers.exceptions import UnsupportedDesktopEnvironment
from pathlib import Path

__all__ = (
    "open_url",
    "open_terminal",
    "open_with_associated_program",
    "open_file_manager",
)


FilePath = Union[str, Path]


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
        directory: FilePath,
        if_windows_launch_cmd: bool = False,
        **popen_kwargs) -> Optional[subprocess.Popen]:
    """
    Function to launch the terminal with the given directory

    Parameters
    ----------
    directory : FilePath
        Directory to launch the terminal with
    if_windows_launch_cmd : bool
        If the OS is of `Windows` Family,
        launch Cmd instead of PowerShell (default is False)

    Returns
    -------
    subprocess.Popen
        The Popen subprocess used to launch the terminal
    """
    directory = str(directory)
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
    else:
        from os_launchers.constants import unix_family
        de_terminal_command = \
            unix_family.SUPPORTED_DE_TERMINALS.get(
                unix_family.DESKTOP_ENVIRONMENT
            )
        if de_terminal_command is not None:
            command_list = [*de_terminal_command, directory]
        else:
            raise UnsupportedDesktopEnvironment(
                "{} is not a supported desktop environment"
                .format(unix_family.DESKTOP_ENVIRONMENT)
            )
    return subprocess.Popen(command_list, **popen_kwargs)


def open_with_associated_program(
        path: FilePath,
        **popen_kwargs) -> Optional[subprocess.Popen]:
    """
    Function to open the given path with the associated program

    Parameters
    ----------
    path : FilePath
        Path to the file or directory to be opened

    Returns
    -------
    None, subprocess.Popen
        If on `Windows` the `os.startfile` will be used which
        returns nothing.
        On other operating systems, the Popen subprocess
        used to launch the file will be returned
    """
    path = str(path)
    command_list = None
    if CURRENT_MACHINE == "Windows":
        os.startfile(path)
        return
    elif CURRENT_MACHINE == "Darwin":
        from os_launchers.constants import unix_family
        command_list = [unix_family.OPEN_DIRECTORY, path]
    else:
        from os_launchers.constants import unix_family
        command_list = [unix_family.XDG_OPEN_DIRECTORY, path]
    return subprocess.Popen(command_list, **popen_kwargs)


def open_file_manager(
        path: FilePath,
        always_open_parent_dir: bool = False,
        **popen_kwargs) -> Optional[subprocess.Popen]:
    """
    Function to open the file manager in the
    parent directory of the given path and highlighting it
    if supported by the file manager
    NOTE: THIS FUNCTION IS NOT FULLY TESTED
    ESPECIALLY AGAINST THE BSD FAMILY

    Parameters
    ----------
    path : FilePath
        Path to the file or directory to be opened
    always_open_parent_dir : bool
        On the supported platforms and DE, this option will make
        no difference, however, on an unsupported DE instead of
        raising `UnsupportedDesktopEnvironment`,
        will just open the parent path with no highlighting or selection
        (default is False)

    Returns
    -------
    subporcess.Popen
        The Popen subprocess used to launch the file manager
    """
    path = str(path)
    command_list = None
    if CURRENT_MACHINE == "Windows":
        from os_launchers.constants import windows
        command_list = [
            windows.EXPLORER_DIRECTORY, "/select,{}".format(path)
        ]
    elif CURRENT_MACHINE == "Darwin":
        from os_launchers.constants import unix_family
        command_list = [
            unix_family.OPEN_DIRECTORY, "-R", path
        ]
    else:
        # Many file managers do not support highlighting a file or folder
        # In unsupported file manager the parent directory will be opened
        from os_launchers.constants import unix_family
        de_file_browser_command = \
            unix_family.SUPPORTED_DE_FILE_BROWSERS.get(
                unix_family.DESKTOP_ENVIRONMENT
            )
        if de_file_browser_command is not None:
            command_list = [
                *de_file_browser_command,
                path
            ]
        else:
            if always_open_parent_dir:
                parent_path = str(Path(path).parent)
                command_list = [
                    unix_family.XDG_OPEN_DIRECTORY, parent_path
                ]
            else:
                raise UnsupportedDesktopEnvironment(
                    "{} is not a supported desktop environment"
                    .format(unix_family.DESKTOP_ENVIRONMENT)
                )
    return subprocess.Popen(command_list, **popen_kwargs)
