import volux
from voluxbar import VoluxBar
from voluxdemomodule import VoluxDemoModule

# create Volux Operator object (hub for communication between modules)
vlx = volux.VoluxOperator()

# load Volux Bar module
vlx.add_module(VoluxBar())
vlx.add_module(VoluxDemoModule())

vlx.bar.add_mode("default",vlx.demo)

vlx.bar.modes['default'].set(20)
print(vlx.demo.get())

# list loaded modules
# vlx.list_modules()

# return info for a module
# vlx.bar.get_module_info()
