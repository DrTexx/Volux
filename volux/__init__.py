#TODO: fix volume bar not going to zero
#TODO: replace zero volume with mute if supported under Debian
#TODO: add animation options (e.g. slide in, fade in, etc.)
#TODO: add numbers to the bar
#TODO: add support for Windows/Mac (e.g. scroll support)
#TODO: allow bar to be attached to different sides
#TODO: allow customization of bar thickness
#TODO: make bar opacity adapt to darkness/brightness of background
#TODO: modifier key makes scroll change channel pan instead

# DEPENDENCIES:
# (all working with most recent versions as of 04/12/2018)
# sudo apt install python3-tk
# sudo apt install python3-dbus # maybe?
# sudo apt install libasound2-dev
# pip3 install pyalsaaudio --user
# pip3 install plyer --user
# pip3 install psutil --user

# BUILTIN MODULES #
import time # used for delays
import math
from _thread import start_new_thread # used to run functions in parallel
import tkinter as Tk
from subprocess import call
from os.path import realpath
# SITE PACKAGES #
from plyer import notification
import alsaaudio as al
# LOCAL MODULES
import volux.temperatures as temps
from volux.dp_datatools import LivePercentage, clamp
from volux.VolumeAssistant import VolumeAssistant
from volux.VolumeBar import VolumeBar
### ---- PREFERENCES ---- ###
program_title = "volux"
program_icon = realpath('icon.png')
sound_device = "Master"
default_mixer_name = "Master"
default_opacity = 0.5
outside_zone_opacity = 0.1
bar_height = 5
### ---- SETUP STUFF ---- ###
VolAs = VolumeAssistant() # initialise a Volume Assistant object
VolBar = VolumeBar()
coreWatch = temps.CoreWatch(temps.get_cores()) # start watching cores for temperature issues

### DEFINE STATES
class VolumeMode:
    def __init__(self):pass
    def enter(self):
        VolBar.mode = VolBar.modes['volume']
        VolAs.mixer.setmute(0)
    def vacate(self):
        VolBar.mode = VolBar.modes['unknown']
class MuteMode:
    def __init__(self): pass
    def enter(self):
        VolBar.mode = VolBar.modes['muted']
        VolAs.mixer.setmute(1)
    def vacate(self):
        VolBar.mode = VolBar.modes['unknown']
class BrightnessMode:
    def __init__(self): pass
    def enter(self):
        VolBar.mode = VolBar.modes['brightness']
    def vacate(self):
        VolBar.mode = VolBar.modes['unknown']
        if VolAs.ismuted() == True:
            return(MuteMode)
        elif VolAs.ismuted() == False:
            return(VolumeMode)
        else: raise TypeError("_ismuted should be a bool value")
### DEFINE STATE MANAGER
class StateManager:
    def __init__(self,initial_state):
        self.state = initial_state
    def change_state(self,new_state): # request to change states
        self.state().vacate()
        new_state().enter()
        self.state = new_state
### CREATE A STATE MANAGER
sm = StateManager(VolumeMode)

