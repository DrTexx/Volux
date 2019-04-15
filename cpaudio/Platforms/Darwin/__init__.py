class MixerController:

    def __init__(self):

        from subprocess import call

        print("mixers:",alsaaudio.mixers())
        print("PCM:",alsaaudio.PCM().cardname())
        self.mixer = alsaaudio.Mixer("Master")

    def svol(self,newvol):
        if type(newvol) == int:
            
            if (newvol >= 0) and (newvol <= 100):
                try:
                    call(["osascript -e 'set volume output volume {}'".format(newvol)], shell=True)
                except:
                    raise Exception
            else:
                raise ValueError("volume must be between 0 and 100")
        else:
            raise TypeError("volume must be an integer")

    def gvol(self):

        return(call(["osascript -e 'set ovol to output volume of (get volume settings)'"], shell=True)) # return average across channels

    def smute(self,newstate):
        
        if type(newstate) == bool:
            
            if newstate == False:
                call(["osascript -e 'set volume with output muted'"], shell=True)
            elif newstate == True:
                call(["osascript -e 'set volume without output muted'"], shell=True)
            else:
                raise Exception("WHAT?")
        
        else:
            raise TypeError("Input must be boolean")

    def gmute(self):
        
        ismuted_string = call(["osascript -e 'output muted of (get volume settings)'"], shell=True)
        
        if ismuted_string == "true":
            return(True)
        elif ismuted_string == "false":
            return(False)
        else:
            raise Exception("ismuted_string didn't return 'true' or 'false', please raise a Github issue! <3")

############################

# set volume on mac
#call(["osascript -e 'set volume output volume {}'".format(volperc)], shell=True)

# get volume on mac
#call(["osascript -e 'set ovol to output volume of (get volume settings)'"], shell=True)
