import pytest
from .context import volux

# create Volux Operator object (hub for communication between modules)
vlx = volux.VoluxOperator()
cli_module = volux.coremodules.VoluxCliPrint()
cli_UUID = None


class Test_operator:
    def test_add_module(self):
        global cli_UUID
        cli_UUID = vlx.add_module(cli_module)
        assert cli_UUID in vlx.modules

    def test_add_module_twice(self):
        with pytest.raises(Exception):
            vlx.add_module(cli_module)

    def test_add_bad_module(self):
        with pytest.raises(TypeError):
            vlx.add_module(vlx)

    def test_remove_module(self):
        assert cli_UUID in vlx.modules
        vlx.remove_module(cli_module)
        assert not (cli_UUID in vlx.modules)

    def test_remove_missing_module(self):
        with pytest.raises(AttributeError):
            vlx.remove_module(cli_module)
        vlx.add_module(cli_module)

    def test_validate_module(self):
        assert vlx.validate_module(vlx) is False
        assert vlx.validate_module(cli_module) is True

    def test_get_modules(self):
        assert vlx.get_modules() == vlx.modules

    def test_add_connection(self):
        vlx.add_connection(volux.VoluxConnection(vlx.cli, vlx.core, 30))

    def test_start_sync(self):
        vlx.start_sync()

    def test_stop_sync(self):
        vlx.stop_sync()


if __name__ == "__main__":
    test_op = Test_operator()
    test_op.test_add_module()
