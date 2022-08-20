import os
import subprocess
import webbrowser
from typing import Union, Optional
from os_launchers.constants import (
    CURRENT_MACHINE,
    DESKTOP_ENVIRONMENT,
    SUPPORTED_DE_FILE_BROWSERS,
    SUPPORTED_DE_TERMINALS,
)
from os_launchers.exceptions import UnsupportedDesktopEnvironment
from pathlib import Path

__all__ = (
    "open_url",
    "open_terminal",
    "open_file",
    "open_file_manager",
)


FilePath = Union[str, Path]


def open_url(url: str, new: int = 2, auto_raise: bool = True) -> None:
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
    webbrowser.open(url, new=new, autoraise=auto_raise)


def open_terminal(
        directory: FilePath,
        if_windows_launch_cmd: bool = False) -> Optional[subprocess.Popen]:
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
        command_list = [
            "PowerShell",
            "Start-Process",
            "-WorkingDirectory",
            directory,
            "PowerShell" if not if_windows_launch_cmd else "Cmd"
        ]
    elif CURRENT_MACHINE == "Darwin":
        command_list = [
            "open",
            "-a",
            "Terminal",
            directory
        ]
    else:
        linux_terminal_command = \
            SUPPORTED_DE_TERMINALS.get(DESKTOP_ENVIRONMENT)
        if linux_terminal_command is not None:
            command_list = [*linux_terminal_command, directory]
        else:
            raise UnsupportedDesktopEnvironment(
                "{} is not a supported desktop environment"
                .format(DESKTOP_ENVIRONMENT)
            )
    return subprocess.Popen(command_list)


def open_file(file_path: FilePath) -> Optional[subprocess.Popen]:
    """
    Function to open the given file path with the associated program

    Parameters
    ----------
    file_path : FilePath
        Path to the file to be opened

    Returns
    -------
    None, subprocess.Popen
        If on `Windows` the `os.startfile` will be used which
        returns nothing.
        On other operating systems, the Popen subprocess
        used to launch the file will be returned
    """
    file_path = str(file_path)
    if CURRENT_MACHINE == "Windows":
        os.startfile(file_path)
    elif CURRENT_MACHINE == "Darwin":
        return subprocess.Popen(
            ["open", file_path],
        )
    else:
        return subprocess.Popen(
            ["xdg-open", file_path],
        )


def open_file_manager(
        file_or_directory_path: FilePath,
        always_open_parent_dir: bool = False) -> Optional[subprocess.Popen]:
    """
    Function to open the file manager in the
    parent directory of the given path and highlighting it
    if supported by the file manager
    NOTE: THIS FUNCTION IS NOT FULLY TESTED
    ESPECIALLY AGAINST THE BSD FAMILY

    Parameters
    ----------
    file_or_directory_path : FilePath
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
    file_or_directory_path = str(file_or_directory_path)
    command_list = None
    if CURRENT_MACHINE == "Windows":
        command_list = [
            "explorer", "/select,{}".format(file_or_directory_path)
        ]
    elif CURRENT_MACHINE == "Darwin":
        command_list = [
            "open", "-R", file_or_directory_path
        ]
    else:
        # Many file managers do not support highlighting a file or folder
        # In unsupported file manager the parent directory will be opened
        linux_file_browser_command = \
            SUPPORTED_DE_FILE_BROWSERS.get(DESKTOP_ENVIRONMENT)
        if linux_file_browser_command is not None:
            command_list = [
                *linux_file_browser_command,
                file_or_directory_path
            ]
        else:
            if always_open_parent_dir:
                parent_path = str(Path(file_or_directory_path).parent)
                command_list = [
                    "xdg-open", parent_path
                ]
            else:
                raise UnsupportedDesktopEnvironment(
                    "{} is not a supported desktop environment"
                    .format(DESKTOP_ENVIRONMENT)
                )
    return subprocess.Popen(command_list)
