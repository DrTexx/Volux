from .broker import VoluxBrokerRequest

class RequestNewConnection:
    def __init__(self,connection):
        self.connection = connection
