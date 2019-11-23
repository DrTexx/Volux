from volux.demo import VoluxDemo


class DemoGuiVis(VoluxDemo):
    def __init__(self, *args, **kwargs):
        super().__init__(
            demo_name="Demo Gui Vis",
            demo_method=self.run_demo,
            alias="guivis",
            *args,
            **kwargs
        )

    def run_demo(self):

        import volux  # import essentials
        import voluxaudio  # module to get amplitude of desktop audio
        import voluxgui  # module to generate GUI

        # instantiate an operator for managing connections
        vlx = volux.VoluxOperator()
        # add modules
        vlx.add_module(volux.modules.VoluxCliPrint())
        vlx.add_module(voluxaudio.VoluxAudio())
        vlx.add_module(voluxgui.VoluxGui())
        # add connections
        vlx.add_connection(
            volux.VoluxConnection(vlx.audio, vlx.gui, 120)
        )  # change GUI bar to match audio amplitude
        # vlx.add_connection(volux.VoluxConnection(vlx.audio,vlx.cli,120))  # print audio amplitude to terminal
        vlx.start_sync()
        vlx.gui.init_window()
