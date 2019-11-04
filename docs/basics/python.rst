######
Python
######

*******
Classes
*******

VoluxOperator
=============

Instantiating a New Operator
----------------------------

.. code-block:: python

   import volux
   vlx = volux.VoluxOperator()

.. note:: ``vlx`` will serve as the name of the operator instance in the following examples

Adding Modules to an Operator
-----------------------------

.. code-block:: python

   from voluxdemomodule import VoluxDemoModule
   demo_module = VoluxDemoModule()
   vlx.add_module()
