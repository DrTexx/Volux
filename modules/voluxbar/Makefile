init:

clean:
		rm -rf dist build *.egg-info .eggs

build:
		make clean
		python3 setup.py bdist_wheel sdist

install:
		pip install -r requirements.txt
		pip install dist/voluxbar-*-*.whl

uninstall:
		pip uninstall voluxbar -y

dev:
		make uninstall
		make build
		make install

install-external-apt:
		apt install python3-tk

.PHONY: init test
