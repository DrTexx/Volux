class VoluxModule:
    """Provides common metadata for every Volux module. All modules (including core) are a subclass of VoluxModule"""

    def __init__(self, module_name, module_attr, module_get, module_set):
        self._module_name = module_name
        self._module_attr = module_attr
        self.get = module_get
        self.set = module_set

    def _loaded(self):
        print("loaded module: {}".format(self._module_name))

    def get_module_info(self):
        return {
            'name': self._module_name,
            'attr': self._module_attr
        }
