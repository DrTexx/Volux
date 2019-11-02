from volux import VoluxModule
import cpaudio


class VoluxVolume(VoluxModule):
    def __init__(self,*args,**kwargs):
        super().__init__(module_name="Volux Volume",module_attr="volume", module_get=self.get, module_set=self.set)
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
