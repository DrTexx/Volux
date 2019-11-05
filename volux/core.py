from .module import VoluxModule

class VoluxCore(VoluxModule):
    """provides a set of utilities for use in other modules"""
    def __init__(self,*args,**kwargs):
        super().__init__(module_name="Volux Core",module_attr="core",module_get=None,module_set=None)

    def get_python_module_items(self,module):

        return [getattr(module,item_name) for item_name in dir(module)]

    def filter_by_attr_value(self,items,attribute,attribute_value):
        """returns only items which have [item].[attribute] == [attribute_value]"""

        valid_items = []

        for item in items:

            if hasattr(item,attribute):

                if getattr(item,attribute) == attribute_value:

                    valid_items.append(item)

        return(valid_items)

    def filter_by_superclass(self,items,superclass):
        """return all objects which have inherited a particular superclass"""

        return self.filter_by_attr_value(items, 'superclass', superclass)

    def gen_demo_dict(self,demo_list):
        """turn a list for VoluxDemos into a dictionary of {[demo alias]: [demo]} pairs"""

        demo_dict = {demo._alias: demo for demo in demo_list}
        return demo_dict
