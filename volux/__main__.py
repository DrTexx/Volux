import volux
from voluxbar import VoluxBar
from voluxdemomodule import VoluxDemoModule
from voluxvolume import VoluxVolume
from voluxlight import VoluxLight

# create Volux Operator object (hub for communication between modules)
vlx = volux.VoluxOperator()

# load Volux Bar module
vlx.add_module(VoluxBar())
vlx.add_module(VoluxDemoModule())
vlx.add_module(VoluxVolume())
vlx.add_module(VoluxLight("Bob's Lamp"))

vlx.bar.add_mode("default",vlx.volume)
vlx.bar.add_mode("light",vlx.light)

if __name__ == '__main__':

    vlx.bar.init_window()
