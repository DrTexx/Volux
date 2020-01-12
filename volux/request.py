"""Define broker request base class."""

from typing import Any


class VoluxBrokerRequest:
    """Base class for request derivatives."""

    def __init__(self, module: Any, req_string: str) -> None:
        """Do not instansiate directly. Class should only ever be used as a parent class for derivatives."""
        self.module: Any = module
        self.req_string: str = req_string
        self.connection: Any = None
