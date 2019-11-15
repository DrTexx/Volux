import volux
from voluxcliprint import VoluxCliPrint  # import CLI module
from voluxaudio import VoluxAudio  # import audio module
from voluxgui import VoluxGui  # import GUI module

vlx = volux.VoluxOperator()  # create operator class

cli_UUID = vlx.add_module(VoluxCliPrint())  # load the CLI module
audio_UUID = vlx.add_module(VoluxAudio())  # load the audio module
gui_UUID = vlx.add_module(
    VoluxGui(shared_modules=[vlx.audio,vlx.cli]),
    req_permissions=[
        volux.RequestNewConnection,
        volux.RequestGetConnections,
        volux.RequestStartSync,
        volux.RequestSyncState
    ]
)  # add GUI module

vlx.modules[gui_UUID].init_window()  # init the GUI

vlx.stop_sync()  # stop syncing connections
