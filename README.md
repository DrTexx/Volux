[![Build Status](https://travis-ci.org/DrTexx/Volux.svg?branch=master)](https://travis-ci.org/DrTexx/Volux)
[![Documentation Status](https://readthedocs.org/projects/volux/badge/?version=latest)](https://volux.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/DrTexx/Volux/branch/master/graph/badge.svg)](https://codecov.io/gh/DrTexx/Volux)
[![Requirements Status](https://requires.io/github/DrTexx/Volux/requirements.svg?branch=master)](https://requires.io/github/DrTexx/Volux/requirements/?branch=master)

[![PyPI Version](https://img.shields.io/pypi/v/volux.svg)](https://pypi.python.org/pypi/volux/)
[![GitHub release](https://img.shields.io/github/release-pre/DrTexx/volux.svg)](https://GitHub.com/DrTexx/volux/releases/)
[![GitHub license](https://img.shields.io/github/license/DrTexx/volux.svg?branch=master)](https://github.com/DrTexx/volux/blob/master/LICENSE)
[![Github all releases](https://img.shields.io/github/downloads/DrTexx/volux/total.svg)](https://GitHub.com/DrTexx/volux/releases/)

[![Platform: Windows,Mac,Linux](https://img.shields.io/badge/Platform-Windows%20%7C%20Mac%20%7C%20Linux-blue.svg)](#)
[![GitHub issues](https://img.shields.io/github/issues/DrTexx/volux.svg?branch=master)](https://GitHub.com/DrTexx/volux/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/DrTexx/volux.svg?branch=master)](https://GitHub.com/DrTexx/volux/pull/)

<!-- | BRANCH  | STATUS |
| ---     | ---    |
| Dev  | [![Build Status](https://travis-ci.org/DrTexx/Volux.svg?branch=dev)](https://travis-ci.org/DrTexx/Volux) [![codecov](https://codecov.io/gh/DrTexx/Volux/branch/dev/graph/badge.svg)](https://codecov.io/gh/DrTexx/Volux) [![Requirements Status](https://requires.io/github/DrTexx/Volux/requirements.svg?branch=dev)](https://requires.io/github/DrTexx/Volux/requirements/?branch=dev) | -->

# Volux
## Description
Volux is a high-level media/entertainment workflow automation platform.

## Demos
- demo video
- demo video
- demo video

## Getting Started
### Important Notes
#### Incompatibilities
Please note that pyaudio - a requirement of the voluxaudio module - does not support python versions _above_ 3.6.9 on windows 10. Any version of Python 3.6.x should work fine.
### Installation
#### Requirements

| PACKAGE    | OPERATING SYSTEM | REQUIREMENTS |
| ---        | ---              | ---          |
| Volux      | Any              | [Python 3.x.x](https://www.python.org/downloads) **\*** |
| Volux Audio | Any       | - [Python 3.6.8](https://www.python.org/downloads/release/python-368/) **\***</br>- Portaudio19 **\***</br>- Libasound2 **\*** |
| Volux Gui | Any | - Tkinter **\*\*** |

**\* may already be installed on your OS, only install if install fails**

**\*\* normally installed by default with python 3**

#### Installing Volux and modules
To install Volux, enter the following into your operating system's CLI

- Windows users, use ***powershell***
- Mac/Linux users, use ***terminal*** \*

\* note for Linux users: install in a virtual environment to avoid heartache

| PACKAGE | INSTALL COMMAND |
| ---     | ---             |
| Volux   | `pip install volux` |
| Volux Audio | `pip install voluxaudio` |
| Volux Gui | `pip install voluxgui` |
| Volux Light | `pip install voluxlight` |

<!-- python3-tk python3-dev python3-venv portaudio19-dev -->

### Using Volux
Enter the following in your operating system's CLI

| ACTION        | COMMAND        |
| ---           | ---            |
| Launch Volux  | `volux launch` \* |
| List commands | `volux --help` |

\* _make sure voluxgui is installed first or you'll get an error!_

## Documentation
**For more information on how to use volux** and how it works, check out the **documentation [here](https://volux.readthedocs.io/en/latest/).**

<!-- ## Getting Started
### Important Notes
#### Incompatibilities
Please note that pyaudio - a requirement of the voluxaudio module - does not support python 3.8 on windows 10. Any version of Python 3.6.x should work fine.

### Installation
Install system requirements

| OS | Command |
| --- | --- |
| Debian 10 | `$ sudo apt install python3 python3-tk python3-dev python3-venv libasound2-dev portaudio19-dev` |
| Windows 10 | Install [python3.6.x](https://www.python.org/downloads/) (if not already installed). Install Microsoft Visual C++ 14.0 from [this installer](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16). Check the 'C++ build tools' checkbox and click 'Install' |
| Darwin (MacOS) | `$ brew install tcl-tk` `$ brew link tcl-tk --force` | -->

### What does it do?
Volux operates using an `Operator` object and various instances of `VoluxModule` subclasses.

Each aspect of your media/entertainment setup is represented by it's own volux module.

The operator object acts as a hub for a standard method of communication between volux modules added to it.

<!-- ### Official Modules
| Module            | Aspect          | Controls              |
| ---               | ---             | ---                   |
| `VoluxBar`        | GUI Element     | display values, display colors, increase/decrease values, set values |
| `VoluxDemoModule` | CLI messages    | set value, get value |
| `VoluxDisplay`    | Monitor         | get monitor size (wip) |
| `VoluxLight`      | LIFX bulb       | set color, set power, get color, get power |
| `VoluxVolume`     | Computer Volume | set volume, get volume, set muted, get muted | -->

These modules can read/write data of the associated aspects in coordination with each other to create seamless workflows.

### Installing from source
See [here](https://volux.readthedocs.io/en/latest/advanced/install-source.html#installing-from-source).

<!-- While hovering over the bar:

| Bar color | Action             | Result                     |
| ---       | ---                | ---                        |
| _any_     | right-click        | change bar color           |
| _any_     | double right-click | exit volux                 |
| 📗 green  | scroll up          | 🔉 increase volume          |
| 📗 green  | scroll down        | 🔉 decrease volume          |
| 📗 green  | middle-click       | 🔇 mute                     |
| 🔴 red    | scroll up          | 🔉 increase volume          |
| 🔴 red    | scroll down        | 🔉 decrease volume          |
| 🔴 red    | middle-click       | 🔇 unmute                   |
| 📘 blue   | scroll up          | 💡 increase bulb brightness |
| 📘 blue   | scroll down        | 💡 decrease bulb brightness |
| 📘 blue   | middle-click       | 💡 toggle bulb power        | -->

<!-- ### Features in development
- Settings GUI
- Interface customisation -->

### Basic script for creating a workflow
#### Breakdown of setup
1. Import the framework + essentials
  ```python
  import volux
  ```
2. Import modules for use
  ```python
  from voluxcliprint import VoluxCliPrint
  from voluxaudio import VoluxAudio
  from voluxGui import VoluxGui
  ```
3. Create operator object
  ```python
  vlx = VoluxOperator()
  ```
4. Load the modules into the operator
  ```python
  vlx.add_module(VoluxCliPrint())
  vlx.add_module(VoluxAudio())
  vlx.add_module(
      VoluxGui(shared_modules=[vlx.audio,vlx.cli]),
      req_permissions=[
          volux.RequestNewConnection,
          volux.RequestGetConnections,
          volux.RequestStartSync
      ]
  )
  ```
5. Launch the GUI!
  ```python
  vlx.gui.init_window()
  ```

<!-- ### Supported platforms

<img src="docs/Platform_Windows.svg" width="14pt"/>&nbsp;&nbsp; Windows 7 or later

<img src="docs/Platform_Mac.svg" width="14pt"/>&nbsp;&nbsp; MacOS _(WIP)_

<img src="docs/Platform_Linux.svg" width="14pt"/>&nbsp;&nbsp; Linux (most distributions) -->

<!-- ### External Requirements
| Platform       | External Requirements      |
| ---            | ---                        | -->
<!-- | Linux (Debian) | ```$ sudo apt-get install python3-tk python3-xlib python3-dbus libasound2-dev python3-dev``` | -->

## Issues and bugs
If you have any problems running Volux, please kindly post an issue to this repository. Issues can be solved much faster if you can provide:

- Operating system
- Desktop environment (if using Linux)
- Python version
- Summary of issues experienced
- Relevant screenshot/s (if applicable)

Additional testing has been done under these conditions:

| Archi. | Operating System | Desktop Env   | Python | Verison | Status  | Notes                        |
| ---    | ---              | ---           | ---    | ---     | ---     | ---                          |
| 64 bit | Debian 10 Buster | Gnome 3.30.2  | 3.7.3  | 0.9.18   | Working | Development conditions       |
| 64 bit | Ubuntu 18.04     | N/A           | 3.5    | 0.9.17   | Working | CI Conditions                |
| 64 bit | Ubuntu 18.04     | N/A           | 3.6    | 0.9.17   | Working | CI Conditions                |
| 64 bit | Ubuntu 18.04     | N/A           | 3.7    | 0.9.17   | Working | CI Conditions                |
| 64 bit | Ubuntu 18.04     | N/A           | 3.8    | 0.9.17   | Working | CI Conditions                |
| 64 bit | Windows 10       | N/A           | 3.7.8  | 0.9.17   | Working | - |
| 64 bit | OSX 10.13.5      | N/A           | 3.7.3  | 0.9.17  | Unsupported  | Ironing out the creases      |

<br/>

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

<!-- Acknowledgments of work | [pencil icon](https://www.flaticon.com/free-icon/pencil-writing-tool-symbol-in-circular-button-outline_54602) -->
