class VoluxBroker:
    def __init__(self):
        pass

    def process_request(self,request):
        print("module UUID:",module.UUID)
        print("module request:",request_obj)


class VoluxBrokerRequest:
    def __init__(self,module,request):
        self.module = module
        self.request = request
