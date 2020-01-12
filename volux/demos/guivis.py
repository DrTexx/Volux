# type: ignore

"""Defines the guivis demo."""

# package
from volux.demo import VoluxDemo
from volux import requests as voluxRequests


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

        # instantiate an operator for managing connections
        vlx = volux.VoluxOperator()
        # add modules
        cli_UUID = vlx.add_module(volux.VoluxCliPrint())
        audio_UUID = vlx.add_module(voluxaudio.VoluxAudio())
        gui_UUID = vlx.add_module(
            voluxgui.VoluxGui(
                shared_modules=[vlx.modules[cli_UUID], vlx.modules[audio_UUID]]
            ),
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
                vlx.modules[audio_UUID], vlx.modules[gui_UUID], 120
            )
        )  # change GUI bar to match audio amplitude
        # vlx.add_connection(volux.VoluxConnection(vlx.audio,vlx.cli,120))  # print audio amplitude to terminal
        vlx.modules[gui_UUID].mainApp.LFconnections._refresh_connections()
        vlx.modules[gui_UUID].mainApp.LFconnections._toggle_sync_externally()
        vlx.modules[gui_UUID].init_window()
        vlx.stop_sync()
        print("Ctrl+C to end demo...")
