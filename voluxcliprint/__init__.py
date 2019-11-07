from volux import VoluxModule


class VoluxCliPrint(VoluxModule):
    def __init__(self, *args, **kwargs):
        super().__init__(
            module_name="Volux CLI Print",
            module_attr="cli",
            module_get=self.get,
            module_set=self.set,
            shared_modules=[],
            pollrate=None
        )
        self.cli_val = 0

    def get(self):

        return self.cli_val

    def set(self, new_val):

        self.cli_val = new_val
        print("VoluxCliPrint new value: {}".format(self.cli_val))
