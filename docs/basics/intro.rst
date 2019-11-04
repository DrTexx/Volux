###############
Getting Started
###############

************
Installation
************

Installing with pip
===================

.. prompt:: bash $

    pip install volux


Congratulations, you've just installed Volux!

.. note:: If you would rather build the module yourself, see "Installing from source"

Next, let's try running the 'bar' demo.


*************
Running demos
*************

Bar demo
========

Once volux is finished installing, you can run the bar demo like so:

.. prompt:: bash $

    volux --demo bar

You should now see a transparent bar at the bottom of your screen.

Bar demo explained
------------------

In different modes, performing identical actions on the bar produce different results.

Below, you'll see a table of representing the result of performing
certain actions on the bar in a given mode.

=========  ==================  ================
Bar Color  Action              Result
=========  ==================  ================
Any        Right-click         Change bar mode

           Double right-click  Exit demo

Green      Scroll up           Increase volume

           Scroll down         Decrease volume

           Middle-click        Mute

Red        Scroll up           Increase volume

           Scroll down         Decrease volume

           Middle-click        Unmute

Blue       Scroll up           Increase bulb brightness

           Scroll down         Decrease bulb brightness

           Middle-click        Toggle bulb power
=========  ==================  ================
