# builtin
import logging

# external
import tkinter as tk
from tkinter import ttk

# site
import volux

log = logging.getLogger("voluxgui launch")
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)d"
)
ch.setFormatter(formatter)
log.addHandler(ch)


class TestFrame(ttk.Labelframe):
    def __init__(self, parent, module_root, *args, **kwargs):
        super().__init__(parent, text="Test", *args, **kwargs)
        self.parent = parent
        self.module_root = module_root

        self.block_core = ttk.Frame(self)

        self.output = ttk.Frame(self, height="10px", width="10px")

        self.labeltest = ttk.Label(self, text="test")

        self.labeltest.pack()
        self.output.pack()
        self.block_core.pack()

        ########################################

        self.keybinds = {"Toggle Sync - <Ctrl> + <Enter>"}

        self.binds_title = ttk.Label(self, text="Keyboard shortcuts")
        self.binds_title.pack(anchor="nw")

        self.sep1 = ttk.Separator(self, orient="horizontal")
        self.sep1.pack(anchor="nw", fill=tk.X)

        self.binds_list = ttk.Label(
            self, text="{}".format("\n".join(self.keybinds))
        )
        self.binds_list.pack(anchor="nw")

        self.deltas_title = ttk.Label(self, text="Sync deltas")
        self.deltas_title.pack(anchor="nw")

        self.sep1 = ttk.Separator(self, orient="horizontal")
        self.sep1.pack(anchor="nw", fill=tk.X)

        self.deltas_list = ttk.Label(self, text="")
        self.deltas_list.pack(anchor="nw")
