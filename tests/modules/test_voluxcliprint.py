import pytest
import volux

# create Volux Operator object (hub for communication between modules)
vlx = volux.VoluxOperator()
volux_module_cli_print = volux.modules.VoluxCliPrint()


class Test_voluxcliprint:
    def test_adding_module(self):
        cli_UUID = vlx.add_module(volux_module_cli_print)
        assert cli_UUID in vlx.modules
        assert isinstance(vlx.modules[cli_UUID], volux.VoluxModule)

    def test_get_modules(self):
        print(vlx.get_modules())
        assert vlx.get_modules() == vlx.modules

    def test_default_value(self):

        assert vlx.cli.cli_val == vlx.cli.get()

    def test_set_value(self):
        vlx.cli.set(20)
        assert vlx.cli.get() == 20
        vlx.cli.set(10)
        assert vlx.cli.get() == 10
