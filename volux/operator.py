from .core import VoluxCore
from .module import VoluxModule
from .broker import VoluxBroker
from threading import Thread

class VoluxOperator:
    def __init__(self):
        self.modules = {}
        self.broker = VoluxBroker(self)
        self.add_module(VoluxCore())
        self.connections = {}
        self.threads = []
        self.running = False

    def add_module(self, module, req_permissions=[]):

        if self.validate_module(module):  # if the object passed is a valid module

            if not module in self.modules:

                setattr(module,'broker',self.broker)  # add broker to module
                setattr(module,'req_permissions',req_permissions)  # add broker to module
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
            print("CONNECTION ADDED: UUID={}".format(connection.UUID))

    def start_sync(self):

        if len(self.connections) > 0:

            for cUUID in self.connections:

                connection = self.connections[cUUID]

                wrapped_sync = self._wrap_sync(connection.sync)

                self.threads.append(
                    Thread(target=wrapped_sync)
                )

            self.running = True

            for thread in self.threads:
                thread.start()

        else:

            raise Exception("volux operator has no connections to start sync on!")

    def _wrap_sync(self,sync_method):

        def wrapped_sync():

            while self.running == True:

                sync_method()

        return wrapped_sync
