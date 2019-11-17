import volux
from voluxlightvisualiser import VoluxLightVisualiser, INTENSE_MODE  # import the vis module
from voluxcliprint import VoluxCliPrint  # import CLI module
from voluxaudio import VoluxAudio  # import audio module
from voluxlight import VoluxLight  # import light module (for smartbulbs on local network)
from voluxgui import VoluxGui  # import GUI module

vlx = volux.VoluxOperator()  # create operator class

vis_UUID = vlx.add_module(VoluxLightVisualiser(mode=INTENSE_MODE,packetHz=0,hueHz=0,hue_cycle_duration=5))  # load the vis module
cli_UUID = vlx.add_module(VoluxCliPrint())  # load the CLI module
audio_UUID = vlx.add_module(VoluxAudio())  # load the audio module
light_UUID = vlx.add_module(VoluxLight(instance_label="strip",init_mode="device",init_mode_args={"label": "Strip"}))  # load the light module
gui_UUID = vlx.add_module(
    VoluxGui(shared_modules=[vlx.audio,vlx.cli,vlx.light_strip,vlx.vis]),
    req_permissions=[
        volux.RequestNewConnection,
        volux.RequestGetConnections,
        volux.RequestStartSync,
        volux.RequestSyncState,
        volux.RequestStopSync
    ]
)  # add GUI module

vlx.modules[gui_UUID].init_window()  # init the GUI

vlx.stop_sync()  # stop syncing connections
