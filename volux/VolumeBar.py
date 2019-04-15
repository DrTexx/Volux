class BarMode:

    def __init__(self,name,style_id):

        self.name = name
        self.style_id = style_id

class VolumeBar:

    def __init__(self):

        # TODO: change colors to be a specific hex value
        self.modes = {
            'volume': BarMode('volume',"volume.TFrame"),
            'brightness': BarMode('brightness',"brightness.TFrame"),
            'muted': BarMode('muted',"muted.TFrame"),
            'unknown': BarMode('unknown',"unknown.TFrame")}

        self.mode = self.modes['volume']
