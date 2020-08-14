from typing import Tuple, List, NamedTuple


class HSBK(NamedTuple):
    hue: int
    saturation: int
    brightness: int
    kelvin: int


LifxTileFrame = List[HSBK]
