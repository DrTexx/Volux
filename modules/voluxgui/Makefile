init:

clean:
		rm -rf dist build *.egg-info .eggs

build:
		python3 setup.py bdist_wheel sdist

install:
		pip install -r requirements.txt
		pip install dist/voluxgui-*-*.whl

uninstall:
		pip uninstall voluxgui -y

dev:
		make uninstall
		make clean
		make build
		make install

install-external-apt:
		apt install python3-tk

.PHONY: init test
