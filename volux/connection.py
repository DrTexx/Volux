import uuid

class VoluxConnection:
    """Contains all the properties of a connection between two modules"""

    def __init__(self, input_module, output_module):

        self.input = input_module
        self.output = output_module
        self.UUID = uuid.uuid4()

    def sync(self):

        self.output.set(
            self.input.get()
        )
