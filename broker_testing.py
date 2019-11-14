import volux
from voluxcliprint import VoluxCliPrint
from voluxaudio import VoluxAudio
from voluxgui import VoluxGui

vlx = volux.VoluxOperator()

cli_UUID = vlx.add_module(VoluxCliPrint())
audio_UUID = vlx.add_module(VoluxAudio())
gui_UUID = vlx.add_module(VoluxGui(shared_modules=[vlx.audio,vlx.cli]))

vlx.modules[gui_UUID].init_window()
