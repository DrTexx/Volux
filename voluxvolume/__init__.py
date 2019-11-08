from volux import VoluxModule
import cpaudio


class VoluxVolume(VoluxModule):
    def __init__(self,shared_modules=[],pollrate=100,*args,**kwargs):
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
            shared_modules=shared_modules,
            pollrate=pollrate
        )
        self.mixer = cpaudio.MixerController()

    def get(self):

        return self.mixer.gvol()

    def set(self,new_val):

        if new_val < 0:

            new_val = 0

        elif new_val > 100:

            new_val = 100

        self.mixer.svol(new_val)

    def toggle(self):

        new_state = not self.mixer.gmute()
        self.mixer.smute(new_state)
        return new_state
