from volux.demo import VoluxDemo


class DemoVolLuxBar(VoluxDemo):
    def __init__(self, *args, **kwargs):
        super().__init__(
            demo_name="Demo Vol Lux Bar",
            demo_method=self.run_demo,
            alias="bar",
            requirements=["voluxbar", "voluxlight", "voluxvolume", "colorama"],
            *args,
            **kwargs
        )

    def run_demo(self):

        self._check_reqs()

        import volux
        import voluxbar
        import voluxlight
        import voluxvolume
        import colorama

        device_label = str(
            input("LIFX device's label (case-sensitive!) [Demo Bulb]: ")
        )
        if device_label == "":
            device_label = "Demo Bulb"

        # create Volux Operator object (hub for communication between modules)
        vlx = volux.VoluxOperator()

        vlx.add_module(voluxvolume.VoluxVolume())
        vlx.add_module(voluxbar.VoluxBar())
        vlx.bar.add_mode("default", vlx.volume)
        try:
            vlx.add_module(
                voluxlight.VoluxLight(
                    instance_label="demo",
                    init_mode="device",
                    init_mode_args={"label": device_label},
                )
            )
            vlx.bar.add_mode("light", vlx.light_demo)
        except Exception as err:
            print(
                "{}WARNING: couldn't add light module/s... reason: {}{}".format(
                    colorama.Fore.YELLOW, err, colorama.Style.RESET_ALL
                )
            )

        # load Volux Bar module
        print(
            "{}Tip: Double right-click bar or press Ctrl+C while this window is active to stop demo{}".format(
                colorama.Fore.YELLOW, colorama.Style.RESET_ALL
            )
        )
        vlx.bar.init_window()
