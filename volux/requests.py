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

class RequestGetConnections(VoluxBrokerRequest):
    def __init__(self,module,*args,**kwargs):
        super().__init__(
            module=module,
            *args,
            **kwargs
        )

class RequestStartSync(VoluxBrokerRequest):
    def __init__(self,module,*args,**kwargs):
        super().__init__(
            module=module,
            *args,
            **kwargs
        )

class RequestSyncState(VoluxBrokerRequest):
    def __init__(self,module,*args,**kwargs):
        super().__init__(
            module=module,
            *args,
            **kwargs
        )
