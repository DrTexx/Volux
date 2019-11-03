import pytest
import volux

# create Volux Operator object (hub for communication between modules)
vlx = volux.VoluxOperator()

class VoluxTestModule(volux.VoluxModule):
    def __init__(self,*args,**kwargs):
        super().__init__(
            module_name="Volux Test Module",
            module_attr="test",
            module_get=self.get,
            module_set=self.set
        )
        self.val = 0

    def get(self):
        return self.val

    def set(self,new_val):
        self.val = new_val

class Test_VoluxTestModule:
    def test_add_module(self):
        vlx.add_module(VoluxTestModule())

    def test_get_modules(self):
        print(vlx.get_modules())
        assert vlx.get_modules() == vlx.modules

    def test_modules_set(self):
        vlx.test.set(20)
        assert vlx.test.get() == 20
