# builtin
import sys
import logging
from time import sleep
import platform

# site
import volux
import numpy as np
import pyaudio
import colorama

# local
from .hsv2ansi import *

# user_platform = platform.system()
# if user_platform == "Windows":
#     if sys.version_info[0] >= 3:
#         if sys.version_info[1] > 6:
#             raise RuntimeError(
#                 "Due to a requirement (pyaudio) this module only work on Windows with python version >=3.4,<3.7"
#             )

colorama.init()

log = logging.getLogger("voluxaudio")
log.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter and add it to the handlers
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)d"
)
ch.setFormatter(formatter)
# add the handlers to the logger
log.addHandler(ch)


def clamp(value, minv, maxv):

    return max(min(value, maxv), minv)


__requires_python__ = [">=3", "<3.8"]  # required python version


class VoluxAudio(volux.VoluxModule):
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

    def __init__(
        self,
        sensitivity=9,
        shared_modules=[],
        pollrate=None,
        enable_visualiser=False,
        *args,
        **kwargs
    ):
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
            pollrate=pollrate,
        )
        self.pa = (
            self._get_pyaudio()
        )  # note: this is what causes all the spam when creating module
        self.stream = self._open_stream()
        self.sensitivity = 9
        self.audio_data = []

    def get(self):

        return float(self._get_amplitude())  # 0 .. 100

    def set(self, new_val):

        log.error("you can't set the audio amplitude!")

    def _get_pyaudio(self):

        with volux.SuppressStdoutStderr():

            return pyaudio.PyAudio()

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
        cla_audio_norm = clamp(
            adj_audio_norm, 0, 1
        )  # normalized audio returning a value between 0 to 1
        return cla_audio_norm * 100  # 0 .. 100

    def stop(self):

        # self.mlifx.restore()  # restore original state of all managed lights
        self.stream.stop_stream()
        self.stream.close()
        self.pa.terminate()
        print(colorama.Style.RESET_ALL)  # reset ansi escapes
