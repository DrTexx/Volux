"""Definition of various request classes to be sent by modules and handled by operators."""

from typing import Any

from .request import VoluxBrokerRequest


class AddConnection(VoluxBrokerRequest):
    """Request class for adding a new connection."""

    def __init__(
        self, module: Any, connection: Any, *args: Any, **kwargs: Any
    ):
        """Instansiate. Please see docstring for the class."""
        super().__init__(  # type: ignore
            module=module, req_string="add a new connection", *args, **kwargs
        )
        self.connection = connection


class RemoveConnection(VoluxBrokerRequest):
    """Request class for removing a connection."""

    def __init__(
        self, module: Any, connection: Any, *args: Any, **kwargs: Any
    ):
        """Instansiate. Please see docstring for the class."""
        super().__init__(  # type: ignore
            module=module,
            req_string="remove an existing connection",
            *args,
            **kwargs
        )
        self.connection = connection


class GetConnections(VoluxBrokerRequest):
    """Request class for returning a list of connections."""

    def __init__(self, module: Any, *args: Any, **kwargs: Any) -> None:
        """Instansiate. Please see docstring for the class."""
        super().__init__(  # type: ignore
            module=module,
            req_string="see current connections",
            *args,
            **kwargs
        )


class StartSync(VoluxBrokerRequest):
    """Request class for starting the sync operation on operator."""

    def __init__(self, module: Any, *args: Any, **kwargs: Any) -> None:
        """Instansiate. Please see docstring for the class."""
        super().__init__(  # type: ignore
            module=module,
            req_string="start connection syncing",
            *args,
            **kwargs
        )


class SyncState(VoluxBrokerRequest):
    """Request class for returning the operator's sync status."""

    def __init__(self, module: Any, *args: Any, **kwargs: Any) -> None:
        """Instansiate. Please see docstring for the class."""
        super().__init__(  # type: ignore
            module=module,
            req_string="get the connection sync state",
            *args,
            **kwargs
        )


class StopSync(VoluxBrokerRequest):
    """Request class for stopping the sync operation on operator."""

    def __init__(self, module: Any, *args: Any, **kwargs: Any) -> None:
        """Instansiate. Please see docstring for the class."""
        super().__init__(  # type: ignore
            module=module,
            req_string="stop connection syncing",
            *args,
            **kwargs
        )


class GetModules(VoluxBrokerRequest):
    """Request class for returning loaded modules from the operator."""

    def __init__(self, module: Any, *args: Any, **kwargs: Any) -> None:
        """Instansiate. Please see docstring for the class."""
        super().__init__(  # type: ignore
            module=module, req_string="get loaded modules", *args, **kwargs
        )


class GetSyncDeltas(VoluxBrokerRequest):
    """Request class for returning sync deltas from the operator."""

    def __init__(self, module: Any, *args: Any, **kwargs: Any) -> None:
        """Instansiate. Please see docstring for the class."""
        super().__init__(  # type: ignore
            module=module, req_string="get sync deltas", *args, **kwargs
        )


class GetConnectionNicknames(VoluxBrokerRequest):
    """Request class for return a dictionary of form {[connection_uuid]: [connection_nickname]}."""

    def __init__(self, module: Any, *args: Any, **kwargs: Any) -> None:
        """Instansiate. Please see docstring for the class."""
        super().__init__(  # type: ignore
            module=module,
            req_string="get connection nicknames",
            *args,
            **kwargs
        )
