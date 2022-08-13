# os-launchers

A collection of cross-platform launchers to interact with the OS from a high level
point, simplifying interactions like opening the terminal on every platform
or opening a file on multiple platforms

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for personal use, development or testing purposes. There are two ways which you can get the project working:

### Pre-Packaged Wheels

This project is available on [pypi.org](https://pypi.org/), therefore, you can easily
install this project through pip:

    ```
    pip install os_launchers
    ```

### From Source

As a result of the pypi build only contains the stable builds it could behind
the development version, so you may want to install the package from the development package,
or maybe you would like to contribute to the project

#### Installing the pre-requisites

1. You __MUST__ have a [python](https://www.python.org/) >= 3.5 interpreter installed on your machine. In order to check your python version, you can do:

    ```
    python3 --version
    ```
   
    If you are on ___Windows___, you can visit the [download section](https://www.python.org/downloads/) of the official python website in order to download a matching version.

    If you are on ___Linux OR Mac___, you already have python installed, but it is highly possible that is does not match the minimum required version. You can get a matching version using the package manager on your machine, like so:

    On _Ubuntu_:

    ```
    sudo apt install python3
    ```
   
    On _Fedora_:

    ```
    sudo dnf install python3
    ```
   
    On _Mac (Using homebrew)_:
     
    ```
    brew install python
    ```


2. You __MUST__ also have ___pip___ installed. In order to check if you have pip installed, you can do:

    ```
    pip --version
    ```
   
    If you are on ___Windows___, you probably have pip installed alongside python. If not, follow the [official pip installation guide](https://pip.pypa.io/en/stable/installation/).

    If you are on ___Linux OR Mac___, using your package manager you can install pip, like so:

    On _Ubuntu_:
    
    ```
    sudo apt install python3-pip
    ```
    
    On _Fedora_:

    ```
    sudo dnf install python3-pip
    ```
    On _Mac_:

    ```
    python3 -m pip install --upgrade pip
    ```


3. You __MUST__ also have [___git___](https://git-scm.com/) installed on your machine to be able to copy the repo, otherwise you are going to have to manually copy and paste the files' content. In order to check if you have git installed, you can do:

    ```
    git --version
    ```

    If you are on ___Windows___, you can visit the [download section](https://git-scm.com/downloads) of the official git website and follow their guides to have it setup on your machine.

    If you are on ___Linux OR Mac___, you can easily install git through your package manager, like so:

    On _Ubuntu_:

    ```
    sudo apt install git
    ```
    On _Fedora_:

    ```
    sudo dnf install git
    ```
    On _Mac (Using homebrew)_:

    ```
    brew install git
    ```

#### Setting up the module

6. Clone the repository (copy the source code):

    ```
    git clone https://github.com/Eastern-Skill7173/os-launchers.git
    ```

    _TIP:_ you can add a `--depth 1` to the end of the command to only copy the latest version of each file if you are planing on just using the project, like so:
    ```
    git clone https://github.com/Eastern-Skill7173/os-launchers.git --depth 1
    ```

After cloning the repo, switch to it's directory, and run the following command through your terminal:

    ```
    pip install .
    ```

## Built With

* [Python](https://www.python.org/) - The core programming language

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) & [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* [**Eastern-Skill7173**](https://github.com/Eastern-Skill7173) - *creator and maintainer*

See also the list of [contributors](https://github.com/Eastern-Skill7173/os-launchers/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Special thanks to the python team
* Anyone who has shared or committed to the project
* Also, [_Billie Thompson_](https://github.com/PurpleBooth) for this README template
