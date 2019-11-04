import pytest
import volux
from voluxcliprint import VoluxCliPrint

# create Volux Operator object (hub for communication between modules)
vlx = volux.VoluxOperator()
cli_module   = VoluxCliPrint()

class Test_operator:
    def test_add_module(self):
        vlx.add_module(cli_module)
        assert cli_module in vlx.modules

    def test_add_bad_module(self):
        with pytest.raises(TypeError):
            vlx.add_module(vlx)

    def test_remove_module(self):
        vlx.remove_module(cli_module)
        assert not (cli_module in vlx.modules)

    def test_remove_missing_module(self):
        with pytest.raises(AttributeError):
            vlx.remove_module(cli_module)

    def test_validate_module(self):
        assert vlx.validate_module(vlx) == False

    def test_get_modules(self):
        print(vlx.get_modules())
        assert vlx.get_modules() == vlx.modules
