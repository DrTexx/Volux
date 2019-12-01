# builtin
import logging
import time
import threading

# external
import tkinter as tk
from tkinter import ttk

# site
import volux

# module
from .inputsframe import InputsFrame
from .outputsframe import OutputsFrame
from .connectionsframe import ConnectionsFrame
from .infoframe import InfoFrame

log = logging.getLogger("voluxgui module - mainapplication (frame)")
log.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter and add it to the handlers
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)d"
)
ch.setFormatter(formatter)
# add the handlers to the logger
log.addHandler(ch)


class MainApplication(ttk.Frame):
    def __init__(self, parent, module_root, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.module_root = module_root
        self.vis_on = tk.BooleanVar()

        log.debug(
            "shared modules: {}".format(self.module_root._shared_modules)
        )

        self.value_bar = ttk.Frame(
            self.parent,
            height=14,
            width=100,
            pad="1px",
            style="value_bar.TFrame",
        )
        self.value_bar.pack(side="top", fill=tk.X)

        self.value_bar_fill = tk.Frame(
            self.value_bar, height=14, width=0, background="RED"
        )
        self.value_bar_fill.pack(fill=tk.Y)

        self.p = ttk.Panedwindow(
            self, orient=tk.HORIZONTAL, style="mainApp.TPanedwindow"
        )
        self.p.pack(fill=tk.X, padx="5px", pady="5px")

        self.Finputs = ttk.Frame(self)
        self.LFinputs = InputsFrame(self.Finputs, self.module_root)
        self.LFinputs.pack(anchor="nw")

        self.Foutputs = ttk.Frame(self)
        self.LFoutputs = OutputsFrame(self.Foutputs, self.module_root)
        self.LFoutputs.pack(anchor="nw")

        self.Fconnections = ttk.Frame(self)
        self.LFconnections = ConnectionsFrame(
            self.Fconnections, self.module_root
        )
        self.LFconnections.pack(anchor="nw")

        self.Finfo = ttk.Frame(self)
        self.LFinfo = InfoFrame(self.Finfo, self.module_root)
        self.LFinfo.pack(anchor="nw")

        self.p.add(self.Finputs)
        self.p.add(self.Foutputs)
        self.p.add(self.Fconnections)
        self.p.add(self.Finfo)

        self.wip_notice = ttk.Label(
            self, text="NOTE: GUI IS A WORK-IN-PROGRESS", anchor=tk.CENTER
        )
        self.wip_notice.pack(side="bottom", fill=tk.X)

        for smodule in self.module_root._shared_modules:
            if hasattr(smodule, "tk_frame"):
                setattr(self, smodule.frame_attr, smodule.tk_frame(self))
                this_frame = getattr(self, smodule.frame_attr)
                smodule._set_gui_instance(self.module_root)
                this_frame.pack(
                    side="left", fill=tk.Y, padx="14px", pady="14px"
                )

        self._update_input_output_listboxes()

    def _update_loop(self):

        self.LFinfo._update_deltas()
        self.after(1000, self._update_loop)

    def _update_input_output_listboxes(self):

        # request = RequestGetModules(self.module_root)
        # modules = self.module_root.broker.process_request(request)

        modules = self.module_root._shared_modules

        self.LFinputs.listbox.delete(0, tk.END)  # clear input listbox
        self.LFoutputs.listbox.delete(0, tk.END)  # clear output listbox

        for i in range(len(modules)):

            module = modules[i]

            if hasattr(module, "get"):

                self.LFinputs.listbox.insert(tk.END, module._module_name)

            if hasattr(module, "set"):

                self.LFoutputs.listbox.insert(tk.END, module._module_name)

    def _create_bindings(self):

        # for bind in self.binds:
        #     print(bind)

        self.parent.bind(
            "<Control-Return>", self.LFconnections._toggle_sync_externally
        )
        self.LFinputs.listbox.bind(
            "<Return>", self.LFconnections._add_connection
        )
        self.LFoutputs.listbox.bind(
            "<Return>", self.LFconnections._add_connection
        )
        # self.LFoutputs.testset_data.bind("<Return>", self.LFoutputs._set_test)
        self.LFconnections.listbox.bind(
            "<Delete>", self.LFconnections._remove_connection
        )
        self.LFconnections.hzbox.bind(
            "<Return>", self.LFconnections._add_connection
        )

    def _update_output_listbox(self):

        request = volux.request.RequestGetModules(self.module_root)
        modules = self.broker.process_request(request)

        for i in range(len(modules)):

            module = self.module_root._shared_modules[i]

            if hasattr(module, "set"):

                self.output_listbox.insert(tk.END, module._module_name)

    def _flash_red(self, widget, flash_duration=0.5, flash_iters=3):

        w_type = type(widget)

        if w_type is ttk.Entry:
            red_target = "style"
            red_value = "Error.TEntry"
            normal_value = "TEntry"
        elif w_type is tk.Listbox:
            red_target = "background"
            red_value = "RED"
            normal_value = "WHITE"
        else:
            raise TypeError(
                "cannot do _flash_red on widget of type {}".format(w_type)
            )

        def func_flash_red():
            for i in range(flash_iters):
                time.sleep(0.5)
                widget[red_target] = red_value
                time.sleep(0.5)
                widget[red_target] = normal_value

        flash_thread = threading.Thread(target=func_flash_red)
        flash_thread.start()
