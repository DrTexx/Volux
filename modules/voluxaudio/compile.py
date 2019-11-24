from distutils.core import setup
from Cython.Build import cythonize
from os import path


here = path.abspath(path.dirname(__file__))

filenames = ["voluxaudio/__init__.py", "voluxaudio/hsv2ansi.py"]

full_file_paths = [path.join(here, filename) for filename in filenames]

setup(ext_modules=cythonize(full_file_paths))
