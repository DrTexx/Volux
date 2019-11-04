##########
voluxlight
##########

*******
Classes
*******

VoluxLight
==========

Adding a new light
------------------

.. code-block:: python

   from voluxlight import VoluxLight
   vlight = VoluxLight(<label>)

   <operator instance>.add_module(vlight)

``<label>`` must be a string. This is the name you've set via your mobile for a LIFX bulb on your network.

In the bar demo, we have a bulb with the label ``'Demo Bulb'``,
so we set <label> to match it accordingly.
