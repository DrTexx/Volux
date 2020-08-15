from typing import List, NamedTuple, Callable


class HSBK(NamedTuple):
    hue: int
    saturation: int
    brightness: int
    kelvin: int


LifxTileFrame = List[HSBK]


class HueParameters:
    def __init__(self, _min=0, _max=65535):
        self._min = _min
        self._max = _max


class SaturationParameters:
    def __init__(self, _min=0, _max=65535):
        self._min = _min
        self._max = _max


class BrightnessParameters:
    def __init__(self, _min=0, _max=65535):
        self._min = _min
        self._max = _max


class KelvinParameters:
    def __init__(self, _min=0, _max=65535):
        self._min = _min
        self._max = _max
