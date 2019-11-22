#!/usr/bin/env python -e

import setuptools  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path

__package_name__ = "voluxaudio"

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
    version="1.0.0",  # Required
    packages=[__package_name__],  # Required
    metadata_version="2.1",  # Optional
    summary="volux module for extracting audio data",  # Optional
    description="volux module for extracting audio data",  # Optional
    description_content_type="text/markdown",  # Optional
    author="Denver Pallis",
    author_email="DenverPallisProjects@gmail.com",
    license="GPLv3+",
    install_requires=["volux==0.9.16"],
    setup_requires=["wheel", "setuptools"],
    requires_python=[">=3"],
    requires_external=["libasound2-dev"],
)
