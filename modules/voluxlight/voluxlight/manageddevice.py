"""Defines manageddevice class for lights and related classes."""

from typing import Union, Tuple
import lifxlan


class UnsupportedFeature:
    """Class to represent unsupported features of lights."""

    def __init__(self) -> None:
        """See class docstring."""
        pass


class DeviceState:
    """Class to represent a light's exported state."""

    def __init__(
        self,
        power: Union[None, bool] = None,
        color: Union[None, Tuple[int, int, int, int]] = None,
    ) -> None:
        """See class docstring."""
        self.power = power
        self.color = color


class ManagedDevice:
    """Class to help work with lifx devices."""

    def __init__(self, device: lifxlan.Device) -> None:
        """See class docstring."""
        self.device = device
        self.label = device.get_label()
        self.power = device.get_power()
        self.is_light = device.is_light()
        self.supports_color = device.supports_color()

        self.color: Union[
            None, Tuple[int, int, int, int], UnsupportedFeature
        ] = None
        # self.temperature = UnsupportedFeature()
        # self.multizone = UnsupportedFeature()

    def ssave(self) -> None:
        """Save device state inside of class."""
        self.power = self.device.get_power()

        if self.supports_color is True:
            self.color = self.device.get_color()
        elif self.supports_color is False:
            self.color = UnsupportedFeature()
        else:
            raise TypeError("self.supports_color should be a boolean value")

    def sload(self) -> None:
        """Load device state last saved inside of class."""
        self.device.set_power(self.power)

        if self.supports_color is True:
            self.device.set_color(self.color)

    def simport(self, devicestate: DeviceState) -> None:
        """Use an instance of DeviceState to alter light state."""
        raise NotImplementedError()

    def sexport(self) -> None:
        """Export an instance of DeviceState for later importing."""
        raise NotImplementedError()
