class VoluxModule:
    """Provides common metadata for every Volux module. All modules (including core) are a subclass of VoluxModule"""

    def __init__(self, module_name, module_attr):
        self._module_name = module_name
        self._module_attr = module_attr

    def _loaded(self):
        print("loaded module: {}".format(self._module_name))

    def get_module_info(self):
        print("module_name =", self._module_name)
