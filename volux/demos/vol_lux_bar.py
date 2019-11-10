from ..demo import VoluxDemo
import colorama

class DemoVolLuxBar(VoluxDemo):
    def __init__(self,*args,**kwargs):
        super().__init__(
            demo_name='Demo Vol Lux Bar',
            demo_method=self.run_demo,
            alias="bar",
            *args,
            **kwargs
        )
        self.superclass = VoluxDemo

    def run_demo(self):

        import volux
        from voluxbar import VoluxBar
        from voluxvolume import VoluxVolume

        # create Volux Operator object (hub for communication between modules)
        vlx = volux.VoluxOperator()

        vlx.add_module(VoluxBar())
        vlx.add_module(VoluxVolume())

        vlx.bar.add_mode("default",vlx.volume)

        try:
            raise Exception("OH SHIT")
            from voluxlight import VoluxLight
            vlx.add_module(VoluxLight(instance_label="demo", init_mode="device", init_mode_args={'label': 'Demo Bulb'}))
            vlx.bar.add_mode("light",vlx.light_demo)
        except Exception as err:
            print("{}WARNING: couldn't add light module/s... reason: {}{}".format(colorama.Fore.YELLOW,err,colorama.Style.RESET_ALL))

        # load Volux Bar module
        vlx.bar.init_window()

vol_lux_bar_demo = DemoVolLuxBar()
