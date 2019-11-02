from .core import VoluxCore
from .module import VoluxModule

class VoluxOperator:
    def __init__(self):
        self.add_module(VoluxCore())

    def add_module(self,module):

        if self.validate_module(module): # if the object passed is a valid module

            setattr(self,module._module_attr,module)
            module._loaded() # call modules method for when it's finished being loaded

        else:

            raise TypeError("module must be a subclass of VoluxModule")

    def validate_module(self,module):

        for attrib in ['_module_name','_module_attr']:

            if not hasattr(module, attrib):

                print("module must be a subclass of VoluxModule with the [{}] attribute".format(attrib))
                return False

        return True
