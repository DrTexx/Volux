from .module import VoluxModule


class VoluxCore(VoluxModule):
    """provides a set of utilities for use in other modules"""

    def __init__(self, *args, **kwargs):
        super().__init__(
            module_name="Volux Core",
            module_attr="core",
            module_get=self.get,
            get_type=None,
            get_min=None,
            get_max=None,
            module_set=self.set,
            set_type=None,
            set_min=None,
            set_max=None,
            shared_modules=[],
            pollrate=None,
        )
        self.val = 0

    def get(self):

        return self.val

    def set(self, new_val):

        self.val = new_val

    def get_python_module_items(self, module):

        return [getattr(module, item_name) for item_name in dir(module)]

    def filter_by_attr_value(self, items, attribute, attribute_value):
        """returns only items which have [item].[attribute] == [attribute_value]"""

        valid_items = []

        for item in items:

            if hasattr(item, attribute):

                if getattr(item, attribute) == attribute_value:

                    valid_items.append(item)

        return valid_items

    def filter_by_superclass(self, items, superclass):
        """return all objects which have inherited a particular superclass"""

        return self.filter_by_attr_value(items, "superclass", superclass)

    def gen_demo_dict(self, demo_list):
        """turn a list for VoluxDemos into a dictionary of {[demo alias]: [demo]} pairs"""

        demo_dict = {demo._alias: demo for demo in demo_list}
        return demo_dict

    def get_demos(self):

        from volux import demos, VoluxDemo, VoluxCore

        demos_collected = []

        for attrib in dir(demos):

            demo = getattr(demos, attrib)

            if type(demo) is type:

                if issubclass(demo, VoluxDemo) is True:

                    demos_collected.append(demo)

        return demos_collected

    def get_demo_aliases(self):

        demos_collected = self.get_demos()
        demo_aliases = [demo()._alias for demo in demos_collected]
        return demo_aliases

    def get_demo_dict(self):

        return {demo()._alias: demo for demo in self.get_demos()}

    def get_script_names(self):

        from volux import scripts

        script_names = []
        for item_name in dir(scripts):
            if "script_" in item_name:
                script_names.append(item_name)
        return script_names
