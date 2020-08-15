from typing import List, NamedTuple
from typing_extensions import Protocol


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


class RenderingEngineSettings:
    def __init__(
        self, hue=(), saturation=(), brightness=(), kelvin=(),
    ):
        self.hue = HueParameters(hue)
        self.saturation = SaturationParameters(saturation)
        self.brightness = BrightnessParameters(brightness)
        self.kelvin = KelvinParameters(kelvin)


class FrameRenderFunction(Protocol):
    def __call__(self, val: float,) -> LifxTileFrame:
        ...
