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

    # inital values
    vis_added = False

    # create instance of VoluxOperator
    vlx = VoluxOperator()
    vlx.add_module(VoluxCliPrint())  # add VoluxCliPrint module
    vlx.add_module(VoluxAudio(sensitivity=8))  # add VoluxAudio module

    gui_shared_modules = [vlx.cli,vlx.audio]

    # try adding voluxlight module


    def try_adding_light(**kwargs):
        try:
            return VoluxLight(**kwargs)
        except Exception as err:
            print("{}WARNING: couldn't init light module/s... reason: {}{}".format(colorama.Fore.YELLOW,err,colorama.Style.RESET_ALL))

    lightmodules = [
        try_adding_light(instance_label="strip",init_mode="device",init_mode_args={'label': 'Strip'}),
        try_adding_light(instance_label="demo",init_mode="device",init_mode_args={'label': 'Demo Bulb'})
    ]


    for lightmodule in lightmodules:
        try:
            vlx.add_module(lightmodule)
            gui_shared_modules.append(getattr(vlx,lightmodule._module_attr))
        except Exception as err:
            print("{}WARNING: couldn't add light module/s... reason: {}{}".format(colorama.Fore.YELLOW,err,colorama.Style.RESET_ALL))

    # try:
    #     while hasattr(vlx,'light_all') == False:
    #         vlx.add_module(VoluxLight(instance_label="all",init_mode="all_devices"))
    #         gui_shared_modules.append(vlx.light_all)
    # except:
    #     pass

    # try adding voluxlightvisualiser module
    try:
        from voluxlightvisualiser import VoluxLightVisualiser, INTENSE_MODE
        vlx.add_module(VoluxLightVisualiser(mode=INTENSE_MODE,packetHz=240,hueHz=240,hue_cycle_duration=5))
        gui_shared_modules.append(vlx.vis)
        vis_added = True
    except Exception as err:
        print("{}WARNING: couldn't add visualiser module... reason: {}{}".format(colorama.Fore.YELLOW,err,colorama.Style.RESET_ALL))

    vlx.add_module(VoluxGui(shared_modules=gui_shared_modules))

    if vis_added == True:

        visHz = 120

        def vis_func(loop_hz):

            while True:

                if vlx.gui.mainApp.vis_frame.vis_on.get() == True:

                    vlx.vis.start()
                    print("vis threads started...")

                    while vlx.gui.mainApp.vis_frame.vis_on.get() == True:

                        amp = vlx.audio.get()

                        container_width = vlx.gui.mainApp.vis_frame.visualiser_bar.winfo_width()
                        vlx.gui.mainApp.vis_frame.visualiser_bar_fill.config(width=container_width*(amp/100))

                        vlx.vis.set(amp)
                        vis_get = vlx.vis.get_from_gui()

                        vlx.vis.set(100-amp)
                        vis_get_invert = vlx.vis.get_from_gui()

                        if hasattr(vlx,'light_strip'):
                            vlx.light_strip.set_color(vis_get)
                        # if hasattr(vlx,'light_ceiling'):
                        #     vlx.light_ceiling.set_color(vis_get_invert)
                        # if hasattr(vlx,'light_all'):
                        #     vlx.light_all.set_color(vis_get)

                        sleep(1/loop_hz)

                    vlx.vis.stop()
                    print("vis threads stopped...")

                sleep(1)

        threading.Thread(target=vis_func,args=(visHz,)).start()

    vlx.gui.init_window()
    vlx.audio.stop()

    if vis_added == True:
        vlx.vis.stop()
