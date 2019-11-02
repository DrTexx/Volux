import volux
from voluxbar import VoluxBar

# create Volux Operator object (hub for communication between modules)
vlx = volux.VoluxOperator()

# load Volux Bar module
vlx.add_module(VoluxBar())

# list loaded modules
# vlx.list_modules()

# return info for a module
# vlx.bar.get_module_info()
