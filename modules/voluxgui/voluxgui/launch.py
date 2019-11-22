def launch():

    # builtins
    import os
    import sys
    import threading
    import logging

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

    vlx.add_module(
        # VoluxGui(shared_modules=gui_shared_modules),
        VoluxGui(),
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
