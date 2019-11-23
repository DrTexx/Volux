init:

clean:
		rm -rf dist build *.egg-info .eggs

build:
		make clean
		python3 setup.py bdist_wheel sdist

install:
		pip install -r requirements.txt
		pip install dist/voluxaudio-*-*.whl

uninstall:
		pip uninstall voluxaudio -y

dev:
		make uninstall
		make build
		make install

install-external-apt:
		apt install libasound2

.PHONY: init test
