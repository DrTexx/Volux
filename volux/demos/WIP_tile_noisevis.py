#!/usr/bin/env python3

import lifxlan
import time
import voluxaudio

from volux.demos.MOVE_ME_tile.engines import NoiseFrameEngine

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


nfe = NoiseFrameEngine()

lifx = lifxlan.LifxLAN()

tilechains = lifx.get_tilechain_lights()

min_pixels = 0
max_pixels = 64
n_pixels = min_pixels
tilechains_tiles_colors = [
    tile.get_tile_colors(idx) for idx, tile in enumerate(tilechains)
]
print(tilechains_tiles_colors)

try:

    while True:

        if n_pixels > max_pixels:
            n_pixels = min_pixels

        # print(f"tile_colors[0][0]: {tile_colors[0][0]}")
        cur_amp = vlxaudio.get()
        max_probability = 10
        """(1 / this) is probability."""
        probability_of_reactive_pixel = int(
            max_probability * (cur_amp / 100)
        )  # make reactive less likely with more amplitude
        # probability_of_reactive_pixel = int(
        #     5 * (100 / clamp(1, cur_amp, 100))
        # )  # make reactive more likely with more amplitude
        for tc_idx, tilechain in enumerate(tilechains_tiles_colors):
            for t_idx, tile in enumerate(tilechains):
                tilechains_tiles_colors[tc_idx][t_idx] = nfe.render(cur_amp)

        for tc_idx, tilechain in enumerate(tilechains_tiles_colors):
            for t_idx, tile in enumerate(tilechains):
                tile.set_tile_colors(
                    0, tilechains_tiles_colors[tc_idx][t_idx], rapid=True
                )

        n_pixels += 1

        time.sleep(1 / 60)

except KeyboardInterrupt:
    pass

vlxaudio.cleanup()
