class UnsupportedFeature:
    def __init__(self):
        pass


class DeviceState:
    def __init__(self, power=None, color=None, infrared=None):
        self.power = power
        self.color = color


class ManagedDevice:
    def __init__(self, device):
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

        if self.supports_color is True:
            self.color = self.device.get_color()
        elif self.supports_color is False:
            self.color = UnsupportedFeature()
        else:
            raise TypeError("self.supports_color should be a boolean value")

    def sload(self):
        """load device state last saved inside of class"""
        self.device.set_power(self.power)

        if self.supports_color is True:
            self.device.set_color(self.color)

    def simport(self, devicestate):

        raise NotImplementedError()

    def sexport(self):

        raise NotImplementedError()
