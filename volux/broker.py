from .requests import *
from .connection import VoluxConnection

class VoluxBroker:
    def __init__(self,operator):
        self.operator = operator

    def process_request(self,request):

        print("UUID of requesting module:",request.module.UUID)

        if type(request) == RequestNewConnection:

            print("{} is requesting a new connection...".format(request.module._module_name))

            if type(request) in request.module.req_permissions:

                print("{} has permission to add new connections...".format(request.module._module_name))

                if type(request.connection) == VoluxConnection:

                    print("connection request is valid...")
                    self.operator.add_connection(request.connection)

                else:

                    raise TypeError("requests connection must be of type VoluxConnection")


            else:

                print("{} request permissions: {}".format(request.module._module_name,request.module.req_permissions))
                raise PermissionError("{} is not allowed to add new connections".format(request.module._module_name))

        elif type(request) == RequestGetConnections:

            print("{} is requesting to see current connections...".format(request.module._module_name))

            if type(request) in request.module.req_permissions:

                print("{} has permission to see connections".format(request.module._module_name))

                return self.operator.connections

            else:

                print("{} request permissions: {}".format(request.module._module_name,request.module.req_permissions))
                raise PermissionError("{} is not allowed to add new connections".format(request.module._module_name))

        else:

            raise TypeError("volux broker recieved an invalid request type: {}".format(type(request)))
