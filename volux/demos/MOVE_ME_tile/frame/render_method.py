from typing import Callable

from ..parameters import (
    HueParameters,
    SaturationParameters,
    BrightnessParameters,
    KelvinParameters,
)
from ..types import LifxTileFrame


class FrameRenderMethodSettings:
    def __init__(
        self,
        hue: HueParameters,
        saturation: SaturationParameters,
        brightness: BrightnessParameters,
        kelvin: KelvinParameters,
    ):
        self.hue = hue
        self.saturation = saturation
        self.brightness = brightness
        self.kelvin = kelvin


class FrameRenderMethod:
    """Generic interface for frame rendering methods."""

    def __init__(
        self,
        settings: FrameRenderMethodSettings,
        func: Callable[[int], LifxTileFrame],
    ):
        self.settings = settings
        self._render_func = func

    def render(self, value) -> LifxTileFrame:
        return self._render_func(value)


# def gen_pixel(float) -> HSBK:
#     return HSBK(10, 10, 10, 10)


# def get_frame(pixel: HSBK) -> LifxTileFrame:
#     repeat = [pixel for _ in range(64)]
#     return repeat


# pixel = gen_pixel(1.0)
# frame = get_frame(pixel)
