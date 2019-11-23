#!/usr/bin/env python -e

"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

import setuptools  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path

# personal note: to refresh auto-documentation
# (navigate to repo root first)
# sphinx-apidoc -o docs/modules . test_* cpaudio setup.py voluxdisplay/cpdisplay

# how-to metadata
# https://packaging.python.org/specifications/core-metadata/

# __platform__ = "" # (multiple-use) only if the platform is not listed in the “Operating System” Trove classifiers
# __supported_platform__ = #
# __maintainer__ = "Denver Pallis" # should be omitted if it is identical to Author
# __maintainer_email__ = "DenverPallisProjects@gmail.com" # should be omitted if it is identical to Author
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
    "Bug Reports": "https://github.com/drtexx/{}/issues".format(__name__),
    "Source": "https://github.com/drtexx/{}".format(__name__),
    "Funding": "https://paypal.me/denverpallis",
    "Docs": "https://{}.readthedocs.io".format(__name__),
}

__package_name__ = "volux"

readme_filename = "README.md"
readme_encoding = "utf-8"
long_description_content_type = "text/markdown"

here = path.abspath(path.dirname(__file__))
with open(path.join(here, readme_filename), encoding=readme_encoding) as f:
    long_description = (
        f.read()
    )  # Get the long description from the README file
with open(
    path.join(here, "{}/version.txt".format(__package_name__)), "r"
) as f:
    version = f.readline().splitlines()[0]

setuptools.setup(
    name=__package_name__,  # Required
    version=version,  # Required
    packages=setuptools.find_packages(),  # Required
    url="https://github.com/drtexx/{}".format(__package_name__),  # required
    metadata_version="2.1",  # Optional
    summary="High-level media/entertainment workflow automation platform",  # Optional
    description="High-level media/entertainment workflow automation platform",  # Optional
    description_content_type="text/markdown",  # Optional
    keywords="volux media interface workflow automation platform iot lifx volume sound light tk tkinter gui modular",  # A list of additional keywords to be used to assist searching for the distribution in a larger catalog
    author="Denver Pallis",
    author_email="DenverPallisProjects@gmail.com",
    license="GPLv3+",
    classifiers=classifiers,
    install_requires=["colorama==0.4.1"],  # requirements
    setup_requires=["wheel", "setuptools"],
    requires_python=[">=3"],  # required python version
    requires_external=[],
    project_urls=project_urls,
    long_description=long_description,  # Optional
    long_description_content_type=long_description_content_type,  # Optional
    package_data={"volux": ["version.txt"]},  # Optional
    entry_points={  # Optional
        "console_scripts": [
            "{}={}:__main__.main".format(__package_name__, __package_name__)
        ]
    },
)
