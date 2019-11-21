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
    from voluxaudio import VoluxAudio
    from voluxbar import VoluxBar
    from voluxcliprint import VoluxCliPrint
    from voluxgui import VoluxGui
    from voluxlight import VoluxLight, get_all_lights
    from volux_volume import VoluxVolume

    add_lights = True

    # create instance of VoluxOperator
    vlx = volux.VoluxOperator()

    audio_UUID = vlx.add_module(VoluxAudio(sensitivity=8))
    cli_UUID = vlx.add_module(VoluxCliPrint())
    vol_UUID = vlx.add_module(VoluxVolume())

    gui_shared_modules = [
        vlx.modules[audio_UUID],
        vlx.modules[cli_UUID],
        vlx.modules[vol_UUID],
    ]

    if add_lights is True:

        def func_add_lights():

            devices = get_all_lights()

            for device in devices:
                try:
                    light_module = VoluxLight(
                        instance_label=device.get_label(),
                        init_mode="device",
                        init_mode_args={"label": device.get_label()},
                    )
                    light_UUID = vlx.add_module(light_module)
                    gui_shared_modules.append(vlx.modules[light_UUID])
                except Exception as err:
                    log.error(
                        "{}failed adding device ({}) - {}{}".format(
                            colorama.Fore.YELLOW,
                            device.get_label(),
                            err,
                            colorama.Style.RESET_ALL,
                        )
                    )

        threading.Thread(target=func_add_lights).start()

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

    vlx.gui.init_window()
    vlx.audio.stop()
