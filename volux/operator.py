from .core import VoluxCore
from .module import VoluxModule


class VoluxOperator:
    def __init__(self):
        self.modules = []
        self.add_module(VoluxCore())

    def add_module(self, module):

        if self.validate_module(module):  # if the object passed is a valid module

            if not module in self.modules:

                self.modules.append(module)
                setattr(self, module._module_attr, module)
                module._loaded()  # call module's method for when it's finished being loaded

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

        for attrib in ["_module_name", "_module_attr", 'get', 'set']:

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
