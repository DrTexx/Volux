"""Defines the voluxlight module."""

# builtin
import logging
from typing import Any, Dict, List, Union, Tuple

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
    """Volux module for managing lifx lights."""

    def __init__(
        self,
        instance_label: str,
        init_mode: str,
        init_mode_args: Dict[Any, Any] = {},
        shared_modules: List[volux.VoluxModule] = [],
        pollrate: int = 0,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """See class docstring."""
        super().__init__(
            module_name="Volux Light ({})".format(instance_label),
            module_attr="light_{}".format(instance_label),
            module_get=self._get,
            get_type=float,
            get_min=0,
            get_max=100,
            module_set=self._set,
            set_type=float,
            set_min=0,
            set_max=100,
            module_setup=self.setup,
            module_cleanup=self.cleanup,
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
                if isinstance(self.init_mode_args, dict):
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

    def _get(self):

        for mdevice in self.mdevices:

            color = mdevice.device.get_color()
            power = int(color[2] / 65535)
            return power * 100

    def _set(
        self, new_val: Union[int, float, Tuple[int, int, int, int]]
    ) -> None:

        print(f"new_val: {new_val} ({type(new_val)})")

        if isinstance(new_val, float) or isinstance(new_val, int):

            if new_val < self._set_min:
                new_val = self._set_min

            elif new_val > self._set_max:
                new_val = self._set_max

            for mdevice in self.mdevices:

                color = mdevice.device.get_color()
                new_color = (
                    color[0],
                    color[1],
                    (new_val / self._set_max) * 65535,
                    color[3],
                )
                mdevice.device.set_color(new_color)

        elif isinstance(new_val, tuple):

            self.set_color(
                new_val, duration=50, rapid=True
            )  # this directly correlates with how long a beat must be at max volume to achieve max color intensitiy

        else:

            raise TypeError("input for set must be int, float or HSBK tuple")

    def setup(self) -> None:
        """Tasks for setup."""
        for mdevice in self.mdevices:
            mdevice.ssave()

    def cleanup(self) -> None:
        """Tasks for cleanup."""
        for mdevice in self.mdevices:
            mdevice.sload()

    def set_color(
        self,
        new_color: Tuple[int, int, int, int],
        duration: int = 20,
        rapid: bool = True,
    ) -> None:
        """Set device colour."""
        for mdevice in self.mdevices:

            mdevice.device.set_color(new_color, duration=duration, rapid=rapid)

    def toggle(self) -> None:
        """Toggle power of light."""
        for mdevice in self.mdevices:

            power = mdevice.device.get_power()
            mdevice.device.set_power(
                not power
            )  # not ideal behaviour if all lights in different states

    # def prepare(self) -> None:
    #     """Prepare the light."""
    #     for mdevice in self.mdevices:
    #         mdevice.ssave()

    # def restore(self) -> None:
    #     """Restore the original light state."""
    #     for mdevice in self.mdevices:
    #         mdevice.sload()
