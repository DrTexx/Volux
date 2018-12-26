class MixerController:

    def __init__(self):

        import alsaaudio
#        self.mixer = alsaaudio.Mixer("Master")
        self.mixer = alsaaudio.Mixer()

    def svol(self,newvol):
        if (newvol >= 0) and (newvol <= 100):
            try:
                self.mixer.setvolume(newvol)
            except:
                raise Exception
        else:
            raise ValueError("volume must be between 0 and 100")

    def gvol(self):
        
        _gvol = self.mixer.getvolume()
        return(int(sum(_gvol) / len(_gvol))) # return average across channels

    def smute(self,newstate):
        
        if (newstate == 0) or (newstate == False):
            self.mixer.setmute(0)
        
        elif (newstate == 1) or (newstate == True):
            self.mixer.setmute(1)
        
        else:
            raise TypeError("Input must be either True, False, 0 or 1")

    def gmute(self):
        
        _gmute = self.mixer.getmute()
        return(int(sum(_gmute) / len(_gmute)))
