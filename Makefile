init:
		make install

test:
		py.test tests

build:
		python3 setup.py bdist_wheel sdist

install:
		pip install -r requirements.txt
		pip install dist/volux-*-*.whl

uninstall:
		pip uninstall volux voluxaudio -y

clean:
		rm -rf dist build *.egg-info .eggs

dev:
		make uninstall
		make clean
		make test
		make build
		make install
		cd modules/voluxaudio && make dev
		cd modules/voluxgui && make dev

gui:
		make dev
		volux launch

.PHONY: init test
