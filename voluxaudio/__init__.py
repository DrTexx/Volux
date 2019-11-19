from volux import VoluxModule
import numpy as np
import pyaudio
import colorama
from voluxaudio import lifxtools
from time import sleep
from .hsv2ansi import *

colorama.init()
clamp = lambda value, minv, maxv: max(min(value, maxv), minv)

__requires_python__ = [">=3","<3.8"]  # required python version

class VoluxAudio(VoluxModule):
    """
    based on code by the brilliant Scott Harden
    original post code is adapted from:
    https://www.swharden.com/wp/2016-07-19-realtime-audio-visualization-in-python/

    note:
    this code is sensitive to the volume of applications on your desktop.
    Although your actual output audio to speakers shouldn't affect math,
    the volume you're outputting from applications will.
    it is recommended to max out the volume in applications such as spotify
    and then adjust your actual desktop output level to a desirable volume

    protip:
    if you're a spotify user, enable normalization and set your volume level to 'Loud'
    this let's you get the most out of your volume and better maintains audio quality.

    songs for testing:
    Flux Pavilion feat. Steve Aoki - Steve French [looks alright, but beats aren't very solitary]
    Gold Top - Uh Oh (Stand Tall Fists Up Remix) [looks amazing, however the bass is SO INTENSE that multiplier needs to be reduced]
    Yeah Yeah Yeahs - Heads Will Roll (A-Trak Version) (JVH-C Remix) [totally awesome]
    TOP $HELF - Run That $hit [god-tier bass-wobbles and juicy hits]
    Jack U x Ekali x Gravez - Mind (Karol Tip Edit) [insane unique bass that demands attention, inspires me to work on bass isolation so I can replicate the frequency of subs in light saturation]
    SAINT WKND x SAINT MOTEL - MY TYPE [good for testing future bass isolation]
    Jake Hill - Snowflake [my good the audio is the bass in this song, no isolation needed, really clear graph]
    Flume - Burner [thoooose peaaaks are beautiful]
    """

    def __init__(self,sensitivity=9,shared_modules=[],pollrate=None,enable_visualiser=False,*args,**kwargs):
        super().__init__(
            module_name="Volux Audio",
            module_attr="audio",
            module_get=self.get,
            get_type=float,
            get_min=0,
            get_max=100,
            module_set=self.set,
            set_type=float,
            set_min=0,
            set_max=100,
            shared_modules=shared_modules,
            pollrate=pollrate
        )
        self.pa = pyaudio.PyAudio()
        self.stream = self._open_stream()
        self.sensitivity = 9

    def get(self):

        return float(self._get_amplitude())  # 0 .. 100

    def set(self, new_val):

        print("you can't set the audio amplitude!")

    def _open_stream(self):

        stream = self.pa.open(
            format=pyaudio.paInt16,
            channels=2,  # todo: this shouldn't be hardcoded
            rate=44100,  # todo: this shouldn't be hardcoded
            input=True,
            stream_callback=self._stream_callback,
        )
        return stream

    def _stream_callback(self, in_data, frame_count, time_info, flag):

        audio_data = np.frombuffer(in_data, dtype=np.int16)
        self.audio_data = audio_data
        self.needs_update = True  # is this still needed?

        return (audio_data, pyaudio.paContinue)

    def _get_amplitude(self):
        raw_audio_norm = np.linalg.norm(self.audio_data) / len(self.audio_data)
        adj_audio_norm = raw_audio_norm / 2 ** self.sensitivity
        cla_audio_norm = clamp(adj_audio_norm, 0, 1)  # normalized audio returning a value between 0 to 1
        return cla_audio_norm * 100 # 0 .. 100

    def run_it(self):

        # ---- settings ----

        update_Hz = 240      # 120 is default, low-spec PC's need lower Hz, lights can't
                            # handle Hz too high and crash intermitently
                            # note: tilechains take a lot more processing power to do
                            # realtime music-vis, 60 Hz pretty safe for 1 tilechain
                            # if n in ([n]Hz Δ) is any lower than 0, your computer is
                            # struggling to calculate colors quick enough,
                            # try reducing update_Hz for more accurate music visualisation
                            # note: lifx recommends only sending packets at 50Hz (20ms
                            # per packet) but I'll let you decide if it's worth it
        fade = 20 # in milliseconds
        min_brightness = 1 # default value - 1 (if this is 0 responsiveness might be impacted negatively)
                                   # 65535*0.5 if you want something more bearable on more intense modes
        max_brightness = 65535*1 # default value - 65535
        min_saturation = 65535*0 # default value - 0
        max_saturation = 65535*1 # default value - 65535
        color_temp = 6500 # default: 6500, gnome-NightLight: 4000
        amp_sensitivity = 9 # default: 9 (lower = higher sensitivity, vice versa)
        hue_cycle_duration = 5
        verbose = False

        if (update_Hz < 30):

            print(colorama.Back.RED + colorama.Fore.WHITE + "update_Hz is < 30, enabling automatic fade calculation" + colorama.Style.RESET_ALL)
            sleep(1)

            if (update_Hz >= 1):

                fade = 1000/update_Hz # automatically determine transition duration based on the time between color packets sent to the bulbs (especially makes slower Hz look better)

            else:

                raise ValueError("update_Hz must be greater than or equal to 1!")

        # ---- script ----

        mlifx = lifxtools.ManagedLifx(lifxtools.return_interface(None),verbose=verbose)

        self.lal = lifxtools.LightShow(mlifx,pyaudio,update_Hz,fade,min_brightness=min_brightness,max_brightness=max_brightness,min_saturation=min_saturation,max_saturation=max_saturation,color_temp=color_temp,hue_cycle_duration=hue_cycle_duration,amp_sensitivity=amp_sensitivity)

        self.lal.start()

    def stop(self):

        # self.mlifx.restore()  # restore original state of all managed lights
        self.stream.stop_stream()
        self.stream.close()
        self.pa.terminate()
        print(Style.RESET_ALL)  # reset ansi escapes
