class VoluxBrokerRequest:
    def __init__(self,module):
        self.module = module

class RequestNewConnection(VoluxBrokerRequest):
    def __init__(self,module,connection,*args,**kwargs):
        super().__init__(
            module=module,
            *args,
            **kwargs
        )
        self.connection = connection
