######
Python
######

*******
Classes
*******

VoluxOperator
=============

Instantiating a new operator
----------------------------

.. code-block:: python

   import volux
   vlx = volux.VoluxOperator()

.. note:: ``vlx`` will serve as the name of the operator instance in the following examples

Adding modules to an operator
-----------------------------

.. code-block:: python

   from voluxdemomodule import VoluxDemoModule
   demo_module = VoluxDemoModule()
   vlx.add_module()
