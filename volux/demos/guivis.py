# type: ignore

"""Defines the guivis demo."""

# package
from volux.demo import VoluxDemo
from volux import requests as voluxRequests

SCRIPT_HZ = 60


class DemoGuiVis(VoluxDemo):
    """Demo showing the gui module being influenced by desktop amplitude."""

    def __init__(self, *args, **kwargs):
        """See class docstring."""
        super().__init__(
            demo_name="Demo Gui Vis",
            demo_method=self._run_demo,
            alias="guivis",
            requirements=["voluxaudio", "voluxgui"],
            *args,
            **kwargs
        )

    def _run_demo(self):

        self._check_reqs()

        import volux  # import essentials
        import voluxaudio  # module to get amplitude of desktop audio
        import voluxgui  # module to generate GUI
        import voluxlight
        import voluxlightvisualiser

        # instantiate an operator for managing connections
        vlx = volux.VoluxOperator()
        # add static modules
        cli_UUID = vlx.add_module(volux.VoluxCliPrint())
        audio_UUID = vlx.add_module(voluxaudio.VoluxAudio())
        cache_UUID = vlx.add_module(volux.VoluxCache())
        lightvis_UUID = vlx.add_module(
            voluxlightvisualiser.VoluxLightVisualiser(
                mode="intense", hueHz=SCRIPT_HZ, hue_cycle_duration=5,
            )
        )
        # list static modules for sharing
        shared_modules = [
            vlx.modules[cli_UUID],
            vlx.modules[audio_UUID],
            vlx.modules[cache_UUID],
            vlx.modules[lightvis_UUID],
        ]
        # discover lights
        lights = voluxlight.get_all_lights()
        # load lights into modules
        light_UUIDs = []
        for light in lights:
            light_UUID = vlx.add_module(
                voluxlight.VoluxLight(
                    instance_label=light.get_label(),
                    init_mode="device",
                    init_mode_args={"object": light},
                )
            )
            light_UUIDs.append(light_UUID)
        # add lights to shared modules
        print(light_UUIDs)
        for light_UUID in light_UUIDs:
            shared_modules.append(vlx.modules[light_UUID])
        print(shared_modules)

        # add gui
        gui_UUID = vlx.add_module(
            voluxgui.VoluxGui(shared_modules=shared_modules),
            req_permissions=[
                voluxRequests.SyncState,
                voluxRequests.AddConnection,
                voluxRequests.RemoveConnection,
                voluxRequests.GetConnections,
                voluxRequests.StartSync,
                voluxRequests.StopSync,
                voluxRequests.GetSyncDeltas,
                voluxRequests.GetConnectionNicknames,
            ],
        )
        # add connections
        vlx.add_connection(
            volux.VoluxConnection(
                vlx.modules[audio_UUID], vlx.modules[cache_UUID], SCRIPT_HZ
            )
        )  # set cache to audio amplitude
        vlx.add_connection(
            volux.VoluxConnection(
                vlx.modules[cache_UUID], vlx.modules[gui_UUID], SCRIPT_HZ
            )
        )  # change GUI bar to match cached audio amplitude
        vlx.add_connection(
            volux.VoluxConnection(
                vlx.modules[cache_UUID], vlx.modules[lightvis_UUID], SCRIPT_HZ
            )
        )  # send audio cache to lightvis
        # vlx.add_connection(volux.VoluxConnection(vlx.audio,vlx.cli,120))  # print audio amplitude to terminal
        vlx.modules[gui_UUID].mainApp.LFconnections._refresh_connections()
        vlx.modules[gui_UUID].mainApp.LFconnections._toggle_sync_externally()
        vlx.modules[gui_UUID].init_window()
        vlx.stop_sync()
        print("Ctrl+C to end demo...")
