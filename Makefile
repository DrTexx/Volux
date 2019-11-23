init:

clean:
		rm -rf dist build *.egg-info .eggs

build:
		make clean
		python3 setup.py bdist_wheel sdist

install:
		pip install -r requirements.txt
		pip install dist/volux-*-*.whl

uninstall:
		pip uninstall volux -y

dev:
		make uninstall
		make clean
		make test
		make build
		make install

test:
		pip install pytest
		pytest tests

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

docker-run:
		xhost +local:root # for the lazy and reckless
		export containerId=$(docker ps -l -q)
		sudo docker run -it \
		--env="DISPLAY" \
		--env="ALSA_PCM_CARD=0" \
		--env="QT_X11_NO_MITSHM=1" \
		--volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
		--name volux \
		volux:0.9.16
		xhost -local:root
		sudo docker container rm --force volux

docker-build:
		sudo docker image build -t volux:0.9.16 .

# docker-safe:
# 		sudo docker run -it \
# 		--user=$(id --user) \
# 		--env="DISPLAY" \
# 		--volume="/etc/group:/etc/group:ro" \
# 		--volume="/etc/passwd:/etc/passwd:ro" \
# 		--volume="/etc/shadow:/etc/shadow:ro" \
# 		--volume="/etc/sudoers.d:/etc/sudoers.d:ro" \
# 		--volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
# 		--name volux \
# 		volux:0.9.16
# 		sudo docker container rm --force volux

.PHONY: init test
