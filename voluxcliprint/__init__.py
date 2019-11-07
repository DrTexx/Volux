from volux import VoluxModule


class VoluxCliPrint(VoluxModule):
    def __init__(self, min_val=0, max_val=100, *args, **kwargs):
        super().__init__(
            module_name="Volux CLI Print",
            module_attr="cli",
            module_get=self.get,
            module_set=self.set,
            shared_modules=[]
        )
        self.demo_val = 0
        self.min_val = min_val
        self.max_val = max_val

    def get(self):

        return self.demo_val

    def set(self, new_val):

        self.demo_val = new_val

        print("demo_val: {}".format(self.demo_val))
