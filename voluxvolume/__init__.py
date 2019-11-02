from volux import VoluxModule
import cpaudio


class VoluxVolume(VoluxModule):
    def __init__(self,*args,**kwargs):
        super().__init__(module_name="Volux Volume",module_attr="volume", module_get=self.get, module_set=self.set)
        self.mixer = cpaudio.MixerController()

    def get(self):

        return self.mixer.gvol()

    def set(self,new_val):

        self.mixer.svol(new_val)
