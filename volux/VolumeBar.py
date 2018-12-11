class BarMode:
    def __init__(self,name,color):
        self.name = name
        self.color = color
class VolumeBar:
    def __init__(self):
        self.modes = {
            'volume': BarMode('volume','GREEN'),
            'brightness': BarMode('brightness','BLUE'),
            'muted': BarMode('muted','RED'),
            'unknown': BarMode('unknown','GREY')}
        self.mode = self.modes['volume']
