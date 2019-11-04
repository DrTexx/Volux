#!/usr/bin/env python -e

"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# personal note: to refresh auto-documentation
# (navigate to repo root first)
# sphinx-apidoc -o docs/modules . test_* cpaudio setup.py voluxdisplay/cpdisplay

# how-to metadata
# https://packaging.python.org/specifications/core-metadata/

import volux  # CHANGE THIS TO MATCH YOUR PACKAGE'S NAME!

mypackage = volux

readme_filename = 'README.md'
readme_encoding = 'utf-8'
long_description_content_type = 'text/markdown'

import setuptools # Always prefer setuptools over distutils
from codecs import open # To use a consistent encoding
from os import path
here = path.abspath(path.dirname(__file__))
with open(path.join(here, readme_filename), encoding=readme_encoding) as f:
    long_description = f.read() # Get the long description from the README file

setuptools.setup(
    metadata_version=mypackage.__metadata_version__, # Optional
    name=mypackage.__name__, # Required
    version=mypackage.__version__, # Required
    summary=mypackage.__summary__, # Optional
    description=mypackage.__description__, # Optional
    description_content_type=mypackage.__description_content_type__,  # Optional
    keywords=mypackage.__keywords__,
    url=mypackage.__homepage__,
    author=mypackage.__author__,
    author_email=mypackage.__author_email__,
    license=mypackage.__license__,
    classifiers=mypackage.__classifiers__,
    install_requires=mypackage.__requires_dist__,
    requires_python=mypackage.__requires_python__,
    requires_external=mypackage.__requires_external__,
    project_urls=mypackage.__project_urls__,

    long_description=long_description, # Optional
    long_description_content_type=long_description_content_type, # Optional

    package_data={ # Optional
        'sample': ['package_data.dat'],
    },
    entry_points={ # Optional
        'console_scripts': [
            '{}={}:__main__.main'.format(mypackage.__name__,mypackage.__name__),
        ],
    },
    packages=setuptools.find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
)
