######################
Installing from source
######################

.. warning:: If any of the code below looks unfamiliar or scary to you,
          building from source is not a good idea. It is highly recommended to
          install volux from pip or at least via the latest wheel release on
          pypi.

.. prompt:: bash $

    git clone https://github.com/DrTexx/Volux.git
    cd Volux
    python3 -m venv venv
    source venv/bin/activate
    pip install -r volux/demos/demo_volbar_requirements.txt
    pip install wheel setuptools --upgrade
    python3 setup.py bdist_wheel
    cd dist
    pip install volux-*.whl
