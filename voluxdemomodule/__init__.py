from volux import VoluxModule

class VoluxDemoModule(VoluxModule):
    def __init__(self,*args,**kwargs):
        super().__init__(
            module_name="Volux Demo Module",
            module_attr="demo",
            module_get=self.get,
            module_set=self.set
        )
        self.demo_val = None

    def get(self):
        return self.demo_val

    def set(self, new_val):
        self.demo_val = new_val
