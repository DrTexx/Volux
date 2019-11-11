class UnsupportedFeature:
    def __init__(self):
        pass

class DeviceState:
    def __init__(self,power=None,color=None,infrared=None):
        self.power = power
        self.color = color

class ManagedDevice:
    def __init__(self,device):
        self.device = device
        self.label = device.get_label()
        self.power = device.get_power()
        self.is_light = device.is_light()
        self.supports_color = device.supports_color()

        self.color = None
        # self.temperature = UnsupportedFeature()
        # self.multizone = UnsupportedFeature()
        # self.infrared = UnsupportedFeature()

    def ssave(self):
        """save device state inside of class"""
        self.power = self.device.get_power()

        if (self.supports_color == True): self.color = self.device.get_color()
        elif (self.supports_color == False): self.color = UnsupportedFeature()
        else: raise TypeError("self.supports_color should be a boolean value")

    def sload(self):
        """load device state last saved inside of class"""
        self.device.set_power(self.power)

        if (self.supports_color == True):
            self.device.set_color(self.color)


# class ManagedLight:
#     def __init__(self, _light, debug=False):
#         if debug == True:
#             print("creating a new ManagedLight...")
#         self.light = _light
#         self.power = None
#         self.color = None
#         self.infrared = None
#
#     def ssave(self):
#         """save light state inside of class"""
#         self.power = self.light.get_power()
#         self.color = self.light.get_color()
#         # self.infrared = self.light.get_infrared()
#
#     def sload(self):
#         """load light state last saved inside of class"""
#         self.light.set_color(self.color)
#         self.light.set_power(self.power)
#         # self.light.set_infrared(self.infrared)
#
#     def sexport(self):
#         """export light state to outside class"""
#         return DeviceState(power=self.power,color=self.color,infrared=self.infrared)
#
#     def simport(self,devicestate):
#         """import light state from outside class"""
#         self.power, self.color, self.infrared = devicestate.power, devicestate.color, devicestate.infrared
#
#     def print_saved_state(self):
#         """print the saved state of the light"""
#         print(
#             "[{} (saved)] power:{} color:{} infrared:{}".format(
#                 self.light.get_label(), self.power, self.color, self.infrared
#             )
#         )
