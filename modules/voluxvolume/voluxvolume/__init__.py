from volux import VoluxModule
import cpmixer


class VoluxVolume(VoluxModule):
    def __init__(self, shared_modules=[], pollrate=100, *args, **kwargs):
        super().__init__(
            module_name="Volux Volume",
            module_attr="volume",
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
            shared_modules=shared_modules,
            pollrate=pollrate,
        )
        self.cpmixer = cpmixer.Mixer()

    def get(self):

        return self.cpmixer.gvol()

    def set(self, new_val):

        if new_val < 0:

            new_val = 0

        elif new_val > 100:

            new_val = 100

        self.cpmixer.svol(int(new_val))

    def setup(self):

        pass

    def cleanup(self):

        pass

    def toggle(self):

        new_state = not self.cpmixer.gmute()
        self.cpmixer.smute(new_state)
        return new_state
