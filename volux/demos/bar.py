# type: ignore

"""Defines volux bar demo."""

# builtin
import sys

# package
from volux.demo import VoluxDemo

# ensure python 3 or above is being used.
if sys.version_info[0] < 3:
    raise RuntimeError("Python 3 or above required.")


class DemoVolLuxBar(VoluxDemo):
    """Volux demo for overlay elements and interaction with modules."""

    def __init__(self, *args, **kwargs):
        """See class docstring."""
        super().__init__(
            demo_name="Demo Vol Lux Bar",
            demo_method=self._run_demo,
            alias="bar",
            requirements=["voluxbar", "voluxlight", "voluxvolume", "colorama"],
            *args,
            **kwargs
        )

    def _run_demo(self):

        self._check_reqs()

        import volux
        import voluxbar
        import voluxlight
        import voluxvolume
        import colorama

        device_label = str(
            input(  # nosec
                "LIFX device's label (case-sensitive!) [Demo Bulb]: "
            )
        )
        if device_label == "":
            device_label = "Demo Bulb"

        # create Volux Operator object (hub for communication between modules)
        vlx = volux.VoluxOperator()

        vol_UUID = vlx.add_module(voluxvolume.VoluxVolume())
        bar_UUID = vlx.add_module(voluxbar.VoluxBar())
        vlx.modules[bar_UUID].add_mode("default", vlx.modules[vol_UUID])
        try:
            demolight_UUID = vlx.add_module(
                voluxlight.VoluxLight(
                    instance_label="demo",
                    init_mode="device",
                    init_mode_args={"label": device_label},
                )
            )
            vlx.modules[bar_UUID].add_mode(
                "light", vlx.modules[demolight_UUID]
            )
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
        vlx.modules[bar_UUID].init_window()
