from volux.demo import VoluxDemo


class DemoSimpleLightVis(VoluxDemo):
    def __init__(self, *args, **kwargs):
        super().__init__(
            demo_name="Demo Simple Light Vis",
            demo_method=self.run_demo,
            alias="lightvis",
            *args,
            **kwargs
        )

    def run_demo(self):

        import volux
        from voluxlightvisualiser import VoluxLightVisualiser, INTENSE_MODE
        from modules.voluxaudio import VoluxAudio
        from modules.voluxlight import VoluxLight

        script_hz = 240
        device_label = str(
            input("LIFX device's label (case-sensitive!) [Strip]: ")
        )
        if device_label == "":
            device_label = "Strip"

        vlx = volux.VoluxOperator()

        audio_UUID = vlx.add_module(VoluxAudio())
        lstrip_UUID = vlx.add_module(
            VoluxLight(
                instance_label="demo",
                init_mode="device",
                init_mode_args={"label": device_label},
            )
        )
        vis_UUID = vlx.add_module(
            VoluxLightVisualiser(
                mode=INTENSE_MODE, hueHz=script_hz, hue_cycle_duration=5
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
            vlx.modules[lstrip_UUID].prepare()
            vlx.start_sync()
            input("press [Enter] to stop...")
        except KeyboardInterrupt:
            print("Exit signal sent!")
        finally:
            vlx.stop_sync()
            vlx.modules[lstrip_UUID].restore()
