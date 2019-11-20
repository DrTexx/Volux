import threading
from time import sleep
import tkinter as tk
from tkinter import ttk
import colorama
import logging
import lifxlan

colorama.init()

log = logging.getLogger("volux script - GUI")
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


def launch_gui():

    import volux
    from voluxcliprint import VoluxCliPrint
    from voluxlight import VoluxLight
    from voluxaudio import VoluxAudio
    from voluxgui import VoluxGui

    # inital values
    # vis_added = False

    # create instance of VoluxOperator
    vlx = volux.VoluxOperator()
    cli_UUID = vlx.add_module(VoluxCliPrint())  # add VoluxCliPrint module
    audio_UUID = vlx.add_module(
        VoluxAudio(sensitivity=8)
    )  # add VoluxAudio module

    gui_shared_modules = [vlx.modules[cli_UUID], vlx.modules[audio_UUID]]

    lightmodules = []

    log.info("discovering LIFX devices on network...")
    lifx = lifxlan.LifxLAN(None)
    devices = lifx.get_devices()
    log.info("finished LIFX device discovery")
    log.debug("LIFX devices found: {}".format(devices))

    for device in devices:
        try:
            lightmodules.append(
                VoluxLight(
                    instance_label=device.get_label(),
                    init_mode="device",
                    init_mode_args={"label": device.get_label()},
                )
            )
        except Exception as err:
            log.error(
                "{}failed adding device ({}) - {}{}".format(
                    colorama.Fore.YELLOW,
                    device.get_label(),
                    err,
                    colorama.Style.RESET_ALL,
                )
            )

    for lightmodule in lightmodules:
        try:
            vlx.add_module(lightmodule)
            gui_shared_modules.append(getattr(vlx, lightmodule._module_attr))
        except Exception as err:
            log.warning(
                "{}couldn't add light module/s... reason: {}{}".format(
                    colorama.Fore.YELLOW, err, colorama.Style.RESET_ALL
                )
            )

    # try:
    #     while hasattr(vlx,'light_all') == False:
    #         vlx.add_module(VoluxLight(instance_label="all",init_mode="all_devices"))
    #         gui_shared_modules.append(vlx.light_all)
    # except:
    #     pass

    # try adding voluxlightvisualiser module
    try:
        from voluxlightvisualiser import VoluxLightVisualiser, INTENSE_MODE

        vlx.add_module(
            VoluxLightVisualiser(
                mode=INTENSE_MODE,
                packetHz=240,
                hueHz=240,
                hue_cycle_duration=5,
            )
        )
        gui_shared_modules.append(vlx.vis)
        # vis_added = True
    except Exception as err:
        log.warning(
            "{}couldn't add visualiser module... reason: {}{}".format(
                colorama.Fore.YELLOW, err, colorama.Style.RESET_ALL
            )
        )

    log.debug("shared_modules: {}".format(gui_shared_modules))
    vlx.add_module(
        VoluxGui(shared_modules=gui_shared_modules),
        req_permissions=[
            volux.RequestSyncState,
            volux.RequestAddConnection,
            volux.RequestRemoveConnection,
            volux.RequestGetConnections,
            volux.RequestStartSync,
            volux.RequestStopSync,
        ],
    )

    # if vis_added == True:
    #
    #     visHz = 120
    #
    #     def vis_func(loop_hz):
    #
    #         while True:
    #
    #             if vlx.gui.mainApp.vis_frame.vis_on.get() == True:
    #
    #                 vlx.vis.start()
    #                 print("vis threads started...")
    #
    #                 while vlx.gui.mainApp.vis_frame.vis_on.get() == True:
    #
    #                     amp = vlx.audio.get()
    #
    #                     container_width = vlx.gui.mainApp.vis_frame.visualiser_bar.winfo_width()
    #                     vlx.gui.mainApp.vis_frame.visualiser_bar_fill.config(width=container_width*(amp/100))
    #
    #                     vlx.vis.set(amp)
    #                     vis_get = vlx.vis.get_from_gui()
    #
    #                     vlx.vis.set(100-amp)
    #                     vis_get_invert = vlx.vis.get_from_gui()
    #
    #                     if hasattr(vlx,'light_strip'):
    #                         vlx.light_strip.set_color(vis_get)
    #                     # if hasattr(vlx,'light_ceiling'):
    #                     #     vlx.light_ceiling.set_color(vis_get_invert)
    #                     # if hasattr(vlx,'light_all'):
    #                     #     vlx.light_all.set_color(vis_get)
    #
    #                     sleep(1/loop_hz)
    #
    #                 vlx.vis.stop()
    #                 print("vis threads stopped...")
    #
    #             sleep(1)
    #
    #     threading.Thread(target=vis_func,args=(visHz,)).start()

    vlx.gui.init_window()
    vlx.audio.stop()

    # if vis_added == True:
    #     vlx.vis.stop()
