import lifxlan
from voluxaudio import lifxtools
from .managedtilechain import ManagedTilechain


class ManagedLifx:
    def __init__(self, lifx, verbose=False, create_managed=True):

        self.lifx = lifx
        self.verbose = verbose

        self.devices, self.lights, self.tilechains, self.multizonelights = [], [], [], []
        self.managed_devices, self.managed_lights, self.managed_tilechains, self.managed_multizonelights = [], [], [], []
        self.device_count, self.light_count, self.tilechain_count = None, None, None

        if self.verbose == True:
            print("discovering LIFX devices...")
        self.refresh_devices(refresh_managed=create_managed)

    # refresh list of devices and (unless specified not to) sort the list accordingly
    def refresh_devices(self, sort=True, refresh_managed=True):

        self.devices = self.lifx.get_devices()

        if sort == True:

            self._sort_devices()

        if refresh_managed == True:

            self.remanage_devices()

    def remanage_devices(self):

        self._refresh_managed_devices()
        self._refresh_managed_lights()
        self._refresh_managed_tilechains()

    def _refresh_managed_devices(self):

        self.managed_devices = []

        for device in self.devices:

            self.managed_devices.append(lifxtools.ManagedDevice(device))

    def _refresh_managed_lights(self):

        self.managed_lights = []

        for light in self.lights:

            self.managed_lights.append(lifxtools.ManagedLight(light))

    def _refresh_managed_tilechains(self):

        self.managed_tilechains = []

        for tilechain in self.tilechains:

            self.managed_tilechains.append(ManagedTilechain(tilechain))

    def _refresh_managed_multizonelights(self):

        self.managed_multizonelights = []

        for device in self.managed_devices:
            if type(device) == lifxlan.MultiZoneLight:
                self.managed_multizonelights.append(device)

    def print_device_labels(self):

        for device in self.devices:

            print(device.get_label())

    # put devices in respective lists, e.g. TileChain types in .tilechains, etc.
    def _sort_devices(self, get_counts=True):

        for device in self.devices:

            device_type = type(device)

            if device_type == lifxlan.light.Light:

                self.lights.append(device)

            elif device_type == lifxlan.tilechain.TileChain:

                self.tilechains.append(device)

            elif device_type == lifxlan.multizonelight.MultiZoneLight:

                self.multizonelights.append(device)

            else:

                raise TypeError(
                    "type of",
                    device.get_label(),
                    "is",
                    device_type,
                    "and we don't recognize it!",
                )

        if self.verbose == True:
            print("finished sorting devices!")
        if self.verbose == True:
            self.print_sorted_lists()

        if get_counts == True:
            self._get_device_counts()

    def print_sorted_lists(self):

        print("devices", self.devices)
        print("lights", self.lights)
        print("tilechains", self.tilechains)

    def _get_device_counts(self):

        self.device_count = len(self.devices)
        self.light_count = len(self.lights)
        self.tilechain_count = len(self.tilechains)

    def add_device(self,new_device):

        self.devices.append(new_device)
        self.managed_devices.append(lifxtools.ManagedDevice(new_device))

    def prepare(self):

        for mlight in self.managed_lights:

            mlight.ssave()
            mlight.light.set_power(True)

        for mtilechain in self.managed_tilechains:

            mtilechain.ssave()
            mtilechain.TileChain.set_power(True)

    def restore(self):

        for mlight in self.managed_lights:

            mlight.sload()

        for mtilechain in self.managed_tilechains:

            mtilechain.sload()
