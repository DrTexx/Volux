[![PyPI Version](https://img.shields.io/pypi/v/volux.svg)](https://pypi.python.org/pypi/volux/)
[![GitHub release](https://img.shields.io/github/release-pre/DrTexx/volux.svg)](https://GitHub.com/DrTexx/volux/releases/)
[![GitHub license](https://img.shields.io/github/license/DrTexx/volux.svg?branch=master)](https://github.com/DrTexx/volux/blob/master/LICENSE)
[![Github all releases](https://img.shields.io/github/downloads/DrTexx/volux/total.svg)](https://GitHub.com/DrTexx/volux/releases/)
[![Platform: Windows,Mac,Linux](https://img.shields.io/badge/Platform-Windows%20%7C%20Mac%20%7C%20Linux-blue.svg)](#)

# Volux
| BRANCH  | BUILD | COVERAGE | REQUIREMENTS | ISSUES | OPEN PRs |
| ---     | ---          | ---      | ---          | ---    | ---      |
| Master  | [![Build Status](https://travis-ci.org/DrTexx/Volux.svg?branch=master)](https://travis-ci.org/DrTexx/Volux) | [![codecov](https://codecov.io/gh/DrTexx/Volux/branch/master/graph/badge.svg)](https://codecov.io/gh/DrTexx/Volux) | [![Requirements Status](https://requires.io/github/DrTexx/Volux/requirements.svg?branch=master)](https://requires.io/github/DrTexx/Volux/requirements/?branch=master) | [![GitHub issues](https://img.shields.io/github/issues/DrTexx/volux.svg?branch=master)](https://GitHub.com/DrTexx/volux/issues/) | [![GitHub pull-requests](https://img.shields.io/github/issues-pr/DrTexx/volux.svg?branch=master)](https://GitHub.com/DrTexx/volux/pull/) |
| Develop | [![Build Status](https://travis-ci.org/DrTexx/Volux.svg?branch=develop)](https://travis-ci.org/DrTexx/Volux) | [![codecov](https://codecov.io/gh/DrTexx/Volux/branch/develop/graph/badge.svg)](https://codecov.io/gh/DrTexx/Volux) | [![Requirements Status](https://requires.io/github/DrTexx/Volux/requirements.svg?branch=develop)](https://requires.io/github/DrTexx/Volux/requirements/?branch=develop) |

## Description
Volux is a high-level media/entertainment workflow automation platform.

### What does it do?
Volux operates using an `Operator` object and various instances of `VoluxModule` subclasses.

Each aspect of your media/entertainment setup is represented by it's own volux module.

The operator object acts as a hub for a standard method of communication between Volux modules added to it.

### Official Modules
| Module            | Aspect          | Controls              |
| ---               | ---             | ---                   |
| `VoluxBar`        | GUI Element     | display values, display colors, increase/decrease values, set values |
| `VoluxDemoModule` | CLI messages    | set value, get value |
| `VoluxDisplay`    | Monitor         | get monitor size (wip) |
| `VoluxLight`      | LIFX bulb       | set color, set power, get color, get power |
| `VoluxVolume`     | Computer Volume | set volume, get volume, set muted, get muted |

These modules can read/write data of the associated aspects in coordiation with each other to create seamless workflows.

### Demo script
In order to execute the demo script, you must installed the requirements in [`/volux/demos/demo_volbar_requirements.txt`](/volux/demos/demo_volbar_requirements.txt).

To install these requirements:
```bash
$ pip install -r volux/demos/demo_volbar_requirements.txt
```

Run the demo script
```bash
$ python3 -m volux
```

While hovering over the bar:

| Bar color | Action       | Result                   |
| ---       | ---          | ---                      |
| _any_     | right-click  | change bar color         |
| 📗 green  | scroll up    | increase volume          |
| 📗 green  | scroll down  | decrease volume          |
| 📗 green  | middle-click | mute                     |
| 🔴 red    | scroll up    | increase volume          |
| 🔴 red    | scroll down  | decrease volume          |
| 🔴 red    | middle-click | unmute                   |
| 📘 blue   | scroll up    | increase bulb brightness |
| 📘 blue   | scroll down  | decrease bulb brightness |
| 📘 blue   | middle-click | toggle bulb power        |

### What _will_ it do?
Features in development / planned for development
- Brightness control via mouse wheel
- Interface customisation

### Screenshots

| Mode                | State    | Image |
| :---:               | :---:    | :---: |
| Volume (active)     | active   | <img src="docs/volume-active.jpg"/> |
| Volume (inactive)   | inactive | <img src="docs/volume-inactive.jpg"/> |
| Mute (active)       | active   | <img src="docs/mute-active.jpg"/> |
| Brightness (active) | active   | <img src="docs/brightness-active.jpg"/> |

### Supported platforms

<img src="docs/Platform_Windows.svg" width="14pt"/>&nbsp;&nbsp; Windows 7 or later

<img src="docs/Platform_Mac.svg" width="14pt"/>&nbsp;&nbsp; MacOS _(WIP)_

<img src="docs/Platform_Linux.svg" width="14pt"/>&nbsp;&nbsp; Linux (most distributions)

## Installation
<img src="docs/note-icon.svg" width="14pt"/> **NOTE:** Under some operating systems / linux distros all references to ___'pip'___ must be replaced with ___'pip3'___. Debian is an example of this. This is often the case to prevent confusion between Python 2.7.x interpreters and Python 3.x interpreters

<img src="docs/note-icon.svg" width="14pt"/> **NOTE:** Under some operating systems / linux distros all references to ___'python'___ must be replaced with ___'python3'___. Debian is an example of this. This is often the case to prevent confusion between Python 2.7.x interpreters and Python 3.x interpreters

<img src="docs/note-icon.svg" width="14pt"/> **NOTE:** If you recieve the error `error: invalid command 'bdist_wheel'` when running `python setup.py bdist_wheel`, try the following: Try upgrading the wheel package `pip install wheel --upgrade`. No luck? Try reinstalling the wheel package. Failing that, try upgrading pip `python3 -m pip install pip --upgrade`. Failing that, _ensure_ you installed the [requirements for your platform](#installation). Failing that, instead build with the command `python setup.py build`. If you're still having issues, please submit a detailed issue on Github.

### Requirements
| Platform       | External Requirements      |
| ---            | ---                        |
| Windows        | ```> pip install https://github.com/AndreMiras/pycaw/archive/master.zip``` |
| Darwin (MacOS) | ```$ brew install tcl-tk``` ```$ brew link tcl-tk --force``` |
| Linux (Debian) | ```$ sudo apt-get install python3-tk python3-xlib python3-dbus libasound2-dev python3-dev``` |

### Installation
| Installation Method                | Command/s                                           | Platforms
| ---                                | ---                                                 | ---
| pip (as user) ***recommended!***   | ```> pip install volux --user```                    | Windows/Unix
| pip (as root)                      | ```$ sudo pip install volux```                      | Unix
| wheel (.whl) (as user)             | ```> pip install volux-*-py3-none-any.whl --user``` | Windows/Unix
| wheel (.whl) (as root)             | ```$ sudo pip install volux-*-py3-none-any.whl```   | Unix

### Build from source
Clone this repository:

    $ git clone https://github.com/DrTexx/volux.git

Install pip requirements:

    $ cd volux
    $ pip install -r requirements.txt --user

_Issues with pip? Please see notes under [Installation](#installation)_

Build:

    $ pip install wheel --upgrade
    $ python setup.py bdist_wheel

_Issues with building? Please see notes under [Installation](#installation)_

Install:

    Check the 'dist' folder for volux-x.x.x-py3-*.whl, then see "Installation" above

## Using Volux
All interactions with Volux are only valid when hovering over the bar Volux produces. This allows you to interact with Volux without loosing your ability to scroll in other applications.

### Launching
In order to launch Volux, open your platform's command-line/terminal and run the following:

    python -m volux

<img src="docs/note-icon.svg" width="14pt"/> **NOTE:** This will not be necessary in future releases (however still possible). An application launcher will be provided in addition to the option to launch at startup.

### Modes
To cycle between modes in Volux, _right-click_ the main bar. By default, a green bar signifies **volume mode** and a blue bar signifies **brightness mode** (wip).

### Volume/brightness
While in volume or brightness mode, _scroll up/down_ to increase/decrease volume or brightness while hovering over the main bar.

### Exit
To exit Volux, _double right-click_ the bar at any time.

## Issues and bugs
If you have any problems running Volux, please kindly post an issue to this repository. Issues can be solved much faster if you can provide:

- Your OS
- Your desktop environment (if using Linux)
- Your python version
- A Summary of issues experienced
- Any relevant screenshot/s

Volux is developed under Debian 9 Stretch (Linux) using GNOME 3.22.2 and Python 3.5. Providing you've correctly installed all dependencies, Volux is almost guranteed to work under these conditions.

Additional testing has been done under these conditions:

| Archi. | Operating System | Desktop Env   | Python | Verison | Status  | Notes                        |
| ---    | ---              | ---           | ---    | ---     | ---     | ---                          |
| 64 bit | Debian 9 Stretch | Gnome 3.22.2  | 3.5    | 0.8.16  | Working | Development conditions       |
| 64 bit | Ubuntu _ver=?_   | Gnome _ver=?_ | 3.6    |         | Working |                              |
| 64 bit | Windows 10       | N/A           | 3.7    | 0.8.16  | Working | Reimplementation successful! |
| 64 bit | Windows 10       | N/A           | 3.7.2  | 0.8.16  | Working |                              |
| 64 bit | OSX 10.13.5      | N/A           | 3.7.3  | 0.8.16  | Broken  | Ironing out the creases      |

<br/>

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

Acknowledgments of work | [pencil icon](https://www.flaticon.com/free-icon/pencil-writing-tool-symbol-in-circular-button-outline_54602)
