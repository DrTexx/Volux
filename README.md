[![PyPI Version](https://img.shields.io/pypi/v/volux.svg)](https://pypi.python.org/pypi/volux/)
[![GitHub release](https://img.shields.io/github/release-pre/DrTexx/volux.svg)](https://GitHub.com/DrTexx/volux/releases/)
[![Documentation Status](https://readthedocs.org/projects/volux/badge/?version=latest)](https://volux.readthedocs.io/en/latest/?badge=latest)
[![GitHub license](https://img.shields.io/github/license/DrTexx/volux.svg?branch=master)](https://github.com/DrTexx/volux/blob/master/LICENSE)
[![Github all releases](https://img.shields.io/github/downloads/DrTexx/volux/total.svg)](https://GitHub.com/DrTexx/volux/releases/)
[![Platform: Windows,Mac,Linux](https://img.shields.io/badge/Platform-Windows%20%7C%20Mac%20%7C%20Linux-blue.svg)](#)

# Volux
| BRANCH  | BUILD | COVERAGE | REQUIREMENTS | ISSUES | OPEN PRs |
| ---     | ---          | ---      | ---          | ---    | ---      |
| Master  | [![Build Status](https://travis-ci.org/DrTexx/Volux.svg?branch=master)](https://travis-ci.org/DrTexx/Volux) | [![codecov](https://codecov.io/gh/DrTexx/Volux/branch/master/graph/badge.svg)](https://codecov.io/gh/DrTexx/Volux) | [![Requirements Status](https://requires.io/github/DrTexx/Volux/requirements.svg?branch=master)](https://requires.io/github/DrTexx/Volux/requirements/?branch=master) | [![GitHub issues](https://img.shields.io/github/issues/DrTexx/volux.svg?branch=master)](https://GitHub.com/DrTexx/volux/issues/) | [![GitHub pull-requests](https://img.shields.io/github/issues-pr/DrTexx/volux.svg?branch=master)](https://GitHub.com/DrTexx/volux/pull/) |
| Develop | ![Build Status](https://travis-ci.org/DrTexx/Volux.svg?branch=develop) | [![codecov](https://codecov.io/gh/DrTexx/Volux/branch/develop/graph/badge.svg)](https://codecov.io/gh/DrTexx/Volux/branch/develop) | [![Requirements Status](https://requires.io/github/DrTexx/Volux/requirements.svg?branch=develop)](https://requires.io/github/DrTexx/Volux/requirements/?branch=develop) |

## Description
Volux is a high-level media/entertainment workflow automation platform.

## Documentation
Volux uses readthedocs.io for it's documentation.

Read it [here](https://volux.readthedocs.io/en/latest/).

## Getting Started
### Installation
Install the latest stable build
```bash
$ pip install volux
```

### Launch GUI (in alpha)
```bash
$ volux launch
```

### Commands
```bash
$ volux --help
```

### Demo
Run the volume/light bar demo
```bash
$ volux demo bar
```

## About volux

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

### Installing from source
See [here](https://volux.readthedocs.io/en/latest/advanced/install-source.html#installing-from-source).

### Demo script
See [here](https://volux.readthedocs.io/en/latest/basics/intro.html#bar-demo)

While hovering over the bar:

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
| 📘 blue   | middle-click       | 💡 toggle bulb power        |

### Features in development
- Settings GUI
- Interface customisation

### Supported platforms

<img src="docs/Platform_Windows.svg" width="14pt"/>&nbsp;&nbsp; Windows 7 or later

<img src="docs/Platform_Mac.svg" width="14pt"/>&nbsp;&nbsp; MacOS _(WIP)_

<img src="docs/Platform_Linux.svg" width="14pt"/>&nbsp;&nbsp; Linux (most distributions)

### External Requirements
| Platform       | External Requirements      |
| ---            | ---                        |
| Darwin (MacOS) | ```$ brew install tcl-tk``` ```$ brew link tcl-tk --force``` |
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
| 64 bit | Debian 10 Buster | Gnome 3.30.2  | 3.7.3  | 0.9.4   | Working | Development conditions       |
| 64 bit | Ubuntu 16.04     | N/A           | 3.7    | 0.9.4   | Working | CI Conditions                |
| 64 bit | Windows 10       | N/A           | 3.7.3  | 0.9.4   | Working |                              |
| 64 bit | Windows 10       | N/A           | 3.7.2  | 0.8.16  | Working |                              |
| 64 bit | OSX 10.13.5      | N/A           | 3.7.3  | 0.8.16  | Broken  | Ironing out the creases      |

<br/>

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

Acknowledgments of work | [pencil icon](https://www.flaticon.com/free-icon/pencil-writing-tool-symbol-in-circular-button-outline_54602)
