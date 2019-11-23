from volux import VoluxDemo


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

        self._check_reqs()

        from time import sleep
        import volux
        import voluxaudio

        # create Volux Operator object (hub for communication between modules)
        vlx = volux.VoluxOperator()

        vlx.add_module(voluxaudio.VoluxAudio())
        vlx.add_module(volux.VoluxCliPrint())

        vlx.add_connection(volux.VoluxConnection(vlx.audio, vlx.cli, 60))

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
