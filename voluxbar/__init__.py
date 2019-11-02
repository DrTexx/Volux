from volux import VoluxModule

class VoluxBar(VoluxModule):
    def __init__(self,*args,**kwargs):
        super().__init__(module_name="Volux Bar",module_attr="bar", module_get=self.get, module_set=self.set)
        self.modes = {}

    def add_mode(self,name,module):
        self.modes.update({name: module})

    def remove_mode(self,name):
        self.modes.pop(name)

    def get(self):
        print("WIP!")

    def set(self, new_val):
        print("WIP!")
