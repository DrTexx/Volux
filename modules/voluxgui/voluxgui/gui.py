# builtin
import colorsys

# external
import tkinter as tk
from tkinter import ttk

# site
import volux

# module
from .mainapplication import MainApplication
from .rgbtohex import rgb_to_hex


class VoluxGui(volux.VoluxModule):
    def __init__(self, shared_modules=[], pollrate=None, *args, **kwargs):
        super().__init__(
            module_name="Volux GUI",
            module_attr="gui",
            module_get=self.get,
            get_type=None,
            get_min=None,
            get_max=None,
            module_set=self.set,
            set_type=None,
            set_min=None,
            set_max=None,
            module_setup=self.setup,
            module_cleanup=self.cleanup,
            shared_modules=shared_modules,
            pollrate=pollrate,
            *args,
            **kwargs
        )

        self._shared_modules.append(self)

        # self.root = ThemedTk(theme="equilux")
        self.root = tk.Tk()
        self.mainApp = MainApplication(self.root, self, style="mainApp.TFrame")
        self.val = 0

    def get(self):

        return self.val

    def set(self, new_val):

        self.val = new_val
        container_width = (
            self.mainApp.value_bar.winfo_width()
        )  # note: wasteful, find alternative or remove in future

        r, g, b = colorsys.hsv_to_rgb(0, self.val / 100, self.val / 100)
        # print(r, g, b)
        # print(type(r), type(g), type(b))
        r, g, b = (int(r * 255), int(g * 255), int(b * 255))
        # print(r, g, b)
        # print(type(r), type(g), type(b))
        hex_color = rgb_to_hex(r, g, b)

        self.mainApp.value_bar_fill.configure(
            width=container_width * (self.val / 100),
            # width=container_width * (100),
            background=hex_color,
        )

    def setup(self):

        pass

    def cleanup(self):

        pass

    def init_window(self):

        self.binds = {
            "Start Sync": {
                "contexts": [self.mainApp.LFoutputs.testset_data],
                "command": self.mainApp.LFoutputs._set_test,
                "keycode": "<Return>",
            }
        }

        self.gui_style = ttk.Style()
        # self.gui_style.configure("TFrame", background="#19191B")
        # self.gui_style.configure("TPanedwindow", background="#19191B")
        # self.gui_style.configure("TLabelframe", background="#19191B")
        # self.gui_style.configure("TListbox", background="#19191B")
        # self.gui_style.configure("mainApp.TFrame", background="#19191B")
        # self.gui_style.configure("mainApp.TPanedwindow", background="GREY")
        self.gui_style.configure("value_bar.TFrame", background="BLACK")
        self.gui_style.configure("value_bar_fill.TFrame", background="RED")
        self.gui_style.configure("TEntry", fieldbackground="WHITE")
        self.gui_style.configure("Error.TEntry", fieldbackground="RED")
        # self.gui_style.theme_use('clam')

        self.mainApp.pack(side="top", fill=tk.X)
        self.root.title("Volux")
        screen_size = (
            self.root.winfo_screenwidth(),
            self.root.winfo_screenheight(),
        )
        window_size = (900, 500)
        self.root.geometry(
            "{}x{}+{}+{}".format(
                window_size[0],
                window_size[1],
                screen_size[0] - window_size[0],
                screen_size[1] - window_size[1],
            )
        )  # define the size of the window
        self.mainApp._update_loop()
        self.mainApp._create_bindings()
        self.root.mainloop()
