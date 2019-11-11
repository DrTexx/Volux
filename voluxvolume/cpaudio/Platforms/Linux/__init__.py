class MixerController:

    def __init__(self):

        import alsaaudio
        try:
            # print("mixers:",alsaaudio.mixers())
            # print("PCM:",alsaaudio.PCM().cardname())
            self.mixer = alsaaudio.Mixer("Master")
        except FileNotFoundError:
            print("I see you're running on a CI server -.-")

    def svol(self,newvol):
        if type(newvol) == int:

            if (newvol >= 0) and (newvol <= 100):
                try:
                    self.mixer.setvolume(newvol)
                except:
                    raise Exception
            else:
                raise ValueError("volume must be between 0 and 100")
        else:
            raise TypeError("volume must be an integer")

    def gvol(self):

        _gvol = self.mixer.getvolume()
        return(int(sum(_gvol) / len(_gvol))) # return average across channels

    def smute(self,newstate):

        if type(newstate) == bool:

            if newstate == False:
                self.mixer.setmute(0)
            elif newstate == True:
                self.mixer.setmute(1)
            else:
                raise Exception("WHAT?")

        else:
            raise TypeError("Input must be boolean")

    def gmute(self):

        _gmute = self.mixer.getmute()
        mute_average = int(sum(_gmute) / len(_gmute))

        if mute_average == 0:
            return(False)
        elif mute_average == 1:
            return(True)

        else:
            raise Exception("mute_average didn't return 0 or 1, please create an issue on Github!")
