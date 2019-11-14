import uuid
from time import sleep

class VoluxConnection:
    """Contains all the properties of a connection between two modules"""

    def __init__(self, input_module, output_module, hz):

        self.input = input_module
        self.output = output_module
        self.UUID = uuid.uuid4()
        self.hz = hz

    def sync(self):

        print("{} -> {}".format(self.input._module_name,self.output._module_name))

        self.output.set(
            self.input.get()
        )

        sleep(1/self.hz)
