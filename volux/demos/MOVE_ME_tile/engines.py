from random import randint
from math import ceil, floor

from volux.demos.MOVE_ME_tile.parameters import (
    HueParameters,
    SaturationParameters,
    BrightnessParameters,
    KelvinParameters,
)
from volux.demos.MOVE_ME_tile.frame.render_method import (
    FrameRenderMethod,
    FrameRenderMethodSettings,
)
from .types import HSBK
from .util import clamp


class SolidFrameEngine(FrameRenderMethod):
    """Renders a frame where every pixel is the same color."""

    def __init__(self):
        settings = FrameRenderMethodSettings(
            hue=HueParameters(),
            saturation=SaturationParameters(),
            brightness=BrightnessParameters(),
            kelvin=KelvinParameters(),
        )
        super().__init__(settings=settings, func=self._func)

    def _func(self, val):
        return [(0, 65535, (65535 / 100) * val, 3500) for _ in range(64)]


class NoiseFrameEngine(FrameRenderMethod):
    def __init__(self):
        settings = FrameRenderMethodSettings(
            hue=HueParameters(),
            saturation=SaturationParameters(),
            brightness=BrightnessParameters(),
            kelvin=KelvinParameters(),
        )
        super().__init__(settings=settings, func=self._func)

    def _func(self, val):

        max_probability = 10
        """(1 / this) is probability."""
        # make reactive pixels less likely when value is higher
        probability_of_reactive_pixel = int(max_probability * (val / 100))
        # make reactive more likely with more amplitude
        # probability_of_reactive_pixel = int(5 * (100 / clamp(1, val, 100)))

        tile_colors = []

        # HACK: best done with map(), I think.
        for _ in range(64):
            if randint(0, probability_of_reactive_pixel) == 1:
                tile_colors.append(
                    HSBK(
                        (65535 / 1),
                        (65535 / 100) * (randint(80, 100)),
                        (65535 / 100) * val,
                        3500,
                    )
                )
            else:
                tile_colors.append(
                    HSBK(
                        (65535 / 2),
                        (65535 / 100) * (randint(1, 100)),
                        (65535 / 100) * val / 4,
                        3500,
                    )
                )

        print(f"generated a noise frame ({'#' * ceil(val/10):10})")

        return tile_colors
