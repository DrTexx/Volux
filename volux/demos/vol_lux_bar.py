from ..demo import VoluxDemo

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
        from voluxlight import VoluxLight

        # create Volux Operator object (hub for communication between modules)
        vlx = volux.VoluxOperator()

        # load Volux Bar module
        vlx.add_module(VoluxBar())
        vlx.add_module(VoluxVolume())
        vlx.add_module(VoluxLight("all_devices", init_mode_args={'label': 'Strip'}, group="Office"))
        vlx.bar.add_mode("default",vlx.volume)
        vlx.bar.add_mode("light",vlx.light)
        vlx.bar.init_window()

vol_lux_bar_demo = DemoVolLuxBar()
