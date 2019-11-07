def launch_gui():

    from volux import VoluxOperator
    from voluxlight import VoluxLight
    from voluxgui import VoluxGui

    vlx = VoluxOperator()
    vlx.add_module(VoluxLight(init_mode="device",init_mode_args={'label': 'Strip'}))
    vlx.add_module(VoluxGui(shared_modules=[vlx.light]))
    vlx.gui.init_window()
