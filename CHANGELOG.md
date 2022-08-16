# Change Log

## 0.0.1
* Base module in beta form

## 0.1.0
* Fixed `ModuleNotFound` error, by replacing line 5 (`from constants import ...`) of `src/_launchers.py` with (`from os_launchers.constants import ...`)

## 0.1.1
* Added exception raising to `open_terminal` and `open_file_manager` launchers if called on unsupported desktop environments
* Added `always_open_parent_dir` parameter to `open_file_manager` launcher to open the parent directory regardless of the supported or unsupported DE
* Added `exceptions.py` and within it `UnsupportedDesktopEnvironment` exception subclass
* Updated `README.md`. Changed line 17 (`pip install os_launchers`) to `pip install os-launchers`, Fixed grammatical issues