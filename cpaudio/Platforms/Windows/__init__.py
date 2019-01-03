class MixerController:
    def __init__(self):

        from ctypes import cast, POINTER
        from comtypes import CLSCTX_ALL
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

        self.volume = cast(interface, POINTER(IAudioEndpointVolume))
        _vol_range = self.volume.GetVolumeRange()
        self._vol_min = _vol_range[0]
        self._increment = abs(_vol_range[0])/100

    def svol(self,newvol):

        if type(newvol) == int:

            if (newvol >= 0) and (newvol <= 100):

                try:
                    _steps = 100 - newvol
                    newmaster = 0 -(self._increment*_steps)
                    self.volume.SetMasterVolumeLevel(newmaster, None)

                except:
                    raise Exception

            else:
                raise ValueError("volume must be between 0 and 100")
        else:
            raise TypeError("volume must be an integer")

    def gvol(self):

        # get abs min
        _abs_min = abs(self._vol_min)
        # get abs current value
        _abs_val = self.volume.GetMasterVolumeLevel()
        # divide current by abs min
        inverse_percent = _abs_val / _abs_min
        # multiply product by 100 for scaled percentage
        _gvol = 100-(abs(inverse_percent)*100)
        return(round(_gvol))

    def smute(self,newstate):

        if type(newstate) == bool:
             
            if newstate == False:
                self.volume.SetMute(0, None)
            elif newstate == True:
                self.volume.SetMute(1, None)
            else:
                raise Exception("WHAT?")

        else:
            raise TypeError("Input must be boolean")

    def gmute(self):

        _gmute = self.volume.GetMute()
         
        if _gmute == 0:
            return(False)
        elif _gmute == 1:
            return(True)
         
        else:
            raise Exception("Mute didn't return 0 or 1, please create an issue on Github!")
