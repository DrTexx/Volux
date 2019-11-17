from .requests import *
from .connection import VoluxConnection

class VoluxBroker:
    def __init__(self,operator):
        self.operator = operator

    def process_request(self,request):

        mUUID = request.module.UUID

        print("UUID of requesting module:",mUUID)

        if type(request) in request.module.req_permissions:

            print("module states it has permissions")

            if type(request) in self.operator.permissions[mUUID]:

                print("operator verified module's permissions")

                req_type = type(request)

                print("{} is requesting to '{}'...".format(request.module._module_name,request.req_string))

                if req_type == RequestNewConnection:

                    if type(request.connection) == VoluxConnection:

                        self.operator.add_connection(request.connection)

                elif req_type == RequestGetConnections:

                    return self.operator.connections

                elif req_type == RequestStartSync:

                    self.operator.start_sync()

                elif req_type == RequestSyncState:

                    return self.operator.running

                elif req_type == RequestStopSync:

                    self.operator.stop_sync()

                else:

                    raise TypeError("volux broker recieved an invalid request type: {}".format(type(request)))

            else:

                raise PermissionError("operator could not verify module '{}' had valid permissions".format(request.module._module_name))

        else:

            raise PermissionError("module '{}' doesn't claim to have valid permissions".format(request.module._module_name))


        # elif type(request) == RequestGetConnections:
        #
        #     print("{} is requesting to see current connections...".format(request.module._module_name))
        #
        #     if type(request) in request.module.req_permissions:
        #
        #         print("{} has permission to see connections".format(request.module._module_name))
        #
        #         return self.operator.connections
        #
        #     else:
        #
        #         print("{} request permissions: {}".format(request.module._module_name,request.module.req_permissions))
        #         raise PermissionError("{} is not allowed to add new connections".format(request.module._module_name))
        #
        # elif type(request) == RequestStartSync:
        #
        #     print("{} is requesting to start sync...".format(request.module._module_name))
        #
        #     if type(request) in request.module.req_permissions:
        #
        #         print("{} has permission to start sync".format(request.module._module_name))
        #
        #         self.operator.start_sync()
        #
        #     else:
        #
        #         print("{} request permissions: {}".format(request.module._module_name,request.module.req_permissions))
        #         raise PermissionError("{} is not allowed to start sync".format(request.module._module_name))
        #
        # elif type(request) == RequestSyncState:
        #
        #     print("{} is requesting to get sync state...".format(request.module._module_name))
        #
        #     if type(request) in request.module.req_permissions:
        #
        #         print("{} has permission to get sync state.".format(request.module._module_name))
        #
        #         return self.operator.running
        #
        #     else:
        #
        #         print("{} request permissions: {}".format(request.module._module_name,request.module.req_permissions))
        #         raise PermissionError("{} is not allowed to get sync state".format(request.module._module_name))
