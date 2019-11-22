init:
		pip install -r requirements.txt

dev:
		rm -rf dist/
		pip uninstall voluxaudio -y
		python3 setup.py bdist_wheel sdist
		pip install dist/voluxaudio-*-*.whl

.PHONY: init test
