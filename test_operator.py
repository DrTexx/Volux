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

    def test_add_bad_module(self):
        with pytest.raises(TypeError):
            vlx.add_module(vlx)

    def test_remove_module(self):
        vlx.remove_module(demo_module)
        assert not (demo_module in vlx.modules)

    def test_remove_missing_module(self):
        with pytest.raises(AttributeError):
            vlx.remove_module(demo_module)

    def test_validate_module(self):
        assert vlx.validate_module(vlx) == False

    def test_get_modules(self):
        print(vlx.get_modules())
        assert vlx.get_modules() == vlx.modules
