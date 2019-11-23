import volux
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import logging
import threading
from time import sleep

log = logging.getLogger("voluxgui module")
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

        self.mainApp.value_bar_fill.config(
            width=container_width * (self.val / 100)
        )

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
            self.parent, height=14, width=100, pad="1px"
        )
        self.value_bar.pack(side="top", fill=tk.X)

        self.value_bar_fill = ttk.Frame(
            self.value_bar, height=14, width=0, style="value_bar_fill.TFrame"
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
        self.LFoutputs.testset_data.bind("<Return>", self.LFoutputs._set_test)
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
                sleep(0.5)
                widget[red_target] = red_value
                sleep(0.5)
                widget[red_target] = normal_value

        flash_thread = threading.Thread(target=func_flash_red)
        flash_thread.start()


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

        self.testget = ttk.Button(
            self, text="Get Test", command=self._get_test
        )
        self.testget.pack(anchor="nw", side="top", fill=tk.X)

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

        self.testset = ttk.Button(
            self, text="Set Test", command=self._set_test
        )
        self.testset.pack(anchor="nw", side="top", fill=tk.X)

        self.testset_data = ttk.Entry(self)
        self.testset_data.pack()

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
        request = volux.request.RequestRemoveConnection(
            self.module_root, connection=connection
        )
        self.module_root.broker.process_request(request)
        self._refresh_connections()

    def _start_connection_sync(self):

        request = volux.request.RequestStartSync(self.module_root)

        self.module_root.broker.process_request(request)

    def _stop_connection_sync(self):

        request = volux.request.RequestStopSync(self.module_root)

        self.module_root.broker.process_request(request)

    def _get_sync_state(self):

        request = volux.request.RequestSyncState(self.module_root)

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
            request = volux.request.RequestAddConnection(
                self.module_root, connection=connection
            )
            self.module_root.broker.process_request(request)
            self._refresh_connections()

    def _get_connections(self):

        request = volux.request.RequestGetConnections(self.module_root)
        return self.module_root.broker.process_request(request)

    def _get_sync_hz(self):

        hzbox_val = self.hzbox.get()
        if hzbox_val == "":
            return None
        else:
            return int(hzbox_val)


class InfoFrame(ttk.Labelframe):
    def __init__(self, parent, module_root, *args, **kwargs):
        super().__init__(parent, text="Info", *args, **kwargs)
        self.parent = parent
        self.module_root = module_root

        self.keybinds = {"Toggle Sync - <Ctrl> + <Enter>"}

        self.binds_title = ttk.Label(self, text="Keyboard shortcuts")
        self.binds_title.pack(anchor="nw")

        self.sep = ttk.Separator(self, orient="horizontal")
        self.sep.pack(anchor="nw", fill=tk.X)

        self.binds_list = ttk.Label(
            self, text="{}".format("\n".join(self.keybinds))
        )
        self.binds_list.pack(anchor="nw")
