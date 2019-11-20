from .requests import *


class VoluxBroker:
    def __init__(self, operator):
        self.operator = operator

    def process_request(self, request, verbose=True):

        if issubclass(type(request), VoluxBrokerRequest) == True:

            if verbose == True:

                print(
                    "request from {} is a valid subclass...".format(
                        request.module._module_name
                    )
                )

            mUUID = request.module.UUID

            if verbose == True:

                print("UUID of requesting module:", mUUID)

            if type(request) in request.module.req_permissions:

                if verbose == True:

                    print(
                        "{} claims it's allowed to {}".format(
                            request.module._module_name, request.req_string
                        )
                    )

                if type(request) in self.operator.permissions[mUUID]:

                    if verbose == True:

                        print("Operator verified module's permissions")

                    req_type = type(request)

                    if verbose == True:

                        print(
                            "{} is requesting to '{}'...".format(
                                request.module._module_name, request.req_string
                            )
                        )

                    if req_type == RequestAddConnection:

                        self.operator.add_connection(request.connection)

                    elif req_type == RequestRemoveConnection:

                        self.operator.remove_connection(request.connection)

                    elif req_type == RequestGetConnections:

                        return self.operator.connections

                    elif req_type == RequestStartSync:

                        self.operator.start_sync()

                    elif req_type == RequestSyncState:

                        return self.operator.running

                    elif req_type == RequestStopSync:

                        self.operator.stop_sync()

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
                        request.module._module_name, request.req_string, type(request)
                    )
                )

        else:

            raise TypeError("request must be a subclass of VoluxBrokerRequest")
