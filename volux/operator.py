from .core import VoluxCore
from .module import VoluxModule
from .broker import VoluxBroker
from .connection import VoluxConnection
from threading import Thread
import colorama
import logging

colorama.init()

log = logging.getLogger("volux operator")
log.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler("volux_operator.log")
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter and add it to the handlers
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
log.addHandler(fh)
log.addHandler(ch)


class VoluxOperator:
    def __init__(self):
        self.modules = {}
        self.permissions = {}
        self.broker = VoluxBroker(self)
        self.add_module(VoluxCore())
        self.connections = {}
        self.threads = []
        self.running = False

    def add_module(
        self,
        module,
        req_permissions=[],
        check_module_repeats=True,
        overwrite_attributes=False,
    ):

        if self.validate_module(
            module
        ):  # if the object passed is a valid module

            if check_module_repeats is True:

                loaded_module_types = [type(m) for m in self.modules.values()]
                if (
                    type(module) in loaded_module_types
                ):  # if this type of module is already in operator's modules

                    log.warning(
                        "{}a different instance of the module '{}' is already loaded{}".format(
                            colorama.Fore.YELLOW,
                            module._module_name,
                            colorama.Style.RESET_ALL,
                        )
                    )

            if module.UUID in self.modules.keys():

                raise Exception(
                    "this instance of module '{}' is already loaded! [{}{}{}]".format(
                        module._module_name,
                        colorama.Fore.GREEN,
                        module.UUID,
                        colorama.Style.RESET_ALL,
                    )
                )

            else:

                setattr(module, "broker", self.broker)  # add broker to module
                setattr(
                    module, "req_permissions", req_permissions
                )  # add broker to module
                self.modules.update(
                    {module.UUID: module}
                )  # add module to operator
                self.permissions.update({module.UUID: req_permissions})

                if module._module_attr in dir(
                    self
                ):  # if attrbute already present
                    attribute_warning_string = "{}Warning: attribute '{}' is already being used by operator{}".format(
                        colorama.Fore.YELLOW,
                        module._module_name,
                        colorama.Style.RESET_ALL,
                    )
                    if overwrite_attributes is False:
                        log.warning(attribute_warning_string + ", skipping...")
                    elif overwrite_attributes is True:
                        log.warning(
                            attribute_warning_string + ", overwriting..."
                        )
                        setattr(self, module._module_attr, module)
                else:
                    setattr(self, module._module_attr, module)

                module._loaded()  # call module's method for when it's finished being loaded
                log.info(
                    "module added: {name} [{color}{UUID}{reset}]".format(
                        name=module._module_name,
                        color=colorama.Fore.GREEN,
                        UUID=module.UUID,
                        reset=colorama.Style.RESET_ALL,
                    )
                )
                return module.UUID

        else:

            raise TypeError("module must be a subclass of VoluxModule")

    def remove_module(self, module):

        if module in self.modules.values():

            del self.modules[module.UUID]
            delattr(self, module._module_attr)

        else:

            raise AttributeError(
                "module '{}' not loaded!".format(module._module_name)
            )

    def validate_module(self, module):

        for attrib in ["_module_name", "_module_attr", "get", "set", "UUID"]:

            if not hasattr(module, attrib):

                log.error(
                    "module must be a subclass of VoluxModule with the [{}] attribute".format(
                        attrib
                    )
                )
                return False

        log.debug(
            "module passed validation - {} [{}]".format(
                module._module_name, module.UUID
            )
        )
        return True

    def get_modules(self):

        return self.modules

    def add_connection(self, connection):

        if type(connection) == VoluxConnection:

            if connection.UUID in self.connections:
                log.warning("connection already exists!")

            else:
                self.connections.update({connection.UUID: connection})
                log.info(
                    "connection added: {name} [{color}{UUID}{reset}]".format(
                        name=connection.nickname,
                        color=colorama.Fore.CYAN,
                        UUID=connection.UUID,
                        reset=colorama.Style.RESET_ALL,
                    )
                )

        else:

            raise TypeError(
                "connection must be an instance of VoluxConnection"
            )

    def remove_connection(self, connection):

        if connection.UUID in self.connections:

            del self.connections[connection.UUID]
            log.info(
                "connection removed: {name} [{color}{UUID}{reset}]".format(
                    name=connection.nickname,
                    color=colorama.Fore.CYAN,
                    UUID=connection.UUID,
                    reset=colorama.Style.RESET_ALL,
                )
            )

        else:

            raise ValueError(
                "Can not remove connection: UUID is not in connections ({})".format(
                    connection.UUID
                )
            )

    def start_sync(self):

        if len(self.connections) > 0:

            for cUUID in self.connections:

                connection = self.connections[cUUID]

                wrapped_sync = self._wrap_sync(connection.sync)

                self.threads.append(Thread(target=wrapped_sync))

            self.running = True

            for thread in self.threads:
                thread.start()

            log.info(
                "{}[CONNECTION SYNC STARTED]{}".format(
                    colorama.Fore.YELLOW, colorama.Style.RESET_ALL
                )
            )

        else:

            log.error(
                "{}volux operator has no connections to start sync on!{}".format(
                    colorama.Fore.RED, colorama.Style.RESET_ALL
                )
            )
            self.stop_sync

    def _wrap_sync(self, sync_method):
        def wrapped_sync():

            while self.running is True:

                sync_method()

        return wrapped_sync

    def stop_sync(self):

        self.running = False

        # for thread in self.threads:
        #     thread.join()

        self.threads = []

        log.info(
            "{}[CONNECTION SYNC STOPPED]{}".format(
                colorama.Fore.YELLOW, colorama.Style.RESET_ALL
            )
        )
