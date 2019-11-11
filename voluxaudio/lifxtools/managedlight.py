from voluxaudio.lifxtools import DeviceState

class ManagedLight:
    def __init__(self, _light, debug=False):
        if debug == True:
            print("creating a new ManagedLight...")
        self.light = _light
        self.power = None
        self.color = None
        self.infrared = None

    def ssave(self):
        """save light state inside of class"""
        self.power = self.light.get_power()
        self.color = self.light.get_color()
        # self.infrared = self.light.get_infrared()

    def sload(self):
        """load light state last saved inside of class"""
        self.light.set_color(self.color)
        self.light.set_power(self.power)
        # self.light.set_infrared(self.infrared)

    def sexport(self):
        """export light state to outside class"""
        return DeviceState(power=self.power,color=self.color,infrared=self.infrared)

    def simport(self,devicestate):
        """import light state from outside class"""
        self.power, self.color, self.infrared = devicestate.power, devicestate.color, devicestate.infrared

    def print_saved_state(self):
        """print the saved state of the light"""
        print(
            "[{} (saved)] power:{} color:{} infrared:{}".format(
                self.light.get_label(), self.power, self.color, self.infrared
            )
        )
