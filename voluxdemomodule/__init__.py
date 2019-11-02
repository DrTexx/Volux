from volux import VoluxModule

class VoluxDemoModule(VoluxModule):
    def __init__(self,min_val=0,max_val=100,*args,**kwargs):
        super().__init__(
            module_name="Volux Demo Module",
            module_attr="demo",
            module_get=self.get,
            module_set=self.set
        )
        self.demo_val = 0
        self.min_val = min_val
        self.max_val = max_val

    def get(self):
        return self.demo_val

    def set(self, new_val):

        clamped_to = None

        if (new_val < self.min_val):
            self.demo_val = self.min_val
            clamped_to = "min"

        elif (new_val > self.max_val):
            self.demo_val = self.max_val
            clamped_to = "max"

        else:
            self.demo_val = new_val

        print("demo_val: {} (clamped by [{}])".format(self.demo_val,clamped_to))
