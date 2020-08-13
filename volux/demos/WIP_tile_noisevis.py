#!/usr/bin/env python3

import lifxlan
import time
import voluxaudio
from random import randint

vlxaudio = voluxaudio.VoluxAudio()
vlxaudio.setup()


def engage_x_pixels(x, _max=64):
    """Return a list of 64 HSVK tuples. Turn on x many pixels of tile."""
    HSVK_normal = (0, 0, (65535 / 100) * vlxaudio.get(), 3500)
    HSVK_it_off = (0, 65535, 10000, 3500)

    def _func(i):
        if i <= x:
            return HSVK_normal
        else:
            return HSVK_it_off

    return map(_func, range(_max))


# HACK: quick and dirty implementation
def mutate_pixel(n, new_color, all_colors):
    """Change only the color of pixel n of tile."""
    all_colors[n] = new_color
    return all_colors


lifx = lifxlan.LifxLAN()

tiles = lifx.get_tilechain_lights()

min_pixels = 0
max_pixels = 64
n_pixels = min_pixels
tile_colors = [tile.get_tile_colors(0) for tile in tiles]
print(tile_colors)

try:

    while True:

        if n_pixels > max_pixels:
            n_pixels = min_pixels

        # print(f"tile_colors[0][0]: {tile_colors[0][0]}")
        for i in range(64):
            if randint(0, 1) == 1:
                tile_colors[0][0][i] = (
                    0,
                    0,
                    (65535 / 100) * vlxaudio.get(),
                    3500,
                )
            else:
                tile_colors[0][0][i] = (0, 0, 0, 3500)

        for tile in tiles:
            print(f"setting {n_pixels} pixels")
            # print(f"tile colors: {tile_colors[0][0]}")
            tile.set_tile_colors(
                0, tile_colors[0][0], rapid=True,
            )

        n_pixels += 1

        time.sleep(1 / 20)

except KeyboardInterrupt:
    pass

vlxaudio.cleanup()
