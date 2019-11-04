########################
Writing your own modules
########################

.. warning:: This section is a work-in-progress

Example Module
==============

.. code-block:: python

    from volux import VoluxModule

    class DecoyVoluxModule(VoluxModule):
        def __init__(self, *args, **kwargs):
            super().__init__(
                module_name="Decoy Module",
                module_attr="decoy",
                module_get=self.get,
                module_set=self.set,
            )
            self.val = 0

        def get(self):

            return self.val

        def set(self, new_val):

            self.val = new_val

``module_name`` is the human-readable name for your volux module.

``module_attr`` is the attribute which will be added to the `VoluxOperator` object.

``module_get`` is the class method for getting the modules generic data

``module_set`` is the class method for setting the modules generic data
