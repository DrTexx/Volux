#!/usr/bin/env python -e

import setuptools  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path

__package_name__ = "voluxgui"

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
    version="0.1.0",  # Required
    packages=[__package_name__],  # Required
    metadata_version="2.1",  # Optional
    summary="volux module which provides a gui for volux itself",  # Optional
    description="volux module which provides a gui for volux itself",  # Optional
    description_content_type="text/markdown",  # Optional
    author="Denver Pallis",
    author_email="DenverPallisProjects@gmail.com",
    license="GPLv3+",
    install_requires=["volux>=0.9.16,<1.0.0"],
    setup_requires=["wheel", "setuptools"],
    python_requires=">=3",
    requires_external=["python3-tk"],
    entry_points={  # Optional
        "console_scripts": [
            "{}={}:__main__.main".format(__package_name__, __package_name__)
        ]
    },
)
