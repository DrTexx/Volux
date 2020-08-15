from random import randint
from math import ceil, floor

from .types import (
    HueParameters,
    SaturationParameters,
    BrightnessParameters,
    KelvinParameters,
)
from .engine.frame import (
    FrameEngine,
    RenderingEngineSettings,
)
from .engine.motion import MotionEngine
from .types import HSBK
from .util import clamp


class SolidFrameEngine(FrameEngine):
    """Renders a frame where every pixel is the same color."""

    def __init__(self):
        settings = RenderingEngineSettings(
            hue=HueParameters(),
            saturation=SaturationParameters(),
            brightness=BrightnessParameters(),
            kelvin=KelvinParameters(),
        )
        super().__init__(settings=settings, render_func=self._func)

    def _func(self, val, settings):
        print("settings not respected yet.")
        return [(0, 65535, (65535 / 100) * val, 3500) for _ in range(64)]
        # for idx, pixel in enumerate(self.frame):
        #     if idx % 2 == 0:
        #         self.frame[idx] = (
        #             (65535 / 1),
        #             65535,
        #             (65535 / 100) * (val / 100),
        #             6500,
        #         )
        #     else:
        #         if randint(0, 1) == 0:
        #             self.frame[idx] = (
        #                 (65535 / 2),
        #                 65535,
        #                 (65535 / 50) * (val / 2),
        #                 6500,
        #             )
        #         else:
        #             self.frame[idx] = (
        #                 (65535 / 3),
        #                 65535,
        #                 (65535 / 50) * (val / 2),
        #                 6500,
        #             )

        return self.frame


class NoiseFrameEngine(FrameEngine):
    def __init__(self):
        settings = RenderingEngineSettings(
            hue=HueParameters(),
            saturation=SaturationParameters(),
            brightness=BrightnessParameters(),
            kelvin=KelvinParameters(),
        )
        super().__init__(settings=settings, render_func=self._func)

    # TODO: settings not respected yet.
    def _func(self, val, settings):

        max_probability = 10
        """(1 / this) is probability."""
        # make reactive pixels less likely when value is higher
        probability_of_reactive_pixel = int(max_probability * (val / 100))
        # make reactive more likely with more amplitude
        # probability_of_reactive_pixel = int(
        #     max_probability * (100 / clamp(1, val, 100))
        # )
        # print(f"reactivity probability: 1 / {probability_of_reactive_pixel}")

        tile_colors = []

        # HACK: best done with map(), I think.
        for _ in range(64):
            if randint(0, probability_of_reactive_pixel) == 1:
                tile_colors.append(
                    HSBK(
                        (65535 / 1),
                        (65535 / 100) * (randint(80, 100)),
                        (65535 / 100) * val,
                        6500,
                    )
                )
            else:
                tile_colors.append(
                    HSBK(
                        (65535 / 2),
                        (65535 / 100) * (randint(90, 100)),
                        # (65535 / 100) * val / 10,
                        # (65535 / 100) * (19 + (31 / max(1, val))),
                        (65535 / 100) * (1 + (19 / max(1, val))),
                        6500,
                    )
                )

        # print(f"generated a noise frame ({'#' * ceil(val/10):10})")

        return tile_colors


class SplashMotionEngine(MotionEngine):
    def __init__(self):
        raise NotImplementedError("Splash Motion Engine not yet implemented.")


class NorthernMotionEngine(MotionEngine):
    """Northern Lights. Bottom Text.

    Paint the first pixel of the tile with a val-based hue and brightness, produces a trail that runs down the entire tile and slowly fades away.

    The higher the val, the longer the pixel takes to fade away while trailing down the tile.
    """

    def __init__(self):
        super().__init__(
            render_func=self._render_func, settings=RenderingEngineSettings()
        )
        self.frame = [(0, 65535, (65535 / 100) * 10, 3500) for _ in range(64)]

    def _render_func(self, val, settings: RenderingEngineSettings):
        # print("settings not respected yet.")
        for idx, pixel in enumerate(self.frame):
            # if pixel[1] >= 65535:
            # else:
            #     self.frame[idx][1] += 1
            self.frame[-1] = (
                randint(int((65535 / 100) * val), int((65535 / 100) * val)),
                # 65535 / 2,
                65535,
                # randint(int((65535 / 100) * val), int((65535 / 100) * val)),
                (65535 / 100) * val,
                3500,
            )
            self.frame[idx - 1] = (
                self.frame[idx][0],
                # (self.frame[idx][0] - 100) % 65535,
                # self.frame[idx][1],
                max(0, self.frame[idx][1] - 400),
                # self.frame[idx][2],
                max(0, self.frame[idx][2] - 800),
                self.frame[idx][3],
            )

        # print(f"shifted {'#' * int((val / 10))}")

        return self.frame
