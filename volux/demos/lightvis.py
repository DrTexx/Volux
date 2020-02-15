# type: ignore

"""Define simple light volux demo."""

# builtin
from typing import Any
import sys

# package
from volux.demo import VoluxDemo

# ensure python 3 or above is being used.
if sys.version_info[0] < 3:
    raise RuntimeError("Python 3 or above required.")


class DemoSimpleLightVis(VoluxDemo):
    """Simple demo for audio visualisation with smartlights."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Please see class docstring."""
        super().__init__(
            demo_name="Demo Simple Light Vis",
            demo_method=self._run_demo,
            alias="lightvis",
            requirements=["voluxaudio", "voluxlight", "voluxlightvisualiser"],
            *args,
            **kwargs
        )

    def _run_demo(self) -> None:

        self._check_reqs()

        import volux
        import voluxaudio
        import voluxlight
        import voluxlightvisualiser as vvis

        script_hz = 60
        device_label = str(
            input("LIFX device's label (case-sensitive!) [Strip]: ")  # nosec
        )
        if device_label == "":
            device_label = "Strip"

        vlx = volux.VoluxOperator()

        audio_UUID = vlx.add_module(voluxaudio.VoluxAudio())
        lstrip_UUID = vlx.add_module(
            voluxlight.VoluxLight(
                instance_label=device_label,
                init_mode="device",
                init_mode_args={"label": device_label},
            )
        )
        vis_UUID = vlx.add_module(
            vvis.VoluxLightVisualiser(
                mode="intense",
                hueHz=script_hz,
                hue_cycle_duration=10,
                input_value_impact=10,
            )
        )

        vlx.add_connection(
            volux.VoluxConnection(
                vlx.modules[audio_UUID], vlx.modules[vis_UUID], script_hz
            )
        )
        vlx.add_connection(
            volux.VoluxConnection(
                vlx.modules[vis_UUID], vlx.modules[lstrip_UUID], script_hz
            )
        )

        try:
            vlx.start_sync()
            input("press [Enter] to stop...")  # nosec
        except KeyboardInterrupt:
            print("Exit signal sent!")
        finally:
            vlx.stop_sync()
