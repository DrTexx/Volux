import pytest
import volux

# create Volux Operator object (hub for communication between modules)
vlx = volux.VoluxOperator()


class VoluxTestModule(volux.VoluxModule):
    def __init__(self, shared_modules=[], *args, **kwargs):
        super().__init__(
            module_name="Volux Test Module",
            module_attr="test",
            module_get=self.get,
            get_type=int,
            get_min=0,
            get_max=100,
            module_set=self.set,
            set_type=int,
            set_min=0,
            set_max=100,
            shared_modules=shared_modules,
            pollrate=None,
        )
        self.val = 0

    def get(self):
        return self.val

    def set(self, new_val):
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

    def test_get_module_info(self):
        assert vlx.test.get_module_info() == {
            "name": "Volux Test Module",
            "attr": "test",
        }

    def test_bad_shared_modules(self):
        with pytest.raises(TypeError):
            vlx.add_module(VoluxTestModule(shared_modules={"key": "value"}))
        with pytest.raises(TypeError):
            vlx.add_module(VoluxTestModule(shared_modules=None))
        with pytest.raises(TypeError):
            vlx.add_module(VoluxTestModule(shared_modules="o hai mark"))
        with pytest.raises(TypeError):
            vlx.add_module(VoluxTestModule(shared_modules=24))
