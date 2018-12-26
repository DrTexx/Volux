class MixerController:
    def __init__(self):
        import alsaaudio as al
        self.mixer = al.Mixer("Master")
    def svol(self,newvol):
        self.mixer.setvolume(newvol)
    def smute(self,newstate):
        if (newstate == 0) or (newstate == False):
            self.mixer.setmute(0)
        elif (newstate == 1) or (newstate == True):
            self.mixer.setmute(1)