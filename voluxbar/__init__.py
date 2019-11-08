from volux import VoluxModule
import tkinter as tk
from tkinter import ttk

class VoluxBar(VoluxModule):
    def __init__(self,shared_modules=[],pollrate=100,*args,**kwargs):
        super().__init__(
            module_name="Volux Bar",
            module_attr="bar",
            module_get=self.get,
            get_type=int,
            get_min=0,
            get_max=100,
            module_set=self.set,
            set_type=int,
            set_min=0,
            set_max=100,
            shared_modules=shared_modules,
            pollrate=pollrate
        )
        self.modes = {}
        self.mode = 'default'
        self.root = tk.Tk()
        self.mainApp = MainApplication(self.root,self,style='Bar.TFrame')

    def add_mode(self,name,module):
        self.modes.update({name: module})

    def remove_mode(self,name):
        self.modes.pop(name)

    def get(self):
        print("WIP!")

    def set(self, new_val):
        print("WIP!")

    def init_window(self):
        self.gui_style = ttk.Style()
        self.gui_style.configure('BarVal.TFrame', background="GREEN")
        self.gui_style.configure('Bar.TFrame', background="BLACK")

        self.mainApp.pack(side="top", fill=tk.BOTH)
        self.root.title("title")
        self.root.attributes("-topmost",True) # force window to stay on top (doesn't work in full screen applications)
        self.root.overrideredirect(1) # remove frame of window
        screen_size = (self.root.winfo_screenwidth(), self.root.winfo_screenheight())
        self.root.geometry("{}x{}+{}+{}".format(
            1920,
            8,
            0,
            1080-8
        )) # define the size of the window
        self.root.wait_visibility(self.root) # required for window transparency
        self.root.wm_attributes("-alpha",0.1) # make window transparent
        self.mainApp._update_loop()
        self.root.mainloop()


class MainApplication(ttk.Frame):
    def __init__(self,parent,VoluxBar_obj,*args,**kwargs):
        ttk.Frame.__init__(self,parent,*args,**kwargs)
        self.parent = parent
        self.VoluxBar_obj = VoluxBar_obj

        self.s_width = self.parent.winfo_screenwidth()

        self._bar = VolumeBar(self, style='Bar.TFrame')
        self._bar.pack(fill=tk.Y,side=tk.LEFT)

        self._init_bindings()

    def _update_loop(self):
        self.parent.lift() # ensure window on top of others
        self._refresh_bar()
        # print("refreshing...")
        self.after(self.VoluxBar_obj._pollrate,self._update_loop) # repeat _update_loop()

    def _refresh_bar(self):
        val = self.VoluxBar_obj.modes[self.VoluxBar_obj.mode].get()
        self._bar.barValue.config(width=self.s_width*(val/100))
        pass

    def _init_bindings(self):
        self.bind("<Enter>",self._mouse_entered)
        self.bind("<Leave>",self._mouse_left)
        self.parent.bind("<MouseWheel>",self._scroll_delta)
        self.parent.bind("<Button-2>",self._middle_click)
        self.parent.bind("<Button-4>",self._scroll_up)
        self.parent.bind("<Button-5>",self._scroll_down)
        self.parent.bind("<Button-3>",self._right_click)
        # self.parent.bind("<Control-Button-4>",self._brightness_up)
        # self.parent.bind("<Control-Button-5>",self._brightness_down)
        self.parent.bind("<Double-Button-3>",self._exit_app)

    def _mouse_entered(self, event):

        self.parent.wm_attributes("-alpha",0.8) # make window transparent

    def _mouse_left(self, event):

        self.parent.wm_attributes("-alpha",0.1) # make window transparent

    def _middle_click(self, event):

        active_module = self.VoluxBar_obj.modes[self.VoluxBar_obj.mode]

        if hasattr(active_module,'toggle'):
            new_state = active_module.toggle()
            if new_state == True:
                self.VoluxBar_obj.gui_style.configure('BarVal.TFrame', background="RED")
            elif new_state == False:
                self.VoluxBar_obj.gui_style.configure('BarVal.TFrame', background="GREEN")
        else:
            print("module '{}' has no toggle method!".format(active_module._module_name))

    def _scroll_delta(self, event):

        movement = event.delta/120

        if movement == 1:
            self._scroll_up(event)

        elif movement == -1:
            self._scroll_down(event)

        else:
            raise ValueError("movement should be 1 or -1")

    def _scroll_up(self, event):

        val = self.VoluxBar_obj.modes[self.VoluxBar_obj.mode].get()
        self.VoluxBar_obj.modes[self.VoluxBar_obj.mode].set(val+5)
        self._refresh_bar()

    def _scroll_down(self, event):

        val = self.VoluxBar_obj.modes[self.VoluxBar_obj.mode].get()
        self.VoluxBar_obj.modes[self.VoluxBar_obj.mode].set(val-5)
        self._refresh_bar()

    def _right_click(self, event):

        if self.VoluxBar_obj.mode == 'default':

            self.VoluxBar_obj.mode = 'light'
            self.VoluxBar_obj.gui_style.configure('BarVal.TFrame', background="BLUE")

        elif self.VoluxBar_obj.mode == 'light':

            self.VoluxBar_obj.mode = 'default'
            self.VoluxBar_obj.gui_style.configure('BarVal.TFrame', background="GREEN")

        else:

            raise Exception("mode not recognized!")

        self._refresh_bar()

    def _exit_app(self, event):

        exit()


class VolumeBar(ttk.Frame):
    def __init__(self,parent,*args,**kwargs):
        ttk.Frame.__init__(self,parent,*args,**kwargs)
        self.parent = parent

        self.barValue = ttk.Frame(self,width=1920*0.5,height=100,style="BarVal.TFrame")
        self.barValue.pack()
