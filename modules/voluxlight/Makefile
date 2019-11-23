init:

clean:
		rm -rf dist build *.egg-info .eggs

build:
		python3 setup.py bdist_wheel sdist

install:
		pip install -r requirements.txt
		pip install dist/voluxlight-*-*.whl

uninstall:
		pip uninstall voluxlight -y

dev:
		make uninstall
		make clean
		make build
		make install

.PHONY: init test
