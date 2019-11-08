#!/usr/bin/env python -e

"""
docstring
"""

from .operator import *
from .module import *
from .core import *
from .demo import *

__metadata_version__ = "2.1"
__name__ = "volux"
__version__ = "0.9.9"
# __platform__ = "" # (multiple-use) only if the platform is not listed in the “Operating System” Trove classifiers
# __supported_platform__ = #
__summary__ = "High-level media/entertainment workflow automation platform"
__description__ = "High-level media/entertainment workflow automation platform"
__description_content_type__ = "text/markdown"
__keywords__ = "volux media interface workflow automation platform iot lifx volume sound light tk tkinter gui modular"  # A list of additional keywords to be used to assist searching for the distribution in a larger catalog.
__homepage__ = "https://github.com/drtexx/volux"
__author__ = "Denver Pallis"
__author_email__ = "DenverPallisProjects@gmail.com"
# __maintainer__ = "Denver Pallis" # should be omitted if it is identical to Author
# __maintainer_email__ = "DenverPallisProjects@gmail.com" # should be omitted if it is identical to Author
__license__ = "GPLv3+"
__classifiers__ = [
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Environment :: MacOS X",
    "Environment :: Win32 (MS Windows)",
    "Environment :: X11 Applications",
    "Intended Audience :: Developers",
    "Intended Audience :: End Users/Desktop",
    "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    "Natural Language :: English",
    "Operating System :: MacOS",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Topic :: Games/Entertainment",
    "Topic :: Home Automation",
    "Topic :: Multimedia",
    "Topic :: Scientific/Engineering :: Human Machine Interfaces",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: User Interfaces",
]
__requires_dist__ = [  # requirements
    "lifxlan==1.2.5",
    "pycaw; platform_system == 'Windows'",
    "comtypes==1.1.7; platform_system == 'Windows'",
    "pyalsaaudio==0.8.4; platform_system == 'Linux'",
    "colorama==0.4.1",
]
__requires_python__ = [">=3"]  # required python version
__requires_external__ = []  # external requirements
__project_urls__ = {  # a browsable URL for the project and a label for it, separated by a comma
    "Bug Reports": "https://github.com/drtexx/{}/issues".format(__name__),
    "Source": "https://github.com/drtexx/{}".format(__name__),
    "Funding": "https://paypal.me/denverpallis",
    "Docs": "https://{}.readthedocs.io".format(__name__),
}

# metadata standard: https://packaging.python.org/specifications/core-metadata/
