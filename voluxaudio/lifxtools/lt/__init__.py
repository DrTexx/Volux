"""
lt module from lifxtools package
"""

print("lifxtools/lt/__init__.py")

# UI imports
import tkinter as tk  # for UI
from tkinter import ttk  # for not ugly UI

# Backend imports
import lifxtools  # for controlling lights

class LightShowTab(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        print(self._name,"PARENT =",self.parent)

        self.placeholder = ttk.Label(self, text="PLACEHOLDER")
        self.placeholder.pack()

        self.fade_slider = ttk.Scale(self, from_=0, to=1000)
        self.fade_slider.pack()

        self.minbrightness_slider = ttk.Scale(self, from_=1, to=100)
        self.minbrightness_slider.pack()

        # w = Scale(master, from_=0, to=200, orient=tk.HORIZONTAL)
        # w.pack()


class Navbar(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        print(self._name,"PARENT =",self.parent)


        self.notebook = ttk.Notebook(self.parent)

        self.page_lightcontrol = ttk.Frame(self.notebook)
        self.page_scenemanager = ttk.Frame(self.notebook)
        self.page_lightshow = LightShowTab(self.notebook)

        self.devices_found = tk.Listbox(self.page_lightcontrol, selectmode=tk.EXTENDED)
        self.devices_found.pack()

        print("devices",self.parent.mlifx.devices) # print found devices to console

        for index, mdevice in enumerate(self.parent.mlifx.managed_devices, 0): # add each found device to the GUI list
            self.devices_found.insert(index, mdevice.label)

        print_selected_device = ttk.Button(self.page_lightcontrol, text="print selected devices index to console", command=self._print_selected_devices)
        print_selected_device.pack()

        toggle_device_power = ttk.Button(self.page_lightcontrol, text="toggle device power", command=self._toggle_device_power)
        toggle_device_power.pack()

        set_to_default = ttk.Button(self.page_lightcontrol, text="set to default", command=self._set_to_default)
        set_to_default.pack()

        set_to_bedtime = ttk.Button(self.page_lightcontrol, text="set to bedtime", command=self._set_to_bedtime)
        set_to_bedtime.pack()

        set_to_theatre = ttk.Button(self.page_lightcontrol, text="set to theatre", command=self._set_to_theatre)
        set_to_theatre.pack()

        save_state = ttk.Button(self.page_lightcontrol, text="save state", command=self._save_state)
        save_state.pack()

        load_state = ttk.Button(self.page_lightcontrol, text="load state", command=self._load_state)
        load_state.pack()



        self.notebook.add(self.page_lightcontrol, text="Light Control")
        self.notebook.add(self.page_scenemanager, text="Scene Manager")
        self.notebook.add(self.page_lightshow, text="Light Show")

        self.notebook.pack(expand=1, fill="both")

    def _print_selected_devices(self):
        print(self.devices_found.curselection()) # return a tuple of indexes for selected items

    def _get_selected_mdevices(self):
        device_indexes = self.devices_found.curselection()
        devices_to_return = [self.parent.mlifx.managed_devices[device_i] for device_i in device_indexes]
        return devices_to_return # return a tuple of indexes for selected items

    def _toggle_device_power(self):
        mdevices = self._get_selected_mdevices()
        print("toggling power of mdevices:",mdevices)
        for mdevice in mdevices:
            mdevice.device.set_power(not mdevice.device.get_power())

    def _set_to_default(self):
        mdevices = self._get_selected_mdevices()
        print("setting mdevices to default:",mdevices)
        for mdevice in mdevices:
            mdevice.device.set_color(lifxtools.default_color)

    def _set_to_bedtime(self):
        mdevices = self._get_selected_mdevices()
        print("setting mdevices to bedtime:",mdevices)
        for mdevice in mdevices:
            mdevice.device.set_color(lifxtools.bedtime_color)

    def _set_to_theatre(self):
        mdevices = self._get_selected_mdevices()
        print("setting mdevices to theatre:",mdevices)
        for mdevice in mdevices:
            mdevice.device.set_color(lifxtools.theatre_color)

    def _save_state(self):
        mdevices = self._get_selected_mdevices()
        print("saving state of mdevices:",mdevices)
        for mdevice in mdevices:
            mdevice.ssave()

    def _load_state(self): # todo: implement the fact you can't load a state that was never saved!
        mdevices = self._get_selected_mdevices()
        print("loading state of mdevices:",mdevices)
        for mdevice in mdevices:
            mdevice.sload()


class DeviceFrameRep(ttk.Frame):
    def __init__(self,mdevice_obj,parent,*args,**kwargs):
        ttk.Frame.__init__(self,parent,*args,**kwargs)
        self.parent = parent

        self.mdevice = mdevice_obj

        self.placeholder = ttk.Label(self,text="DEVICE PREVIEW PLACEHOLDER")
        self.placeholder.pack()

        self.canvas = tk.Canvas(self, width=100, height=100)
        self.canvas.pack()
        self.canvas_rectangle = self.canvas.create_rectangle(0, 0, 100, 100, fill="#40E0D0")

    def refresh(self):
        print(type(self.mdevice))
        print(type(self.mdevice.device))
        color = self.mdevice.device.get_color()
        if (type(color) == tuple):
            h, s, v, k = color
            r, g, b = lifxtools.hsv2rgb(h, s, v)
            hex = "#%02x%02x%02x" % (r, g, b) # todo: fix this please god damn it Denver you fool
            self.canvas.itemconfig(self.canvas_rectangle,fill=hex)
        else:
            print("self.device.color must be a tuple!")


class MainApplication(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        print(self._name,"PARENT =",self.parent)

        # <create the rest of your GUI here>
        self._init_mlifx()
        self._init_GUI()
        print("finished preparing program!")

    def _init_mlifx(self):

        print("_init_mlifx...")
        self.mlifx = lifxtools.ManagedLifx(lifxtools.return_interface(None))
        self.mlifx.add_device(lifxtools.VirtualDevice())
        print(self.mlifx.devices)

    def _init_GUI(self):

        print("_init_GUI...")
        self.navbar = Navbar(self)
        self.navbar.pack(side="left", fill="y")
        self.device_test = DeviceFrameRep(self.mlifx.managed_devices[0],self) # create a frame for the first device
        self.device_test.pack()

    def _update_loop(self, ms_per_loop=1000):
        # self.device_test.refresh()
        # if live_data == True:
        #     pass
        # self._update_brightness()
        self.after(ms_per_loop, self._update_loop)  # repeat _update_loop()

    def _exit_app(self, event):
        exit()


if __name__ == "lifxtools.lt":

    root = tk.Tk()
    mainApp = MainApplication(root)
    mainApp.pack(side="top", fill="both", expand=True)
    mainApp._update_loop()  # must be before main loop
    root.mainloop()

    # lifx = return_interface(num_lights)
    # devices = lifx.get_lights()
    # list_devices(devices)
    # blink_devices(devices)
