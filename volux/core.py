from .module import VoluxModule

class VoluxCore(VoluxModule):
    def __init__(self,*args,**kwargs):
        super().__init__(module_name="Volux Core",module_attr="core",module_get=None,module_set=None)
