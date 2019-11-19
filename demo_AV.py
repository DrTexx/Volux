import volux
from voluxlightvisualiser import VoluxLightVisualiser, INTENSE_MODE
from voluxaudio import VoluxAudio
from voluxlight import VoluxLight

vlx = volux.VoluxOperator()

audio_UUID = vlx.add_module(VoluxAudio())
lstrip_UUID = vlx.add_module(VoluxLight(instance_label="strip",init_mode="device",init_mode_args={'label': 'Strip'}))
vis_UUID = vlx.add_module(VoluxLightVisualiser(mode=INTENSE_MODE,hueHz=240,hue_cycle_duration=5))

vlx.add_connection(
    volux.VoluxConnection(
        vlx.modules[audio_UUID],
        vlx.modules[vis_UUID],
        240
    )
)
vlx.add_connection(
    volux.VoluxConnection(
        vlx.modules[vis_UUID],
        vlx.modules[lstrip_UUID],
        240
    )
)

try:
    vlx.start_sync()
    input("press any key to stop...")
except KeyboardInterrupt:
    print("Exit signal sent!")
finally:
    vlx.stop_sync()
