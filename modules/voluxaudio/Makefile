init:

build:
		rm -rf dist build *.egg-info .eggs
		python3 setup.py bdist_wheel sdist

install:
		sudo apt install libasound2
		pip install -r requirements.txt
		pip install dist/voluxaudio-*-*.whl

uninstall:
		pip uninstall voluxaudio -y

dev:
		make uninstall
		make build
		make install

.PHONY: init test
