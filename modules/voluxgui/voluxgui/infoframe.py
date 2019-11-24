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


class InfoFrame(ttk.Labelframe):
    def __init__(self, parent, module_root, *args, **kwargs):
        super().__init__(parent, text="Info", *args, **kwargs)
        self.parent = parent
        self.module_root = module_root

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

        self._update_deltas()

    def _update_deltas(self):

        if hasattr(self.module_root, "broker"):
            deltas = self.request_sync_deltas()
            nicknames = self.request_connection_nicknames()
            log.debug("deltas: {}".format(deltas))
            log.debug("deltas type: {}".format(type(deltas)))

            # delta_strings = [str(delta) for delta in deltas]

            delta_string_list = []
            for cUUID in deltas:
                delta_string_list.append(
                    "{} == {}".format(nicknames[cUUID], str(deltas[cUUID]))
                )

            self.deltas_list.config(
                text="{}".format("\n".join(delta_string_list))
            )
            # else:
            #     raise Exception(
            #         "deltas list empty! should have returned volux.connection.NoDelta instead!"
            #     )

        else:
            print("broker not loaded yet...")

    def request_sync_deltas(self):

        request = volux.request.GetSyncDeltas(self.module_root)
        deltas = self.module_root.broker.process_request(request)
        return deltas

    def request_connection_nicknames(self):

        request = volux.request.GetConnectionNicknames(self.module_root)
        connection_nicknames = self.module_root.broker.process_request(request)
        return connection_nicknames
