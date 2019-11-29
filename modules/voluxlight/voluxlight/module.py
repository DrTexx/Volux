# builtin
import logging

# site
import volux
import lifxlan

# package
from .manageddevice import ManagedDevice

log = logging.getLogger("voluxlight")
log.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter and add it to the handlers
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
ch.setFormatter(formatter)
# add the handlers to the logger
log.addHandler(ch)


class VoluxLight(volux.VoluxModule):
    def __init__(
        self,
        instance_label,
        init_mode,
        init_mode_args={},
        group=None,
        shared_modules=[],
        pollrate=None,
        *args,
        **kwargs
    ):
        super().__init__(
            module_name="Volux Light ({})".format(instance_label),
            module_attr="light_{}".format(instance_label),
            module_get=self.get,
            get_type=float,
            get_min=0,
            get_max=100,
            module_set=self.set,
            set_type=float,
            set_min=0,
            set_max=100,
            shared_modules=shared_modules,
            pollrate=pollrate,
        )
        init_mode_options = [
            "all_devices",
            "device",
            "group",
        ]  # note: all types of labels are case-sensitive
        self.instance_label = instance_label
        self.init_mode = init_mode
        self.init_mode_args = init_mode_args
        # self.group = group  # note: group labels are caps sensitive

        self.lifx = lifxlan.LifxLAN(None)

        self.devices = []

        if self.init_mode not in init_mode_options:
            raise ValueError(
                "invalid init_mode. options include: {}".format(
                    init_mode_options
                )
            )
        else:
            if self.init_mode == "all_devices":
                self.devices = self.lifx.get_devices()

            elif self.init_mode == "device":
                if type(self.init_mode_args) == dict:
                    if (
                        "ip" in self.init_mode_args
                        and "mac" in self.init_mode_args
                    ):
                        raise NotImplementedError()  # note: implement ip + mac option
                    elif "label" in self.init_mode_args:
                        self.devices.append(
                            self.lifx.get_device_by_name(
                                self.init_mode_args["label"]
                            )
                        )
                    else:
                        raise KeyError("'label' not specified in mode_args")
                else:
                    raise TypeError("init_mode_args must be of type 'dict'")

            elif self.init_mode == "group":
                if "group_label" in self.init_mode_args:
                    devices = self.lifx.get_devices_by_group(
                        self.init_mode_args["group_label"]
                    ).devices
                    if len(devices) > 0:
                        self.devices = devices
                    else:
                        raise Exception(
                            "no devices found for group_label {}! Please note group_label is caps-sensitive!".format(
                                self.init_mode_args["group_label"]
                            )
                        )
                else:
                    raise KeyError("'group_label' not specified in mode_args")

        # if not self.group is None:
        #     for device in self.devices:
        #         if not device.get_group_label() == self.group:
        #             device.set_power(False)
        #             self.devices.remove(device)
        #             print("removed '{}' from selected devices because it's not in group '{}'".format(device.get_label(),self.group))
        if len(self.devices) > 0:
            for device in self.devices:
                if device is not None:
                    device.set_power(True)
                else:
                    raise Exception(
                        "No lights with specified conditions found!"
                    )
        else:
            raise Exception("No lights with specified conditions found!")

        log.debug("devices: {}".format(self.devices))
        self.mdevices = [ManagedDevice(device) for device in self.devices]

    def get(self):

        for device in self.devices:

            color = device.get_color()
            power = color[2] / 65535
            return power * 100

    def set(self, new_val):

        # print("new_val: {} ({})".format(new_val,type(new_val)))

        input_type = type(new_val)

        if input_type == float or input_type == int:

            if new_val < self._set_min:
                new_val = self._set_min

            elif new_val > self._set_max:
                new_val = self._set_max

            for device in self.devices:

                color = device.get_color()
                new_color = (
                    color[0],
                    color[1],
                    (new_val / self._set_max) * 65535,
                    color[3],
                )
                device.set_color(new_color)

        elif input_type == tuple:

            self.set_color(new_val, rapid=True)

        else:

            raise TypeError("input for set must be int, float or HSBK tuple")

    def set_color(self, new_color, duration=20, rapid=True):

        for device in self.devices:

            device.set_color(new_color, duration=duration, rapid=rapid)

    def toggle(self):

        for device in self.devices:

            power = device.get_power()
            device.set_power(
                not power
            )  # not ideal behaviour if all lights in different states

    def prepare(self):

        [mdevice.ssave() for mdevice in self.mdevices]

    def restore(self):

        [mdevice.sload() for mdevice in self.mdevices]
