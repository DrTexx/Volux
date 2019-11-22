# builtin
import importlib

# site
from volux.demo import VoluxDemo


class DemoAudio(VoluxDemo):
    def __init__(self, *args, **kwargs):
        super().__init__(
            demo_name="Demo Audio",
            demo_method=self.run_demo,
            alias="audio",
            requirements=["voluxaudio"],
            *args,
            **kwargs
        )

    def run_demo(self):

        import volux
        import voluxaudio

        # create Volux Operator object (hub for communication between modules)
        vlx = volux.VoluxOperator()

        vlx.add_module(voluxaudio.VoluxAudio())
        vlx.add_module(volux.modules.VoluxCliPrint())

        vlx.add_connection(volux.VoluxConnection(vlx.audio, vlx.cli, 60))

        vlx.start_sync()
