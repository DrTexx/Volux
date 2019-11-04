import pytest
import volux
from voluxcliprint import VoluxCliPrint

# create Volux Operator object (hub for communication between modules)
vlx = volux.VoluxOperator()
cli_module = VoluxCliPrint()

class Test_operator:
    def test_add_module(self):
        vlx.add_module(cli_module)
        assert cli_module in vlx.modules

    def test_add_module_twice(self):
        with pytest.raises(Exception):
            vlx.add_module(cli_module)
            vlx.add_module(cli_module)

    def test_add_bad_module(self):
        with pytest.raises(TypeError):
            vlx.add_module(vlx)

    def test_remove_module(self):
        assert cli_module in vlx.modules
        vlx.remove_module(cli_module)
        assert not (cli_module in vlx.modules)

    def test_remove_missing_module(self):
        with pytest.raises(AttributeError):
            vlx.remove_module(cli_module)

    def test_validate_module(self):
        assert vlx.validate_module(vlx) == False
        assert vlx.validate_module(cli_module) == True

    def test_get_modules(self):
        assert vlx.get_modules() == vlx.modules
