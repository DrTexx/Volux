import warnings
warnings.warn("WARNING: MODULE IS A WORK IN PROGRESS!!!")

class Display:

    def __init__(self):

        import subprocess
        self.subprocess = subprocess
        self.Popen = subprocess.Popen
        self.PIPE = subprocess.PIPE

        self.name = None
        self.brightness = None

    def _gDisplayName(self):

        display_name = self.subprocess.call(['xrandr | grep " connected"'], shell=True)
        print(display_name)
#         process = self.Popen(['xrandr | grep "connected"'], stdout=self.PIPE, stderr=self.PIPE, shell=True)
#         stdout, stderr = process.communicate()
#         print(stdout)

    def sbrightness(self,displayname,new_brightness):

        "xrandr --output {} --brightness {}".format(displayname,new_brightness) # NOTE: CONTROLS LITERAL BRIGHTNESS, NOT BACKLIGHT BRIGHTNESS!!!

    def gbrightness(self):

        pass
        # get the brightness
        # set the self.brightness value


disp = Display()
disp_name = disp._gDisplayName()
disp.sbrightness(disp_name,0.5)
