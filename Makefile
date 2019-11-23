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
		pip uninstall volux -y

clean:
		rm -rf dist build *.egg-info .eggs

dev:
		make uninstall
		make clean
		make test
		make build
		make install

build-all:
		make build
		cd modules/voluxaudio && make build
		cd modules/voluxbar && make build
		cd modules/voluxgui && make build
		cd modules/voluxlight && make build
		cd modules/voluxlightvisualiser && make build
		cd modules/voluxvolume && make build

install-all:
		make install
		cd modules/voluxaudio && make install
		cd modules/voluxbar && make install
		cd modules/voluxgui && make install
		cd modules/voluxlight && make install
		cd modules/voluxlightvisualiser && make install
		cd modules/voluxvolume && make install

uninstall-all:
		make uninstall
		cd modules/voluxaudio && make uninstall
		cd modules/voluxbar && make uninstall
		cd modules/voluxgui && make uninstall
		cd modules/voluxlight && make uninstall
		cd modules/voluxlightvisualiser && make uninstall
		cd modules/voluxvolume && make uninstall

clean-all:
		make clean
		cd modules/voluxaudio && make clean
		cd modules/voluxbar && make clean
		cd modules/voluxgui && make clean
		cd modules/voluxlight && make clean
		cd modules/voluxlightvisualiser && make clean
		cd modules/voluxvolume && make clean

dev-all:
		make dev
		cd modules/voluxaudio && make dev
		cd modules/voluxbar && make dev
		cd modules/voluxgui && make dev
		cd modules/voluxlight && make dev
		cd modules/voluxlightvisualiser && make dev
		cd modules/voluxvolume && make dev

gui:
		make dev
		volux launch

.PHONY: init test
