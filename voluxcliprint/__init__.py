from volux import VoluxModule


class VoluxCliPrint(VoluxModule):
    def __init__(self, *args, **kwargs):
        super().__init__(
            module_name="Volux CLI Print",
            module_attr="cli",
            module_get=self.get,
            get_type=int,
            get_min=0,
            get_max=100,
            module_set=self.set,
            set_type=int,
            set_min=0,
            set_max=100,
            shared_modules=[],
            pollrate=None
        )
        self.cli_val = 0

    def get(self):

        return self.cli_val

    def set(self, new_val):

        self.cli_val = new_val
        print("VoluxCliPrint new value: {}".format(self.cli_val))
