# builtin
import sys
import logging
from time import sleep
import platform
from collections import namedtuple

# site
import volux
import numpy as np
import pyaudio
import colorama

# local
from .hsv2ansi import *
from .lowpass import butter_lowpass_filter

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


vlxaudio_out = namedtuple("vlxaudio_out", ["channels", "lowpasses"])

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
            module_setup=self.setup,
            module_cleanup=self.cleanup,
            shared_modules=shared_modules,
            pollrate=pollrate,
        )
        self._num_channels = 2  # TODO: make configurable
        self._sample_rate = 44100  # TODO: make configurable

    def get(self):

        if self.audio_data == []:

            return float(0)

        else:

            return float(self._get_amplitude())  # 0 .. 100

    # def get_bass(self, freq=60):

    #     if self.audio_data == []:

    #         return float(0)

    #     else:

    #         return 65535

    # TODO: temporary name while testing, needs to be updated once bugs fixed
    def _audio_debug(self):
        # create empty 2D array with list for each channel
        channels = [[] for _ in range(self._num_channels)]

        sample_channel = 0
        for sample in self.audio_data:

            channels[sample_channel].append(sample)

            if sample_channel < self._num_channels - 1:
                sample_channel += 1
            elif sample_channel == self._num_channels - 1:
                sample_channel = 0
            else:
                raise RuntimeError("Bad sample channel during audio splitting")

        # audio data shape:
        # -- [
        # ---------- 0: channel 1 @ t ~ goes from -32,768 .. +32,767
        # ---------- 1: channel 2 @ t ~ goes from -32,768 .. +32,767
        # ---------- 2: channel 1 @ t+1 ~ goes from -32,768 .. +32,767
        # ---------- 3: channel 2 @ t+1 ~ goes from -32,768 .. +32,767
        # -- etc..
        # ------- 2046: channel 1 @ t+? ~ goes from -32,768 .. +32,767
        # ------- 2047: channel 2 @ t+? ~ goes from -32,768 .. +32,767
        # -- ]

        # print(self.audio_data)
        # print(
        #     len(self.audio_data)
        # )  # self.audio_data contains 2^11 items, which translates to a list of 2048 items in the list

        # NOTE: Highest a channel average seems like it would be 1024, reached around 912 with a 20Hz tone at 0db

        channel_averages = []
        for channel in channels:
            # channel_averages.append(np.linalg.norm(channel) / len(channel))
            channel_averages.append(
                np.linalg.norm(channel) / 1024
            )  # TODO: figure out how to derive 1024 eqiv. without checking every time or hard-coding

        channel_lowpasses = []
        for channel in channels:
            lp = butter_lowpass_filter(channel, cutoff=60, fs=44100, order=3)
            channel_lowpasses.append(np.linalg.norm(lp) / 1024)

        return vlxaudio_out(channel_averages, channel_lowpasses)  # 0 .. 1024

    def set(self, new_val):

        log.error("you can't set the audio amplitude!")

    def setup(self):

        self.audio_data = []
        self.pa = (
            self._get_pyaudio()
        )  # note: this is what causes all the spam when creating module
        self.stream = self._open_stream()
        self.sensitivity = 9

    def cleanup(self):

        # self.mlifx.restore()  # restore original state of all managed lights
        self.stream.stop_stream()
        self.stream.close()
        self.pa.terminate()
        # print(colorama.Style.RESET_ALL)  # reset ansi escapes

    def _get_pyaudio(self):

        with volux.SuppressStdoutStderr():

            return pyaudio.PyAudio()

    def _open_stream(self):

        stream = self.pa.open(
            format=pyaudio.paInt16,
            channels=self._num_channels,
            rate=self._sample_rate,
            input=True,
            stream_callback=self._stream_callback,
        )
        return stream

    def _stream_callback(self, in_data, frame_count, time_info, flag):

        audio_data = np.frombuffer(in_data, dtype=np.int16)
        self.audio_data = audio_data

        return (audio_data, pyaudio.paContinue)

    def _get_amplitude(self):
        raw_audio_norm = np.linalg.norm(self.audio_data) / len(self.audio_data)
        adj_audio_norm = raw_audio_norm / 2 ** self.sensitivity
        cla_audio_norm = clamp(
            adj_audio_norm, 0, 1
        )  # normalized audio returning a value between 0 to 1
        return cla_audio_norm * 100  # 0 .. 100
