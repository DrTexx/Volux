import pytest
import volux

# create Volux Operator object (hub for communication between modules)
vlx = volux.VoluxOperator()
module_items = []
demos_collected = []


class DecoyClass:
    def __init__(self):
        self.superclass = "this string is certainly not a class"


class Test_operator:
    def test_correct_type(self):

        assert type(vlx.core) == volux.VoluxCore

    def test_get_python_modules(self):

        from volux import demos

        global module_items
        module_items = vlx.core.get_python_module_items(demos)
        # print("MODULE ITEMS",module_items)
        raw_module_items = [
            getattr(demos, item_name) for item_name in dir(demos)
        ]
        for module_item in module_items:
            assert module_item in raw_module_items

    def test_filter_by_superclass(self):

        global module_items
        module_items.append(DecoyClass())
        global demos_collected
        demos_collected = vlx.core.filter_by_superclass(
            module_items, volux.VoluxDemo
        )

        for demo_x in demos_collected:
            assert demo_x.superclass == volux.VoluxDemo

    def test_gen_demo_dict(self):

        global demo_dict
        global demos_collected
        demo_dict = vlx.core.gen_demo_dict(demos_collected)

        for demo_name in demo_dict:
            assert demo_dict[demo_name].superclass == volux.VoluxDemo

    def test_get_demos(self):

        for demo_x in vlx.core.get_demos():
            assert issubclass(demo_x, volux.VoluxDemo) is True

    def test_get_demo_aliases(self):

        raw_demo_aliases = [d()._alias for d in vlx.core.get_demos()]
        for demo_alias in vlx.core.get_demo_aliases():
            assert demo_alias in raw_demo_aliases

    def test_get_demo_dict(self):

        dict = vlx.core.get_demo_dict()
        all_demo_names = vlx.core.get_demo_aliases()
        all_demos = vlx.core.get_demos()

        for key in dict:
            assert key in all_demo_names
            assert dict[key] in all_demos

    def test_get_script_names(self):

        script_names = vlx.core.get_script_names()
        dir_of_scripts = dir(volux.scripts)

        for script_name in script_names:
            assert script_name in dir_of_scripts
            assert "script_" in script_name