### ---- TKINTER STUFF BEGINS ---- ###
root = Tk.Tk()
class Window(Tk.Frame):
    def __init__(self,master=None):
        Tk.Frame.__init__(self,master)
        self.master = master
        self._init_objects()
        self._init_window()
        self._open_message()
    def _init_objects(self):
        self.displaySize = VolAs._get_display_size(root) # max size of the percentage bar in pixels
        self.barWidth = LivePercentage(0,self.displaySize['x']) # set width of bar
    def _init_window(self):
        m = self.master
        m.title("Please submit an issue to Github if you see this!")
        self.barHeight = bar_height # set height of bar            self._update_bar()
        barContainer = Tk.Frame(m)
        barContainer.configure(background="BLACK")
        barContainer.pack(fill=Tk.BOTH,expand=1)
        self.bar = Tk.Frame(barContainer) # create the bar
        self._update_bar() # update bar values
        def _adjust_bar(event,movement):
            if type(movement) == int: # if movement is an integer
                #self.barMode = self.barModes['volume']
                notchMultiplier = 5 # impact of a single scroll notch on percentage
                newVol = VolAs.volume + movement*notchMultiplier
                VolAs.volume = clamp(newVol,0,100)
            else: raise TypeError("Value should be an integer! Not sure what happened!")
            self._update_bar() # update the bar's graphical appearance
            self._update_volume() # update the system volume
            #TODO: support for Windows/Mac scrolling
        def _scroll_up(event):
            if sm.state == VolumeMode:
                _adjust_bar(event,+1)
            elif sm.state == BrightnessMode:
                _brightness_up()
            elif sm.state == MuteMode:
                sm.change_state(VolumeMode)
            self._update_bar()
        def _scroll_down(event):
            if sm.state == VolumeMode:
                _adjust_bar(event,-1)
            elif sm.state == BrightnessMode:
                _brightness_down()
            elif sm.state == MuteMode:
                sm.change_state(VolumeMode)
            self._update_bar()
        def _middle_click(event):
            if sm.state == VolumeMode: # if unmuted
                sm.change_state(MuteMode) # change to muted
                self._update_bar()
            elif sm.state == MuteMode: # if unmuted
                sm.change_state(VolumeMode) # change to muted
            self._update_bar()
        def _key_pressed(event):
            print("key pressed",event.key)
        def _key_released(event):
            print("key released",event.key)
        def _brightness_up(): print("WIP:"+"UP")
        def _brightness_down(): print("WIP:"+"DOWN")
        def _right_click(event):
            if sm.state == BrightnessMode:
                sm.change_state(sm.state().vacate())
            else:
                sm.change_state(BrightnessMode)
            self._update_bar()
            #print("brightness mode!")
        def _brightness_mode_off():
            sm.state_change(sm.state.vacate())
            self.barMode = self.barModes['default']
            self._update_bar()
            print("brightness mode off!")
        self.bar.pack(fill=Tk.Y,ipadx=5,ipady=5,side=Tk.LEFT)
        m.bind("<MouseWheel>",_adjust_bar)
        m.bind("<Button-2>",_middle_click)
        m.bind("<Button-4>",_scroll_up)
        m.bind("<Button-5>",_scroll_down)
        m.bind("<Button-3>",_right_click)
        m.bind("<Control-Button-4>",_brightness_up)
        m.bind("<Control-Button-5>",_brightness_down)
        m.bind("<Double-Button-3>",self._exit_app)
        barContainer.bind("<Enter>",self._mouse_entered)
        barContainer.bind("<Leave>",self._mouse_left)
    def _update_loop(self,ms_per_loop=1000):
        root.lift() # ensure window on top of others
        self._update_bar() # update bar graphics
        self.after(ms_per_loop,self._update_loop) # repeat _update_loop()
    def _update_bar(self):
        modeColor = VolBar.mode.color # set background based on mode color
        self.barWidth.setPerc(VolAs.volume) # set the width as a percentage
        newWidth = self.barWidth.getNum() # get a numerical version of the percentage
        self.bar.configure(background=modeColor,width=str(newWidth)) # update the bar with these settings
    def _update_volume(self):
        try: self.mixer.setvolume(VolAs.volume)
        except: call(["amixer","sset",str(VolAs.device),str(VolAs.volume)+"%","-q"])
    def _update_mute(self):
        muted = self.mixer.getmute()
        if muted[0] == True: self.mixer.setmute(0)
        elif muted[0] == False: self.mixer.setmute(1)
        else: raise Exception("mixer's .getmute()[0] method should return True or False!")
    def _mouse_entered(self,event): root.wm_attributes("-alpha",default_opacity)
    def _mouse_left(self,event): root.wm_attributes("-alpha",outside_zone_opacity)
    def _open_message(self):
        notification.notify(
            title=program_title,
            message="{} launched!".format(program_title),
            app_name=program_title,
            app_icon=program_icon,
            timeout=5)
    def _exit_app(self,event):
        notification.notify(
            title=program_title,
            message="{} now closing...".format(program_title),
            app_name=program_title,
            app_icon=program_icon,
            timeout=10)
        exit()
        
app = Window(root)
dispSize = VolAs._get_display_size(root)
overlay_w = dispSize['x']
overlay_h = app.barHeight
windowOffsets = {'x': 0,
                 'y': dispSize['y']-app.barHeight}
root.geometry("{}x{}+{}+{}".format(overlay_w,overlay_h,
                                   windowOffsets['x'],windowOffsets['y'])) # define the size of the window
root.attributes("-topmost",True) # force window to stay on top (doesn't work in full screen applications)
root.overrideredirect(1) # remove frame of window
root.wait_visibility(root) # required for window transparency
root.wm_attributes("-alpha",outside_zone_opacity) # make window transparent
root.title(program_title)
app._update_loop() # must be before main loop
root.mainloop()
