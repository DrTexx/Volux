import pytest
import volux

# create Volux Operator object (hub for communication between modules)
vlx = volux.VoluxOperator()
module_items = []
demos_collected = []

class Test_operator:
    def test_correct_type(self):

        assert type(vlx.core) == volux.VoluxCore

    def test_get_python_modules(self):

        from volux import demos
        global module_items
        module_items = vlx.core.get_python_module_items(demos)

    def test_filter_by_superclass(self):

        global demos_collected
        demos_collected = vlx.core.filter_by_superclass(demos_collected,volux.VoluxDemo)

    def test_gen_demo_dict(self):

        global demo_dict
        global demos_collected
        demo_dict = vlx.core.gen_demo_dict(demos_collected)
