def launch():

    # builtins
    import os
    import sys
    import threading
    import logging
    import importlib

    # site
    import volux
    import colorama

    # package
    from .gui import VoluxGui

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

    def add_volux_module(module_name, class_name):

        module = importlib.import_module(module_name)
        module_UUID = vlx.add_module(getattr(module, class_name)())
        shared_modules.append(vlx.modules[module_UUID])
        print("imported {}!".format(module_name))

    add_volux_module("voluxaudio", "VoluxAudio")

    vlx.add_module(
        # VoluxGui(shared_modules=gui_shared_modules),
        VoluxGui(shared_modules=shared_modules),
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
