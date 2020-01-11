class VoluxBrokerRequest:
    def __init__(self, module, req_string):
        self.module = module
        self.req_string: int = req_string
        self.connection = None


class AddConnection(VoluxBrokerRequest):
    def __init__(self, module, connection, *args, **kwargs):
        super().__init__(
            module=module, req_string="add a new connection", *args, **kwargs
        )
        self.connection = connection


class RemoveConnection(VoluxBrokerRequest):
    def __init__(self, module, connection, *args, **kwargs):
        super().__init__(
            module=module,
            req_string="remove an existing connection",
            *args,
            **kwargs
        )
        self.connection = connection


class GetConnections(VoluxBrokerRequest):
    def __init__(self, module, *args, **kwargs):
        super().__init__(
            module=module,
            req_string="see current connections",
            *args,
            **kwargs
        )


class StartSync(VoluxBrokerRequest):
    def __init__(self, module, *args, **kwargs):
        super().__init__(
            module=module,
            req_string="start connection syncing",
            *args,
            **kwargs
        )


class SyncState(VoluxBrokerRequest):
    def __init__(self, module, *args, **kwargs):
        super().__init__(
            module=module,
            req_string="get the connection sync state",
            *args,
            **kwargs
        )


class StopSync(VoluxBrokerRequest):
    def __init__(self, module, *args, **kwargs):
        super().__init__(
            module=module,
            req_string="stop connection syncing",
            *args,
            **kwargs
        )


class GetModules(VoluxBrokerRequest):
    def __init__(self, module, *args, **kwargs):
        super().__init__(
            module=module, req_string="get loaded modules", *args, **kwargs
        )


class GetSyncDeltas(VoluxBrokerRequest):
    def __init__(self, module, *args, **kwargs):
        super().__init__(
            module=module, req_string="get sync deltas", *args, **kwargs
        )


class GetConnectionNicknames(VoluxBrokerRequest):
    def __init__(self, module, *args, **kwargs):
        super().__init__(
            module=module,
            req_string="get connection nicknames",
            *args,
            **kwargs
        )
