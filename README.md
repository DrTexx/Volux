| BRANCH  | BUILD STATUS | COVERAGE | REQUIREMENTS | ISSUES | OPEN PRs |
| ---     | :---:        | :---:    | :---:        | :---:  | :---:    |
| Master  | [![Build Status](https://travis-ci.org/DrTexxOfficial/volux.svg?branch=master)](https://travis-ci.org/DrTexxOfficial/volux) | [![codecov](https://codecov.io/gh/DrTexxOfficial/volux/branch/master/graph/badge.svg)](https://codecov.io/gh/DrTexxOfficial/volux) | [![Requirements Status](https://requires.io/github/DrTexxOfficial/volux/requirements.svg?branch=master)](https://requires.io/github/DrTexxOfficial/volux/requirements/?branch=master) | [![GitHub issues](https://img.shields.io/github/issues/DrTexxOfficial/volux.svg?branch=master)](https://GitHub.com/DrTexxOfficial/volux/issues/) | [![GitHub pull-requests](https://img.shields.io/github/issues-pr/DrTexxOfficial/volux.svg?branch=master)](https://GitHub.com/DrTexxOfficial/volux/pull/) |
| Develop | [![Build Status](https://travis-ci.org/DrTexxOfficial/volux.svg?branch=develop)](https://travis-ci.org/DrTexxOfficial/volux) | [![codecov](https://codecov.io/gh/DrTexxOfficial/volux/branch/develop/graph/badge.svg)](https://codecov.io/gh/DrTexxOfficial/volux) | [![Requirements Status](https://requires.io/github/DrTexxOfficial/volux/requirements.svg?branch=develop)](https://requires.io/github/DrTexxOfficial/volux/requirements/?branch=develop)

# Debug Interface - volux 

[![PyPI Version](https://img.shields.io/pypi/v/volux.svg)](https://pypi.python.org/pypi/volux/)
[![GitHub release](https://img.shields.io/github/release-pre/drtexxofficial/volux.svg)](https://GitHub.com/DrTexxOfficial/volux/releases/)
[![GitHub license](https://img.shields.io/github/license/DrTexxOfficial/volux.svg?branch=master)](https://github.com/DrTexxOfficial/volux/blob/master/LICENSE)
[![Github all releases](https://img.shields.io/github/downloads/DrTexxOfficial/volux/total.svg)](https://GitHub.com/DrTexxOfficial/volux/releases/)

<img src="docs/volux_logo.png" alt="volux logo" width="200"/>

## Installation
### Install via pip
Install as user (recommended):

    $ pip3 install volux --user

Install as root:

    $ sudo pip3 install volux

### Install from source
Clone this repository:

    $ git clone https://github.com/DrTexxOfficial/volux.git

Install requirements:

    $ cd volux
    $ pip3 install -r requirements.txt --user
    
## Script Functionality
### User-Written Verbosity-Dependant Debug Messages
- information is only show when A and B are satisfied
    - debugging is active
    - the threshold verbosity is reached or exceeded (this threshold is specified on a per-message basis)
- verbosity can be
    - set in advanced
    - **modified on-the-fly**
- multiple **external functions** can be executed in a single-line
- users can write their own debugging messages on the status of each function's progress
- console output is colour-coded (based on verbosity levels)

## What is the purpose?
My console had become populated by indecernable walls of debugging text, all thanks to riddling my scripts with lines like `print(str(var),var)` for debugging.
So I created a module to maintain my sanity and save my time.

## Examples
Initial config:
```python3
from volux import volux
volux = volux(3,True)
dpm = volux.print_message
```
Generic example:
```
[IN ]: dpm(2,"message with","sub-message")
[OUT]: [3][2]<=[2018-12-10 01:54:59.845995] message with | sub-message
```

<br/>

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
