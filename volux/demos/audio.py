# type: ignore

"""Defines a simple audio module demo."""

# package
from volux import VoluxDemo


class DemoAudio(VoluxDemo):
    """Simple audio demo that prints amplitude to terminal every x seconds."""

    def __init__(self, *args, **kwargs):
        """See class docstring for infomation."""
        super().__init__(
            demo_name="Demo Audio",
            demo_method=self._run_demo,
            alias="audio",
            requirements=["voluxaudio"],
            *args,
            **kwargs
        )

    def _run_demo(self):

        self._check_reqs()

        from time import sleep
        import volux
        import voluxaudio

        # create Volux Operator object (hub for communication between modules)
        vlx = volux.VoluxOperator()

        audio_UUID = vlx.add_module(voluxaudio.VoluxAudio())
        cli_UUID = vlx.add_module(volux.VoluxCliPrint())

        vlx.add_connection(
            volux.VoluxConnection(
                vlx.modules[audio_UUID], vlx.modules[cli_UUID], 60
            )
        )

        try:
            while True:
                vlx.start_sync()
                sleep(10)
                vlx.stop_sync()
                print("Ctrl+C to exit demo at any time")
                sleep(4)
        except KeyboardInterrupt:
            print("exiting...")
        finally:
            vlx.stop_sync()
            exit()
