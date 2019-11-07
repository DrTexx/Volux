from volux import VoluxModule
import tkinter as tk
from tkinter import ttk

class VoluxGui(VoluxModule):
    def __init__(self, shared_modules=[], *args, **kwargs):
        super().__init__(
            module_name="Volux GUI",
            module_attr="gui",
            module_get=self.get,
            module_set=self.set,
            shared_modules=shared_modules
        )

        self.root = tk.Tk()
        self.mainApp = MainApplication(self.root,self,style="mainApp.TFrame")
        self.example_val = 0

    def get(self):

        return self.decoy_val

    def set(self, new_val):

        self.example_val = new_val

    def init_window(self):

        self.gui_style = ttk.Style()
        self.gui_style.configure('mainApp.TFrame', background="#19191B")

        self.mainApp.pack(side="top", fill=tk.BOTH, expand=True)
        self.root.title("Volux")
        screen_size = (self.root.winfo_screenwidth(), self.root.winfo_screenheight())
        self.root.geometry("{}x{}+{}+{}".format(
            800,
            500,
            1920-800,
            1080-500
        )) # define the size of the window
        self.mainApp._update_loop()
        self.root.mainloop()

class MainApplication(ttk.Frame):
    def __init__(self,parent,module_root,*args,**kwargs):
        ttk.Frame.__init__(self,parent,*args,**kwargs)
        self.parent = parent
        self.module_root = module_root
        self.ext_modules = self.module_root._shared_modules

        self.input_frame = ttk.Frame(self)

        self.input_frame.pack(side="left",fill=tk.Y,padx="14px",pady="14px")

        self.input_label = ttk.Label(self.input_frame,text="INPUTS")
        self.input_label.pack(side="top",fill=tk.BOTH)

        self.input_listbox = tk.Listbox(self.input_frame, selectmode=tk.SINGLE)
        self.input_listbox.pack()

        self.input_testget = ttk.Button(self.input_frame,text="Get Test",command=self._get_test)
        self.input_testget.pack()

        print("(VoluxGUI) shared modules:",self.ext_modules)

        self._update_input_listbox()


    def _update_loop(self):

        pass

    def _get_test(self):

        i = self.input_listbox.curselection()[0]
        get_result = self.ext_modules[i].get()
        print("(VoluxGui) get method result:",get_result)

    def _update_input_listbox(self):

        for i in range(len(self.ext_modules)):
            module_name = self.ext_modules[i]._module_name
            self.input_listbox.insert(tk.END,module_name)

        # for key in self.get_method_dict:
        #
        #     item = self.get_method_dict[key]
        #     print(key,item)
        #
        # self.input_listbox_dict = {}
        #
        # for index, module_name in enumerate(self.get_methods, 0): # add each found device to the GUI list
        #     print(index,module_name)
        #     self.input_listbox_dict.update({index: self.get_methods[module_name]})
        #
        # for key in self.input_listbox_dict:
        #
        #     item = self.input_listbox_dict[key]
        #     self.input_listbox.insert(key,item)

    def _get_selected_mdevices(self):
        devices_to_return = [self.parent.mlifx.managed_devices[device_i] for device_i in device_indexes]
        return devices_to_return # return a tuple of indexes for selected items
