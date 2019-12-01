# builtin
import logging

# external
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

log = logging.getLogger("voluxgui module - inputsframe")
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


class InputsFrame(ttk.Labelframe):
    def __init__(self, parent, module_root, *args, **kwargs):
        super().__init__(parent, text="Inputs", *args, **kwargs)
        self.parent = parent
        self.module_root = module_root

        self.listbox = tk.Listbox(
            self, selectmode=tk.SINGLE, exportselection=False
        )
        self.listbox.pack(anchor="nw", side="top", fill=tk.X)

        self.refresh_button = ttk.Button(
            self, text="Refresh", command=self._refresh_input_list
        )
        self.refresh_button.pack(anchor="nw", side="top", fill=tk.X)

        # self.testget = ttk.Button(
        #     self, text="Get Test", command=self._get_test
        # )
        # self.testget.pack(anchor="nw", side="top", fill=tk.X)

    def _refresh_input_list(self):

        modules = self.module_root._shared_modules

        self.listbox.delete(0, tk.END)  # clear input listbox

        for i in range(len(modules)):

            module = modules[i]

            if hasattr(module, "get"):

                self.listbox.insert(tk.END, module._module_name)

    def _get_test(self):

        input_module = self._get_selected_input_module()

        if input_module is not None:

            get_result = input_module.get()
            log.info("get method response: {}".format(get_result))

        else:

            messagebox.showerror("Volux GUI", "Please select an input to test")

    def _get_selected_input_module(self):

        sel = self.listbox.curselection()
        if len(sel) > 0:
            i = sel[0]
            return self.module_root._shared_modules[i]
        else:
            return None
