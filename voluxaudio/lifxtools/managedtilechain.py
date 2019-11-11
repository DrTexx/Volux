import numpy as np
import lifxlan

# ---- classes ----
class HSVKPixel:
    def __init__(self, hsvk_tuple):

        self.h, self.s, self.v, self.k = hsvk_tuple

    def write(self, hsvk_tuple):

        self.h, self.s, self.v, self.k = hsvk_tuple

    def read(self):

        return (self.h, self.s, self.v, self.k)


class ManagedTilechain:
    def __init__(self, TileChain_Object):
        self.TileChain = TileChain_Object
        self.size = TileChain_Object.get_canvas_dimensions()
        self.size_all_values = (self.size[0], self.size[1], 4)
        self.num_tiles = TileChain_Object.get_tile_count()
        self.num_pixels = ((self.size[0] + 1) * (self.size[1] + 1) * 4) - 1
        self.off_pixel = (0, 0, 0, 6500)
        self.canvas = self._gen_empty_frame()

        self.power = None
        self.color = None

    def _gen_empty_frame(self):

        empty_frame = np.full(self.size_all_values, self.off_pixel, dtype=object)

        return empty_frame

    def read_HSVK_2D(self):

        HSVK_list = []

        # for each cell of self.canvas
        for y in self.canvas:
            for x in y:
                # store the output of cell.read() in 1D array
                HSVK_list.append(x)

        # convert the 1D array to 2D (the third dimension is HSVK data)
        HSVK_2D = np.reshape(HSVK_list, (self.size[0], self.size[1], 4))

        return HSVK_2D

    def read_HSVK_tiles(self):

        # convert the 1D array to a 2D array of 64 pixels per tile
        HSVK_tiles = np.reshape(self.canvas, (self.num_tiles, 64, 4))

        return HSVK_tiles

    def print_HSVK_2D(self):

        # print data relating to each pixel in the HSVK_2D array
        HSVK_2D = self.read_HSVK_2D()
        n = 0
        for y in range(len(HSVK_2D)):
            for x in range(len(HSVK_2D[y])):
                print(
                    "pixel:{} x-index:{} y-index:{} color:{}".format(
                        n, x, y, HSVK_2D[y][x]
                    )
                )
                n += 1

    def print_HSVK_tiles(self):

        # print 2D tile pixels array
        HSVK_tiles = self.read_HSVK_tiles()
        for tile in range(len(HSVK_tiles)):
            for pixel in range(len(HSVK_tiles[tile])):
                print(
                    "tile:{} pixel:{} HSVK:{}".format(
                        tile, pixel, HSVK_tiles[tile][pixel]
                    )
                )

    def update_tilechain(self, fade=0, rapid=True):

        HSVK_tiles = self.read_HSVK_tiles()
        self.TileChain.set_tilechain_colors(HSVK_tiles, fade, rapid=rapid)

    def paint_pixel(self, color, x, y):

        self.canvas[y][x] = color

    def paint_line(self, color, dimension, index):

        if dimension == "x":
            for x in range(self.size[0]):
                self.canvas[index][x] = color

        elif dimension == "y":
            for y in range(len(self.canvas)):
                self.canvas[y][index] = color

        else:
            raise Exception(
                "dimension must be either the string 'x' or 'y', not {}".format(
                    str(dimension)
                )
            )

    def ssave(self):

        self.power = self.TileChain.get_power()
        self.tilechain_colors = self.TileChain.get_tilechain_colors()

    def sload(self):

        self.TileChain.set_power(self.power)
        self.TileChain.set_tilechain_colors(self.tilechain_colors)


# ---- script ----
if __name__ == "__main__":
    lifx = lifxlan.LifxLAN()
    tilechains = lifx.get_tilechain_lights()
    tilechain = tilechains[0]

    my_mtc = ManagedTilechain(tilechain)
    HSVK_list = my_mtc.read_HSVK_2D()
    print(HSVK_list)

    tilechain.set_tilechain_colors(HSVK_list, 0, rapid=True)
