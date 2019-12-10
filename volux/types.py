class HSBK:
    def __init__(self, hue, saturation, brightness, kelvin, *args, **kwargs):
        # pass tests for value ranges

        # set values
        self.h = hue
        self.s = saturation
        self.b = brightness
        self.k = kelvin

    def __repr__(self):

        return [self.h, self.s, self.b, self.k]
