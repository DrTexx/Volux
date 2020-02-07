def launch(connection_preset=""):

    # builtins
    import os
    import sys
    import threading
    import logging
    import importlib

    # site
    import volux
    import colorama
    import lifxlan

    try:
        import voluxlightvisualiser
    except ImportError:
        print(
            colorama.Fore.RED
            + "couldn't import voluxlightvisualiser!"
            + colorama.Style.RESET_ALL
        )

    # package
    from voluxgui import VoluxGui
    from voluxlight import get_all_lights

    log = logging.getLogger("voluxgui launch")
    log.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)d"
    )
    ch.setFormatter(formatter)
    log.addHandler(ch)

    vlx = volux.VoluxOperator()

    shared_modules = []

    def add_volux_module(module_name, class_name, *args, **kwargs):

        try:
            module = importlib.import_module(module_name)
            module_UUID = vlx.add_module(
                getattr(module, class_name)(*args, **kwargs)
            )
            shared_modules.append(vlx.modules[module_UUID])
            return module_UUID
        except Exception as err:
            log.warning("failed to import {}... ({})".format(module_name, err))

    audio_UUID = add_volux_module("voluxaudio", "VoluxAudio")

    cache_UUID = vlx.add_module(volux.VoluxCache())
    shared_modules.append(vlx.modules[cache_UUID])

    invert_UUID = vlx.add_module(volux.VoluxInvert())
    shared_modules.append(vlx.modules[invert_UUID])

    light_labels = []  # note: pretty hacky, not ideal. Wastes time.
    for light in get_all_lights():
        light_labels.append(light.get_label())

    print("light labels:", light_labels)
    for light_label in light_labels:
        add_volux_module(
            "voluxlight",
            "VoluxLight",
            instance_label=light_label,
            init_mode="device",
            init_mode_args={"label": light_label},
        )

    l_strip_UUID = add_volux_module(
        "voluxlight",
        "VoluxLight",
        instance_label="strip",
        init_mode="device",
        init_mode_args={"label": "Strip"},
    )
    vis_UUID = add_volux_module(
        "voluxlightvisualiser",
        "VoluxLightVisualiser",
        mode="intense",
        hueHz=120,
        hue_cycle_duration=5,
    )
    try:
        vis2_UUID = vlx.add_module(
            voluxlightvisualiser.VoluxLightVisualiser(
                mode="intense",
                hueHz=120,
                hue_cycle_duration=5,
                initial_hue=65535 / 2,
            )
        )
        shared_modules.append(vlx.modules[vis2_UUID])
    except Exception:
        log.warning(
            "couldn't make second vis, has voluxlightvisualiser imported correctly?"
        )
    add_volux_module("voluxvolume", "VoluxVolume")

    gui_UUID = vlx.add_module(
        # VoluxGui(shared_modules=gui_shared_modules),
        VoluxGui(shared_modules=shared_modules),
        req_permissions=[
            volux.requests.SyncState,
            volux.requests.AddConnection,
            volux.requests.RemoveConnection,
            volux.requests.GetConnections,
            volux.requests.StartSync,
            volux.requests.StopSync,
            volux.requests.GetSyncDeltas,
            volux.requests.GetConnectionNicknames,
        ],
    )

    if connection_preset == "lightshow":

        connection_list = [
            volux.VoluxConnection(
                vlx.modules[audio_UUID], vlx.modules[gui_UUID], 120
            ),
            volux.VoluxConnection(
                vlx.modules[audio_UUID], vlx.modules[vis_UUID], 120
            ),
            volux.VoluxConnection(
                vlx.modules[vis_UUID], vlx.modules[l_strip_UUID], 120
            ),
        ]

        for connection in connection_list:
            vlx.add_connection(connection)

        vlx.gui.mainApp.LFconnections._refresh_connections()
        vlx.gui.mainApp.LFconnections._toggle_sync_externally()

    vlx.gui.init_window()
    vlx.stop_sync()


if __name__ == "__main__":
    launch()
