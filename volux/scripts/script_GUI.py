import threading
import colorama
from time import sleep
import tkinter as tk
from tkinter import ttk

def launch_gui():

    from volux import VoluxOperator
    from voluxcliprint import VoluxCliPrint
    from voluxlight import VoluxLight
    from voluxaudio import VoluxAudio
    from voluxgui import VoluxGui

    visHz = 240

    vlx = VoluxOperator()
    vlx.add_module(VoluxCliPrint())
    vlx.add_module(VoluxLight(instance_label="strip",init_mode="device",init_mode_args={'label': 'Strip'}))
    vlx.add_module(VoluxLight(instance_label="lamp",init_mode="device",init_mode_args={'label': 'Demo Bulb'}))
    vlx.add_module(VoluxAudio(sensitivity=8))
    # vlx.add_module(VoluxLight(init_mode="device",init_mode_args={'label': 'Demo Bulb'}))  # fix: overwrites the first instance, needs addressing

    gui_shared_modules = [vlx.light_lamp,vlx.light_strip,vlx.cli,vlx.audio]

    vis_added = False

    try:

        # raise Exception("A BIG ERROR")
        from voluxlightvisualiser import VoluxLightVisualiser, INTENSE_MODE
        vlx.add_module(VoluxLightVisualiser(mode=INTENSE_MODE,packetHz=240,hueHz=240,hue_cycle_duration=5))
        gui_shared_modules.append(vlx.vis)
        vis_added = True

    except Exception as err:

        print("{}WARNING: couldn't add visualiser module... reason: {}{}".format(colorama.Fore.YELLOW,err,colorama.Style.RESET_ALL))

    vlx.add_module(VoluxGui(shared_modules=gui_shared_modules))

    if vis_added == True:
        def vis_func(loop_hz):
            while True:
                while vlx.gui.mainApp.vis_frame.vis_on.get() == True:
                    vlx.vis.set(vlx.audio.get())
                    vis_get = vlx.vis.get_from_gui()
                    vlx.light_strip.set_color(vis_get)
                    vlx.light_lamp.set_color(vis_get)
                    sleep(1/loop_hz)

                    # print("START VISUALISER")
                    # vlx.vis.start()
                    # while vlx.vis._enabled == True:
                    #     vlx.vis.set(vlx.audio.get())
                    #     vlx.light.set_color(vlx.vis.get())
                    #     sleep(1/loop_hz)
                sleep(1)

        _vis_func_thread = threading.Thread(target=vis_func,args=(visHz,))
        _vis_func_thread.start()

    vlx.gui.init_window()
    vlx.audio.stop()

    if vis_added == True:
        vlx.vis.stop()
