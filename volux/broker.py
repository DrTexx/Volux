"""Defines the broker class."""

# builtin
import logging
from typing import Any, Union, Dict
from uuid import UUID

# module
from .connection import VoluxConnection, NoDelta
from .request import VoluxBrokerRequest
from . import requests as voluxrequests

log = logging.getLogger("volux broker")
log.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter and add it to the handlers
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
ch.setFormatter(formatter)
# add the handlers to the logger
log.addHandler(ch)


class VoluxBroker:
    """Mediates interaction between volux operator and modules."""

    def __init__(self, operator: Any) -> None:
        """Instansiate a new broker instance."""
        self.operator: Any = operator

    def process_request(
        self, request: VoluxBrokerRequest, verbose: bool = True
    ) -> Any:
        """Evaluate a request object and execute it's associated action if all requirements are satisfied."""
        if issubclass(type(request), VoluxBrokerRequest) is True:

            mUUID: UUID = request.module.UUID

            log.debug(
                "request from {} is a valid subclass...".format(
                    request.module._module_name
                )
            )
            log.debug("UUID of requesting module: {}".format(mUUID))

            if type(request) in request.module.req_permissions:

                log.debug(
                    "{} claims it's allowed to {}".format(
                        request.module._module_name, request.req_string
                    )
                )

                if type(request) in self.operator.permissions[mUUID]:

                    log.debug("Operator verified module's permissions")

                    req_type: type = type(request)

                    log.debug(
                        "{} is requesting to '{}'...".format(
                            request.module._module_name, request.req_string
                        )
                    )

                    if req_type == voluxrequests.AddConnection:

                        self.operator.add_connection(request.connection)

                    elif req_type == voluxrequests.RemoveConnection:

                        self.operator.remove_connection(request.connection)

                    elif req_type == voluxrequests.GetConnections:

                        return self.operator.connections

                    elif req_type == voluxrequests.StartSync:

                        self.operator.start_sync()

                    elif req_type == voluxrequests.SyncState:

                        return self.operator.running

                    elif req_type == voluxrequests.StopSync:

                        self.operator.stop_sync()

                    elif req_type == voluxrequests.GetSyncDeltas:

                        return self.operator.get_sync_deltas()

                    elif req_type == voluxrequests.GetConnectionNicknames:

                        return self.operator.get_connection_nicknames()

                    else:

                        raise TypeError(
                            "volux broker recieved an invalid request type: {}".format(
                                type(request)
                            )
                        )

                else:

                    raise PermissionError(
                        "operator could not verify module '{}' had valid permissions".format(
                            request.module._module_name
                        )
                    )

            else:

                raise PermissionError(
                    "module {} doesn't claim it's allowed to {} ({})".format(
                        request.module._module_name,
                        request.req_string,
                        type(request),
                    )
                )

        else:

            raise TypeError("request must be a subclass of VoluxBrokerRequest")

        return None
