import volux  # import essentials
from modules.voluxaudio import (
    VoluxAudio,
)  # module to get amplitude of desktop audio
from modules.cliprint import VoluxCliPrint  # module to print values to CLI
from modules.voluxgui import VoluxGui  # module to generate GUI

vlx = volux.VoluxOperator()  # instantiate an operator for managing connections
vlx.add_module(VoluxAudio())
vlx.add_module(VoluxCliPrint())
vlx.add_module(VoluxGui())
vlx.add_connection(
    volux.VoluxConnection(vlx.audio, vlx.gui, 120)
)  # change GUI bar to match audio amplitude
# vlx.add_connection(volux.VoluxConnection(vlx.audio,vlx.cli,120))  # print audio amplitude to terminal
vlx.start_sync()
vlx.gui.init_window()
