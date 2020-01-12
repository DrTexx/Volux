"""Defines the operator class."""

from .core import VoluxCore
from .module import VoluxModule
from .broker import VoluxBroker
from .connection import VoluxConnection, NoDelta
from .request import VoluxBrokerRequest
from threading import Thread
import colorama
import logging
from typing import List, Callable, Dict, Union
from uuid import UUID

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
    """Class for managing the operation of the volux platform."""

    def __init__(self) -> None:
        """Instantiate a new operator."""
        self.modules: Dict[UUID, VoluxModule] = {}
        self.permissions: Dict[UUID, List[VoluxBrokerRequest]] = {}
        self.broker: VoluxBroker = VoluxBroker(self)
        self.add_module(VoluxCore())
        self.connections: Dict[UUID, VoluxConnection] = {}
        self.threads: List[Thread] = []
        self.running: bool = False

    def add_module(
        self,
        module: VoluxModule,
        req_permissions: List[VoluxBrokerRequest] = [],
        check_module_repeats: bool = True,
        overwrite_attributes: bool = False,
    ) -> UUID:
        """Load a module into the operator."""
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

    def remove_module(self, module: VoluxModule) -> None:
        """Unload a module from the operator."""
        if module in self.modules.values():

            del self.modules[module.UUID]
            delattr(self, module._module_attr)

        else:

            raise AttributeError(
                "module '{}' not loaded!".format(module._module_name)
            )

    def validate_module(self, module: VoluxModule) -> bool:
        """Check that a module satisfies all the conditions of a valid volux module."""
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

    def get_modules(self) -> Dict[UUID, VoluxModule]:
        """Return a dict of loaded modules."""
        return self.modules

    def add_connection(self, connection: Union[VoluxConnection, None]) -> None:
        """Add a new connection to operator. The connection's sync method will start being called once the operators start_sync method has been called."""
        if isinstance(connection, VoluxConnection):

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

    def remove_connection(
        self, connection: Union[VoluxConnection, None]
    ) -> None:
        """Remove a connection from the operator."""
        if isinstance(connection, VoluxConnection):
            if connection.UUID in self.connections:

                self.connections[connection.UUID]._stopped()
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

    def start_sync(self) -> None:
        """Begin syncing connections."""
        if len(self.connections) > 0:

            for cUUID in self.connections:

                connection = self.connections[cUUID]

                connection._started()

                wrapped_sync = self._wrap_sync(connection)

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

    def _wrap_sync(self, connection: VoluxConnection) -> Callable[[], None]:
        def wrapped_sync() -> None:

            try:

                while self.running is True:

                    log.debug("running {}".format(connection.nickname))
                    connection.sync()

            except Exception as err:

                log.error(
                    "A CONNECTION CRASHED! - {} ({})".format(
                        connection.nickname, err
                    )
                )
                self.running = False
                connection._stopped()

        return wrapped_sync

    def stop_sync(self) -> None:
        """Stop syncing connections."""
        self.running = False

        # for thread in self.threads:
        #     thread.join()

        self.threads = []

        for cUUID in self.connections:

            # run _stopped method on all connections
            self.connections[cUUID]._stopped()
            self.get_sync_deltas()

        log.info(
            "{}[CONNECTION SYNC STOPPED]{}".format(
                colorama.Fore.YELLOW, colorama.Style.RESET_ALL
            )
        )

    def get_sync_deltas(self) -> Dict[UUID, Union[int, NoDelta]]:
        """Return last stored delta for connections."""
        deltas = {}

        for cUUID in self.connections:

            connection = self.connections[cUUID]

            if self.running is True:

                deltas.update({connection.UUID: connection._get_delta()})

            elif self.running is False:

                deltas.update({connection.UUID: NoDelta()})

        return deltas

    def get_connection_nicknames(self) -> Dict[UUID, str]:
        """Return a dict of connection nicknames with connection UUID's as keys."""
        nicknames = {}

        for cUUID in self.connections:

            connection: VoluxConnection = self.connections[cUUID]

            nicknames.update({connection.UUID: connection.nickname})

        return nicknames
