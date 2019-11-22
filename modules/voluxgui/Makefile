init:
		pip install -r requirements.txt

dev:
		rm -rf dist build *.egg-info .eggs
		pip uninstall voluxgui -y
		python3 setup.py bdist_wheel sdist
		pip install dist/voluxgui-*-*.whl

.PHONY: init test
