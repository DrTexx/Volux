from distutils.core import setup
from Cython.Build import cythonize
from os import path


here = path.abspath(path.dirname(__file__))

filenames = [
    "voluxgui/__init__.py",
    "voluxgui/__main__.py",
    "voluxgui/gui.py",
    "voluxgui/launch.py",
]

full_file_paths = [path.join(here, filename) for filename in filenames]

setup(ext_modules=cythonize(full_file_paths))
