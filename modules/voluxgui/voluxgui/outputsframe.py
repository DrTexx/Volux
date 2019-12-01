# builtin
import logging

# external
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

log = logging.getLogger("voluxgui module - outputsframe")
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


class OutputsFrame(ttk.Labelframe):
    def __init__(self, parent, module_root, *args, **kwargs):
        super().__init__(parent, text="Outputs", *args, **kwargs)
        self.parent = parent
        self.module_root = module_root

        self.listbox = tk.Listbox(
            self, selectmode=tk.SINGLE, exportselection=False
        )
        self.listbox.pack(fill=tk.X)

        self.refresh_button = ttk.Button(
            self, text="Refresh", command=self._refresh_output_list
        )
        self.refresh_button.pack(anchor="nw", side="top", fill=tk.X)

        # self.testset = ttk.Button(
        #     self, text="Set Test", command=self._set_test
        # )
        # self.testset.pack(anchor="nw", side="top", fill=tk.X)
        #
        # self.testset_data = ttk.Entry(self)
        # self.testset_data.pack()

    def _refresh_output_list(self):

        modules = self.module_root._shared_modules

        self.listbox.delete(0, tk.END)  # clear input listbox

        for i in range(len(modules)):

            module = modules[i]

            if hasattr(module, "set"):

                self.listbox.insert(tk.END, module._module_name)

    def _set_test(self, event=None):

        output_module = self._get_selected_output_module()

        if output_module is not None:

            set_response = output_module.set(
                float(self.output_testset_data.get())
            )
            log.info("set method response: {}".format(set_response))

        else:

            messagebox.showerror(
                "Volux GUI", "Please select an output to test"
            )
            raise ValueError("no output selected!")

    def _get_selected_output_module(self):

        sel = self.listbox.curselection()
        if len(sel) > 0:
            i = sel[0]
            return self.module_root._shared_modules[i]
        else:
            return None
