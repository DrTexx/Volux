#!/usr/bin/env python

from gi.repository import Gtk
import subprocess

class BrightnessScale:
    def __init__(self):
        # get active monitor and current brightness
        self.monitor = self.getActiveMonitor()
        self.currB = self.getCurrentBrightness()

    def initUI(self):
        # initliaze and configure window 
        window = Gtk.Window()
        window.set_title('Brightness Scale')
        window.set_default_size(250, 50)
        window.set_position(Gtk.WindowPosition.CENTER)
        window.set_border_width(10)

        # slider configuration
        self.adjustment = Gtk.Adjustment(self.currB, 0, 100, 1, 10, 0)
        self.scale = Gtk.HScale()
        self.scale.set_adjustment(self.adjustment)
        self.scale.set_digits(0)

        # close Gtk thread on closing window
        window.connect("destroy", lambda w: Gtk.main_quit())

        # setup event handler on value-changed
        self.scale.connect("value-changed", self.scale_moved)

        # add the scale to window
        window.add(self.scale)

        # show all components in window
        window.show_all()

        # close window on pressing escape key
        accGroup = Gtk.AccelGroup()
        key, modifier = Gtk.accelerator_parse('Escape')
        accGroup.connect(key, modifier, Gtk.AccelFlags.VISIBLE, Gtk.main_quit)
        window.add_accel_group(accGroup)

    def showErrDialog(self):
        self.errDialog = Gtk.MessageDialog(None, 
                                           Gtk.DialogFlags.MODAL,
                                           Gtk.MessageType.ERROR,
                                           Gtk.ButtonsType.OK,
                                           "Unable to detect active monitor, run 'xrandr --verbose' on command-line for more info")
        self.errDialog.set_title("brightness control error")
        self.errDialog.run()
        self.errDialog.destroy()

    def initStatus(self):
        if(self.monitor == "" or self.currB == ""):
            return False
        return True

    def getActiveMonitor(self):
        #Find display monitor
        monitor = subprocess.check_output("xrandr -q | grep ' connected' | cut -d ' ' -f1", shell=True)
        print(monitor)
        if(monitor != ""):
            monitor = monitor.split('\n')[0]
        return monitor

    def getCurrentBrightness(self):
        #Find current brightness
        currB = subprocess.check_output("xrandr --verbose | grep -i brightness | cut -f2 -d ' '", shell=True)
        if(currB != ""):
            currB = currB.split('\n')[0]
            currB = int(float(currB) * 100)
        else:
            currB = ""
        return currB

    def scale_moved(self, event):
        #Change brightness
        newBrightness = float(self.scale.get_value())/100
        cmd = "xrandr --output %s --brightness %.2f" % (self.monitor, newBrightness)
        cmdStatus = subprocess.check_output(cmd, shell=True)

if __name__ == "__main__":
    # new instance of BrightnessScale
    brcontrol = BrightnessScale()
    if(brcontrol.initStatus()):
        # if everything ok, invoke UI and start Gtk thread loop
        brcontrol.initUI()
        Gtk.main()
    else:
        # show error dialog
        brcontrol.showErrDialog()