class BarMode:

    def __init__(self,name,color):

        self.name = name
        self.color = color

class VolumeBar:

    def __init__(self):

        # TODO: change colors to be a specific hex value
        self.modes = {
            'volume': BarMode('volume','GREEN'),
            'brightness': BarMode('brightness','BLUE'),
            'muted': BarMode('muted','RED'),
            'unknown': BarMode('unknown','GREY')}

        self.mode = self.modes['volume']

