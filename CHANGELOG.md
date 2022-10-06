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

## 0.1.2
* Fixed usage of f-string in `src/os-launchers/_launchers.py` (line 158). Changed to `.format` for more compatibility with older python versions
* More efficient implementation of powershell and cmd launchers (merging and using ternary operators)

## 0.2.0
* Added `conversions.py` to `os_launchers/` containing classes to be able to easily convert between the type hint's allowed types
* Added `RegexPattern` type hint to `os_launchers/type_hints.py` for either a compiled regex pattern or string equivalent
* Added `profiles/` to `os_launchers/` containing specific profiles for each OS and unix DE (as of now, the profiles are only written for unix DEs) and their components such as terminals and file managers (as of now, stored separately in their respective files)
* Removed unused constants from `os_launchers/constants/unix_family.py`
