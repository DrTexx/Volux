import psutil
import time
import tkinter as Tk
import plyer
from os.path import realpath
from _thread import start_new_thread


class Core:
    def __init__(self,core_id):
        self.data = psutil.sensors_temperatures
        self.core_id = core_id
        self.label = self.data()['coretemp'][core_id][0]
        self.high = self.data()['coretemp'][core_id][2]
        self.critical = self.data()['coretemp'][core_id][3]
    def current(self):
        return(self.data()['coretemp'][self.core_id][1])

def get_cores():
    core_objects = psutil.sensors_temperatures()['coretemp']
    cores = []
    [cores.append(Core(i)) for i in range(len(core_objects))]
    return(cores)

def print_core(core,show_percentages=True):
    high_percent = (core.current() / core.high) * 100
    critical_percent = (core.current() / core.critical) * 100
    print("[CORE]: {:<3} | [TEMP]: {} | [HIGH]: {} | [CRITICAL]: {}".format(core.label,core.current(),core.high,core.critical))
    if show_percentages == True:
        print("--- [{}%] of throttle heat ({}C)".format(round(high_percent,2),core.high))
        print("--- [{}%] of max heat ({}C)".format(round(critical_percent,2),core.critical))

class CoreWatch():
    def __init__(self,cores,check_frequency=10):
        self.running = False
        self.cores = cores
        self.app_name = "CoreWatch"
        self.check_frequency = check_frequency
        self.start()
    def _start_thread(self):
        print("CoreWatch started!")
        self.running = True
        while self.running == True:
            time.sleep(self.check_frequency) # pause between checks
            for core in self.cores:
                now = time.localtime(); timestring = "{:>2}:{:>2}:{:>2}".format(now[3],now[4],now[5])
                print("[{}] {} | core checked".format(timestring,core.label))
                if core.current() >= core.critical:
                    self._core_critical(core)
                elif core.current() >= core.high:
                    self._core_hot(core)
                elif core.current() > 0:
                    pass
                elif core.current() == 0:
                    self._core_abnormal(core)
                else:
                    self._core_abnormal(core)
            print("MEMORY USED: [{:<4}%] Virtual | [{:<4}%] Swap".format(psutil.virtual_memory()[2],psutil.swap_memory()[3]))
    def start(self):
        if self.running == True: print("CoreWatch already running!")
        else:
            start_new_thread(self._start_thread, ())
    def stop(self):
        if self.running == False: print("nothing is running!")
        else: self.running = False
    def _core_hot(self,hot_core):
        plyer.notification.notify(
            title="Core Hot",
            message="{} is running hot!".format(hot_core.label),
            app_name=self.app_name,
            app_icon=realpath("fire.ico"), # must be .ico on Windows
            timeout=10)
    def _core_critical(self,critical_core):
        plyer.notification.notify(
            title="Core Critical",
            message="{} at critical temperature!".format(critical_core.label),
            app_name=self.app_name,
            app_icon=realpath("exclaimation.png"),
            timeout=15)
    def _core_abnormal(self,abnormal_core):
        plyer.notification.notify(
            title="Core Abnormal",
            message="{} is acting abnormally".format(abnormal_core.label),
            app_name=self.app_name,
            app_icon=realpath("abnormal.png"),
            timeout=10)

# ---- SAMPLE CODE ---- #
#cores = get_cores()
#for core in cores: print_core(core,show_percentages=False)
# ---- END SAMPLE CODE ---- #

# class Window(Tk.Frame):
#     def __init__(self,master=None):
#         Tk.Frame.__init__(self,master)
#         self.master = master
#         self.i = 0
#         self._init_window()
#         self.poll_rate = 1000
#         self._updater()
#     def _init_window(self):
#         m = self.master
#         temps = Tk.Frame(m)
#         self.v = Tk.StringVar()
#         temp_text = Tk.Label(m,textvariable=self.v)
#         temp_text.pack()
#         temps.pack()
#     def update_temps(self):
#         self.i += 1
#         out = [self.i]
#         [out.append(core.current()) for core in cores]
#         self.v.set(out)
#     def _updater(self):
#         self.update_temps()
#         self.after(self.poll_rate,self._updater)
# root = Tk.Tk()
# root.geometry("400x400")
# app = Window(root)
# root.mainloop()
