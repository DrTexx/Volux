import pytest
import volux
from voluxdemomodule import VoluxDemoModule

# create Volux Operator object (hub for communication between modules)
vlx = volux.VoluxOperator()
demo_module = VoluxDemoModule()

class Test_operator:
    def test_add_module(self):
        vlx.add_module(demo_module)
        assert demo_module in vlx.modules

    def test_get_modules(self):
        print(vlx.get_modules())
        assert vlx.get_modules() == vlx.modules
