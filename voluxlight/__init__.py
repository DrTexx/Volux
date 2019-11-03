from volux import VoluxModule
import lifxlan


class VoluxLight(VoluxModule):
    def __init__(self,device_name,*args,**kwargs):
        super().__init__(module_name="Volux Light",module_attr="light", module_get=self.get, module_set=self.set)
        self.device_name = device_name

        self.lifx = lifxlan.LifxLAN(None)
        self.device = self.lifx.get_device_by_name(self.device_name)

    def get(self):

        color = self.device.get_color()
        power = color[2]/65535
        return power*100

    def set(self,new_val):

        if new_val < 0: new_val = 0
        elif new_val > 100: new_val = 100

        new_val = new_val/100

        color = self.device.get_color()
        new_color = (color[0], color[1], new_val*65535, color[3])

        self.device.set_color(new_color)

    def toggle(self):

        power = self.device.get_power()
        self.device.set_power(not power)
