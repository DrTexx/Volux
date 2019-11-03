############
Installation
############

Install from pip
================
.. prompt:: bash $

    pip install volux

.. warning:: Markdown doesn't support a lot of the features of Sphinx,
          like inline markup and directives. However, it works for
          basic prose content. reStructuredText is the preferred
          format for technical documentation, please read `this blog post`_
          for motivation.

.. _this blog post: https://ericholscher.com/blog/2016/mar/15/dont-use-markdown-for-technical-docs/


Install from source
===================
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

Ignore this
===========
.. code-block:: python

   example_list = ['string']
