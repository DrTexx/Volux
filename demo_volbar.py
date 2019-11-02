import volux
from voluxbar import VoluxBar

vlx = volux.VoluxCore()

vlx.add_module(VoluxBar)
vlx.bar.get_module_info()
