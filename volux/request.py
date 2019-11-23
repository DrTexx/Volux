class VoluxBrokerRequest:
    def __init__(self, module, req_string):
        self.module = module
        self.req_string = req_string


class RequestAddConnection(VoluxBrokerRequest):
    def __init__(self, module, connection, *args, **kwargs):
        super().__init__(
            module=module, req_string="add a new connection", *args, **kwargs
        )
        self.connection = connection


class RequestRemoveConnection(VoluxBrokerRequest):
    def __init__(self, module, connection, *args, **kwargs):
        super().__init__(
            module=module,
            req_string="remove an existing connection",
            *args,
            **kwargs
        )
        self.connection = connection


class RequestGetConnections(VoluxBrokerRequest):
    def __init__(self, module, *args, **kwargs):
        super().__init__(
            module=module,
            req_string="see current connections",
            *args,
            **kwargs
        )


class RequestStartSync(VoluxBrokerRequest):
    def __init__(self, module, *args, **kwargs):
        super().__init__(
            module=module,
            req_string="start connection syncing",
            *args,
            **kwargs
        )


class RequestSyncState(VoluxBrokerRequest):
    def __init__(self, module, *args, **kwargs):
        super().__init__(
            module=module,
            req_string="get the connection sync state",
            *args,
            **kwargs
        )


class RequestStopSync(VoluxBrokerRequest):
    def __init__(self, module, *args, **kwargs):
        super().__init__(
            module=module,
            req_string="stop connection syncing",
            *args,
            **kwargs
        )


class RequestGetModules(VoluxBrokerRequest):
    def __init__(self, module, *args, **kwargs):
        super().__init__(
            module=module, req_string="get loaded modules", *args, **kwargs
        )
