"""A metamodule for inverting the value of an input based on the inputs min/max output"""

# site
import volux


class VoluxInvert(volux.VoluxModule):
    def __init__(self, min=0, max=100, *args, **kwargs):
        super().__init__(
            module_name="Volux Invert",
            module_attr="invert",
            module_get=self.get,
            get_type=int,
            get_min=min,
            get_max=max,
            module_set=self.set,
            set_type=int,
            set_min=min,
            set_max=max,
            module_setup=self.setup,
            module_cleanup=self.cleanup,
            shared_modules=[],
            pollrate=None,
        )
        self.val = 0

    def get(self):

        return self._set_max - self.val

    def set(self, new_val):

        self.val = new_val

    def setup(self):

        pass

    def cleanup(self):

        pass
