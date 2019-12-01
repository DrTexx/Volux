""" allows a user to used a cached version of an input to feed multiple outputs """

# site
import volux


class VoluxCache(volux.VoluxModule):
    def __init__(self, *args, **kwargs):
        super().__init__(
            module_name="Volux Cache",
            module_attr="cache",
            module_get=self.get,
            get_type=int,
            get_min=0,
            get_max=100,
            module_set=self.set,
            set_type=int,
            set_min=0,
            set_max=100,
            module_setup=self.setup,
            module_cleanup=self.cleanup,
            shared_modules=[],
            pollrate=None,
        )
        self.cache_val = 0

    def get(self):

        return self.cache_val

    def set(self, new_val):

        self.cache_val = new_val

    def setup(self):

        pass

    def cleanup(self):

        pass
