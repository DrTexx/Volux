#!/usr/bin/env python -e

import setuptools  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path

__package_name__ = "voluxgui"

classifiers = [
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

project_urls = {  # a browsable URL for the project and a label for it, separated by a comma
    "Bug Reports": "https://github.com/drtexx/{}/issues".format(
        __package_name__
    ),
    "Source": "https://github.com/drtexx/{}".format(__package_name__),
    "Funding": "https://paypal.me/denverpallis",
    "Docs": "https://{}.readthedocs.io".format(__package_name__),
}

readme_filename = "README.md"
readme_encoding = "utf-8"
long_description_content_type = "text/markdown"

here = path.abspath(path.dirname(__file__))
with open(path.join(here, readme_filename), encoding=readme_encoding) as f:
    long_description = (
        f.read()
    )  # Get the long description from the README file

setuptools.setup(
    name=__package_name__,  # Required
    version="0.9.0",  # Required
    packages=[__package_name__],  # Required
    metadata_version="2.1",  # Optional
    summary="volux module which provides a gui for volux itself",  # Optional
    description="volux module which provides a gui for volux itself",  # Optional
    description_content_type="text/markdown",  # Optional
    author="Denver Pallis",
    author_email="DenverPallisProjects@gmail.com",
    license="GPLv3+",
    classifiers=classifiers,
    install_requires=["volux==0.9.16"],
    setup_requires=["wheel", "setuptools"],
    requires_python=[">=3"],
    requires_external=["python3-tk"],
    project_urls=project_urls,
    entry_points={  # Optional
        "console_scripts": [
            "{}={}:__main__.main".format(__package_name__, __package_name__)
        ]
    },
)
