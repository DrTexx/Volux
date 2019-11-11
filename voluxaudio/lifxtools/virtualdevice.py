class VirtualDevice:
    def __init__(self, label="Virtual Device", power=True, color=(0,0,65535,6500), is_light=True, supports_color=True):
        self._label = label
        self._power = power
        self._color = color
        self._is_light = is_light
        self._supports_color = supports_color

    def get_label(self):
        return self._label

    def get_power(self):
        return self._power

    def is_light(self):
        return self._is_light

    def supports_color(self):
        return self._supports_color

    def set_power(self,new_power_state):
        self._power = new_power_state
        print("new power state for [{}]: {}".format(self.get_label(),self._power))

    def set_color(self,HSVK_tuple):
        self._color = HSVK_tuple
        print("new color for [{}]: {}".format(self.get_label(),self._color))

    def get_color(self):
        return self._color
