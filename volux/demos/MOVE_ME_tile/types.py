from typing import List, NamedTuple, Callable


class HSBK(NamedTuple):
    hue: int
    saturation: int
    brightness: int
    kelvin: int


LifxTileFrame = List[HSBK]


class FrameRenderFunction:
    Callable[[int], LifxTileFrame]
