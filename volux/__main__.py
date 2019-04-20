#TODO: fix volume bar not visually going to zero
#TODO: replace zero volume with mute if supported under Debian
#TODO: add animation options (e.g. slide in, fade in, etc.)
#TODO: add numbers to the bar
#TODO: add support for Mac
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

# BUILTIN MODULES
import json
from tkinter import * # for UI
from tkinter.ttk import * # for not ugly UI
import sys # for processing CLI arguments
from os.path import realpath # for loading files (e.g. icons)

# SITE PACKAGES #
#from plyer import notification

# LOCAL MODULES
#import volux.temperatures as temps
from volux.dp_datatools import LivePercentage, clamp
from volux.VolumeAssistant import VolumeAssistant
from volux.VolumeBar import VolumeBar
from volux.barStyle import add_bar_styles, barstyles
import cpaudio
mixer = cpaudio.MixerController()



### ---- PREFERENCES ---- ###
program_icon = realpath('icon.png')
with open("preferences.json") as f:
    preferences = json.load(f)


### ---- SETUP STUFF ---- ###
VolAs = VolumeAssistant() # initialise a Volume Assistant object
VolBar = VolumeBar()
#coreWatch = temps.CoreWatch(temps.get_cores()) # start watching cores for temperature issues

### DEFINE STATES
class VolumeMode:

    def __init__(self): pass

    def enter(self):
        VolBar.mode = VolBar.modes['volume']
        mixer.smute(False)

    def vacate(self):
        VolBar.mode = VolBar.modes['unknown']

class MuteMode:

    def __init__(self): pass

    def enter(self):
        VolBar.mode = VolBar.modes['muted']
        mixer.smute(True)

    def vacate(self):
        VolBar.mode = VolBar.modes['unknown']

class BrightnessMode:

    def __init__(self): pass

    def enter(self):
        VolBar.mode = VolBar.modes['brightness']

    def vacate(self):
        VolBar.mode = VolBar.modes['unknown']

        if mixer.gmute() == True:
            return(MuteMode)

        elif mixer.gmute() == False:
            return(VolumeMode)

        else: raise TypeError("_ismuted should be a bool value")

### IMPORT AND INITIALSE STATE MANAGER
from volux.StateManager import StateManager
sm = StateManager(VolumeMode)



### ---- TKINTER STUFF BEGINS ---- ###

root = Tk()

