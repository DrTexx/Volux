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
    try:
        vlx.add_module(VoluxLight(instance_label="office",init_mode="group",init_mode_args={'group_label': 'Office'}))
        gui_shared_modules.append(vlx.light_office)
    except Exception as err:
        print("{}WARNING: couldn't add light module/s... reason: {}{}".format(colorama.Fore.YELLOW,err,colorama.Style.RESET_ALL))

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
        visHz = 240
        def vis_func(loop_hz):
            while True:
                if vlx.gui.mainApp.vis_frame.vis_on.get() == True:
                    vlx.vis.start()
                    while vlx.gui.mainApp.vis_frame.vis_on.get() == True:
                        vlx.vis.set(vlx.audio.get())
                        vis_get = vlx.vis.get_from_gui()
                        vlx.light_office.set_color(
                            vis_get,
                            # duration=50
                        )
                        sleep(1/loop_hz)
                    vlx.vis.stop()

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
