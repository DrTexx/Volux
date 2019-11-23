#!/usr/bin/env python -e

"""
High-level media/entertainment workflow automation platform
"""

from .essentials import get_version
from .operator import VoluxOperator
from .module import VoluxModule
from .core import VoluxCore
from .demo import VoluxDemo
from .connection import VoluxConnection
from .suppress import SuppressStdoutStderr
from .request import *
from .coremodules import *

__version__ = get_version()