class Window(Frame):

    def __init__(self,master=None):

        Frame.__init__(self,master)
        self.master = master
        self._init_objects()
        self._init_styles()
        self._init_window()
        self._init_bindings()
        #self._open_message()

    def _init_objects(self):

        self.displaySize = VolAs._get_display_size(root) # max size of the bar in pixels

        self.barWidth = LivePercentage(0,self.displaySize['x']) # set width of bar

    def _init_styles(self):

        print("INIT STYLES!")
        self.style = Style()
        self.style.configure("barContainer.TFrame", background="BLACK")
        add_bar_styles(self.style, barstyles)

        print("FINISHED ADDING STYLES!")

    def _init_window(self):
        m = self.master
        m.title("Please submit an issue to Github if you see this!")

        self.barContainer = Frame(m, style="barContainer.TFrame")

        self.barContainer.pack(fill=BOTH,expand=1)

        self.barHeight = preferences["bar_height"] # define height of bar

        self.bar = Frame(self.barContainer) # create the bar

        self._update_bar() # update bar values

        def _key_pressed(event): print("key pressed",event.key)
        
        def _key_released(event): print("key released",event.key)
        

        def _brightness_mode_off():
            
            sm.state_change(sm.state.vacate())
            self.barMode = self.barModes['default']
            self._update_bar()
            print("brightness mode off!")
            
        self.bar.pack(fill=Y,ipadx=5,ipady=5,side=LEFT)

    def _adjust_bar(self, event, movement):
        if type(movement) == int: # if movement is an integer
            #self.barMode = self.barModes['volume']
            notchMultiplier = 5 # impact of a single scroll notch on percentage
            newVol = mixer.gvol() + movement*notchMultiplier
            mixer.svol(newVol)
            VolAs.volume = clamp(newVol,0,100)
        
        else: raise TypeError("Value should be an integer! Not sure what happened!")
        
        self._update_bar() # update the bar's graphical appearance
        self._update_volume() # update the system volume
        #TODO: support for Mac scrolling

    def _brightness_up(self): print("WIP:"+"UP")
    
    def _brightness_down(self): print("WIP:"+"DOWN")
    
    def _right_click(self, event):

        if sm.state == BrightnessMode:
            sm.change_state(sm.state().vacate())

        else:
            sm.change_state(BrightnessMode)
        
        self._update_bar()
        #print("brightness mode!")

    def _scroll_up(self, event):
        
        if sm.state == VolumeMode:
            self._adjust_bar(event,+1)

        elif sm.state == BrightnessMode:
            self._brightness_up()

        elif sm.state == MuteMode:
            sm.change_state(VolumeMode)

        self._update_bar()
        
    def _scroll_down(self, event):

        if sm.state == VolumeMode:
            self._adjust_bar(event,-1)

        elif sm.state == BrightnessMode:
            self._brightness_down()

        elif sm.state == MuteMode:
            sm.change_state(VolumeMode)

        self._update_bar()

    def _middle_click(self, event):

        if sm.state == VolumeMode: # if unmuted
            sm.change_state(MuteMode) # change to muted
            self._update_bar()

        elif sm.state == MuteMode: # if unmuted
            sm.change_state(VolumeMode) # change to muted

        self._update_bar()

    def _scroll_delta(self, event):

        movement = event.delta/120

        if movement == 1:
            self._scroll_up(event)

        elif movement == -1:
            self._scroll_down(event)

        else:
            raise ValueError("movement should be 1 or -1")
        
    def _init_bindings(self):
        self.barContainer.bind("<Enter>",self._mouse_entered)
        self.barContainer.bind("<Leave>",self._mouse_left)
        self.master.bind("<MouseWheel>",self._scroll_delta)
        self.master.bind("<Button-2>",self._middle_click)
        self.master.bind("<Button-4>",self._scroll_up)
        self.master.bind("<Button-5>",self._scroll_down)
        self.master.bind("<Button-3>",self._right_click)
        self.master.bind("<Control-Button-4>",self._brightness_up)
        self.master.bind("<Control-Button-5>",self._brightness_down)
        self.master.bind("<Double-Button-3>",self._exit_app)

    def _update_loop(self,ms_per_loop=1000):
        root.lift() # ensure window on top of others
        self._update_bar() # update bar graphics
        self.after(ms_per_loop,self._update_loop) # repeat _update_loop()

    def _update_bar(self):

        self._update_volume()

        mode_style_id = VolBar.mode.style_id # set background based on mode color

        print(mode_style_id)

        self.barWidth.setPerc(VolAs.volume) # set the width as a percentage

        newWidth = self.barWidth.getNum() # get a numerical version of the percentage

        self.bar.configure(style=mode_style_id, width=str(newWidth)) # update the bar with these settings
        

    def _update_volume(self): mixer.svol(VolAs.volume)

    def _toggle_mute(self): mixer.smute(not mixer.gmute()) # toggle mute state

    def _mouse_entered(self,event): root.wm_attributes("-alpha",preferences["default_opacity"])
    def _mouse_left(self,event): root.wm_attributes("-alpha",preferences["outside_zone_opacity"])
    def _open_message(self):
        notification.notify(
            title=program_title,
            message="{} launched!".format(program_title),
            app_name=program_title,
            app_icon=program_icon,
            timeout=5)

    def _exit_app(self,event):
#         notification.notify(
#             title=program_title,
#             message="{} now closing...".format(program_title),
#             app_name=program_title,
#             app_icon=program_icon,
#             timeout=10)
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
root.wm_attributes("-alpha",preferences["outside_zone_opacity"]) # make window transparent
root.title(preferences["program_title"])

print("sys.argv[0]:")
print(sys.argv[0])
if '__main__.py' in sys.argv[0]:
    app._update_loop() # must be before main loop
    root.mainloop()
