# external
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# site
import volux


class ConnectionsFrame(ttk.Labelframe):
    def __init__(self, parent, module_root, *args, **kwargs):
        super().__init__(parent, text="Connections", *args, **kwargs)
        self.parent = parent
        self.module_root = module_root

        self.sync_running = tk.BooleanVar()

        self.checkbutton = ttk.Checkbutton(
            self,
            text="Enable Sync",
            variable=self.sync_running,
            command=self._sync_toggled,
        )
        self.checkbutton.pack(side="top", anchor="nw", fill=tk.Y)

        self.data = ttk.Frame(self, relief="raised", borderwidth="2px")
        self.data.pack(side="top", fill=tk.X, pady="2px")

        self.listbox = tk.Listbox(
            self.data, selectmode=tk.EXTENDED, exportselection=True
        )
        self.listbox.pack(side="left", fill=tk.X)

        self.data_buttons = ttk.Frame(self.data)
        self.data_buttons.pack(side="left")

        self.controls = ttk.Frame(self)
        self.controls.pack()

        self.add_button = ttk.Button(
            self.data_buttons, text="ADD", command=self._add_connection
        )
        self.add_button.pack(side="top")

        self.remove_button = ttk.Button(
            self.data_buttons, text="REMOVE", command=self._remove_connection
        )
        self.remove_button.pack(side="top")

        self.refresh = ttk.Button(
            self.data_buttons,
            text="REFRESH",
            command=self._refresh_connections,
        )
        self.refresh.pack(side="top")

        self.hzbox_label = ttk.Label(self.controls, text="Pollrate (Hz)")
        self.hzbox_label.grid(row=1, column=1)

        self.hzbox = ttk.Entry(self.controls, width="5")
        self.hzbox.grid(row=1, column=2)

    def _sync_toggled(self):

        sync_enabled_in_gui = self.sync_running.get()

        if sync_enabled_in_gui is True:

            self._start_connection_sync()

        elif sync_enabled_in_gui is False:

            self._stop_connection_sync()

    def _remove_connection(self, event=None):

        connection = self._get_selected_connection()
        request = volux.request.RemoveConnection(
            self.module_root, connection=connection
        )
        self.module_root.broker.process_request(request)
        self._refresh_connections()

    def _start_connection_sync(self):

        request = volux.request.StartSync(self.module_root)

        self.module_root.broker.process_request(request)

    def _stop_connection_sync(self):

        request = volux.request.StopSync(self.module_root)

        self.module_root.broker.process_request(request)

    def _get_sync_state(self):

        request = volux.request.SyncState(self.module_root)

        return self.module_root.broker.process_request(request, verbose=False)

    def _get_selected_connection(self):

        connections = self._get_connections()
        connection_index = self.listbox.curselection()[0]
        i = 0
        for connection_UUID in connections:
            if i == connection_index:
                return connections[connection_UUID]
            i += 1

    def _toggle_sync_externally(self, event=None):

        self.sync_running.set(not self.sync_running.get())
        self._sync_toggled()

    def _refresh_connections(self):

        connections = self._get_connections()
        self.listbox.delete(0, tk.END)

        for cUUID in connections:

            self.listbox.insert(tk.END, connections[cUUID].nickname)

    def _add_connection(self, event=None):

        input_module = (
            self.module_root.mainApp.LFinputs._get_selected_input_module()
        )
        output_module = (
            self.module_root.mainApp.LFoutputs._get_selected_output_module()
        )
        hz_input = self._get_sync_hz()

        missing_data = {}

        if input_module is None:
            missing_data.update(
                {"input module": self.module_root.mainApp.LFinputs.listbox}
            )

        if output_module is None:
            missing_data.update(
                {"output module": self.module_root.mainApp.LFoutputs.listbox}
            )

        if hz_input is None:
            missing_data.update({"pollrate": self.hzbox})

        if len(missing_data) > 0:
            messagebox.showerror(
                "Volux GUI - Missing Data",
                "Please specify: \n- {}".format(
                    "\n- ".join(missing_data.keys())
                ),
            )
            for input_area in missing_data.values():
                self.module_root.mainApp._flash_red(input_area)

        else:
            connection = volux.VoluxConnection(
                input_module,
                output_module,
                self.module_root.mainApp.LFconnections._get_sync_hz(),
            )
            request = volux.request.AddConnection(
                self.module_root, connection=connection
            )
            self.module_root.broker.process_request(request)
            self._refresh_connections()

    def _get_connections(self):

        request = volux.request.GetConnections(self.module_root)
        return self.module_root.broker.process_request(request)

    def _get_sync_hz(self):

        hzbox_val = self.hzbox.get()
        if hzbox_val == "":
            return None
        else:
            return int(hzbox_val)
