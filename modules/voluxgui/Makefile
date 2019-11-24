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

build-c:
		python compile.py build_ext -b build_c

clean-c:
		rm -rf build_c

dev-c:
		make clean-c
		make build-c

install-external-apt:
		apt install python3-tk

.PHONY: init test
