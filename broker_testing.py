import volux
import threading
from time import sleep
from voluxcliprint import VoluxCliPrint
from voluxaudio import VoluxAudio
from voluxgui import VoluxGui

vlx = volux.VoluxOperator()

cli_UUID = vlx.add_module(VoluxCliPrint())
audio_UUID = vlx.add_module(VoluxAudio())
gui_UUID = vlx.add_module(
    VoluxGui(shared_modules=[vlx.audio,vlx.cli]),
    req_permissions=[
        volux.RequestNewConnection,
        volux.RequestGetConnections,
        volux.RequestStartSync
    ]
)

vlx.modules[gui_UUID].init_window()  # init GUI
vlx.stop_sync()  # stop syncing connections
