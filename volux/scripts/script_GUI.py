import threading
from time import sleep

def launch_gui():

    from volux import VoluxOperator
    from voluxcliprint import VoluxCliPrint
    from voluxlight import VoluxLight
    from voluxaudio import VoluxAudio
    from voluxlightvisualiser import VoluxLightVisualiser, INTENSE_MODE
    from voluxgui import VoluxGui

    visHz = 240

    vlx = VoluxOperator()
    vlx.add_module(VoluxCliPrint())
    vlx.add_module(VoluxLight(init_mode="device",init_mode_args={'label': 'Strip'}))
    vlx.add_module(VoluxAudio())
    # vlx.add_module(VoluxLight(init_mode="device",init_mode_args={'label': 'Demo Bulb'}))  # fix: overwrites the first instance, needs addressing

    try:
        vlx.add_module(VoluxLightVisualiser(mode=INTENSE_MODE,packetHz=240,hueHz=240,hue_cycle_duration=5))
        vlx.add_module(VoluxGui(shared_modules=[vlx.light,vlx.cli,vlx.audio,vlx.vis]))

        def vis_func(loop_hz):
            while True:
                while vlx.gui.mainApp.vis_on.get() == True:
                    vlx.vis.set(vlx.audio.get())
                    vlx.light.set_color(vlx.vis.get())
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
    except Exception as err:
        print("error with vis:",err)
        vlx.add_module(VoluxGui(shared_modules=[vlx.light,vlx.cli,vlx.audio]))
    vlx.gui.init_window()
    vlx.audio.stop()

    try:
        vlx.vis.stop()
    except:
        print("warning: couldn't stop vlx.vis")
