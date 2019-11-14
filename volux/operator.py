from .core import VoluxCore
from .module import VoluxModule
from .broker import VoluxBroker

class VoluxOperator:
    def __init__(self):
        self.modules = {}
        self.broker = VoluxBroker()
        self.add_module(VoluxCore())

    def add_module(self, module, ):

        if self.validate_module(module):  # if the object passed is a valid module

            if not module in self.modules:

                setattr(module,'broker',self.broker)  # add broker to module
                self.modules.update({module.UUID: module})  # add module to operator
                setattr(self, module._module_attr, module)
                module._loaded()  # call module's method for when it's finished being loaded
                return module.UUID

            else:

                raise Exception("module '{}' is already loaded!".format(module._module_name))

        else:

            raise TypeError("module must be a subclass of VoluxModule")


    def remove_module(self, module):

        if module in self.modules:

            self.modules.remove(module)
            delattr(self, module._module_attr)

        else:

            raise AttributeError("module '{}' not loaded!".format(module._module_name))

    def validate_module(self, module):

        for attrib in ["_module_name", "_module_attr", 'get', 'set', 'UUID']:

            if not hasattr(module, attrib):

                print(
                    "module must be a subclass of VoluxModule with the [{}] attribute".format(
                        attrib
                    )
                )
                return False

        return True

    def get_modules(self):

        return self.modules

    def add_connection(self,connection):

        if connection.UUID in self.connections:
            print("CONNECTION ALREADY EXISTS!")

        else:
            self.connections.update({connection.UUID: connection})
