"""
lifxtools package
"""

print("lifxtools/__init__.py")

from .manageddevice import *
from .virtualdevice import *
from .managedlifx import *
from .managedlight import *
from .managedtilechain import *
from .lightshow import *
from .color_presets import *

# from .message import *
# from .msgtypes import *
# from .unpack import unpack_lifx_message
# from .device import *
# from .light import *
# from .multizonelight import *
# from .group import Group
# from .tilechain import TileChain, Tile
# from .utils import *

# __version__     = '0.0.1'
# __description__ = 'A set of tools for controling LIFX devices on the local network over lan'
# __url__         = 'http://github.com/drtexx/lifxtools'
# __author__      = 'Denver Pallis'
# __license__     = 'GPLv3+'


# imports
from time import sleep, process_time  # used for delays and benchmarking
from lifxlan import LifxLAN, RED, WHITE  # used for controlling lights
from colorsys import rgb_to_hsv, hsv_to_rgb

# settings
num_lights = None  # makes discovery much faster when specified instead of none
live_data = True
debug = True

# decorators
def d_benchmark(func):
    def func_wrapper(*args, **kwargs):
        t1 = process_time()  # take first snapshot of processing time
        result = func(*args, **kwargs)
        t2 = process_time()  # take second snapshot of processing time
        loop_time = t2 - t1
        print(
            "[{}] ({:>3} Hz) took {} seconds to complete!".format(
                func.__name__, int(1 / (loop_time)), loop_time
            )
        )
        return result

    return func_wrapper


def d_debug_messages(func):
    def func_wrapper(*args, **kwargs):
        if debug == True:
            print("[{}] started...".format(func.__name__))
        try:
            return func(*args, **kwargs)
        except Exception as err:
            print("[{}] ERROR!: {}".format(func.__name__, err))
        finally:
            if debug == True:
                print("[{}] finished!".format(func.__name__))

    return func_wrapper


# functions
@d_debug_messages
def return_interface(num_lights):

    if num_lights == None:

        return LifxLAN()

    elif num_lights > 0:

        print(
            "WARNING: num_lights is not None. Make sure it is set to your actual number of devices or you will likely have issues!"
        )
        return LifxLAN(num_lights)

    else:

        raise TypeError("num_lights must be an interger greater than 0")


def return_num_lights(devices):
    if num_lights != None:
        return num_lights
    else:
        return len(devices)


@d_debug_messages
def list_devices(devices):
    i = 0
    for device in devices:
        if debug == True:
            print(
                "devices[{}] = [label='{}', power={}, color={}])".format(
                    i, device.get_label(), device.get_power(), device.get_color()
                )
            )
        i += 1


def blink_devices(devices):
    """ blink all devices found one-by-one """
    for device in devices:
        original_power = device.get_power()

        device.set_power(False, 0.1)
        sleep(0.5)
        device.set_power(True, 0.1)
        sleep(0.5)

        device.set_power(original_power)


def toggle_light(_light):
    light_power = _light.get_power()
    if light_power == 0:
        _light.set_power(True)
        if debug == True:
            print("{} turned on".format(_light.get_label()))
    elif light_power > 0:
        _light.set_power(False)
        if debug == True:
            print("{} turned off".format(_light.get_label()))
    else:
        print(
            "WIP: power other than True or False not currently supported, using 65535 range is not yet implemented"
        )


def set_light_color(_light, color):
    _light.set_color(color)
    if debug == True:
        print("{} color set to {}".format(_light.get_label(), color))


@d_debug_messages
def list_lights(_lights):
    for light in _lights:
        print(
            "[{}] power:{} color:{} infrared:{}".format(
                light.get_label(),
                light.get_power(),
                light.get_color(),
                light.get_infrared(),
            )
        )

def blink_light(_light, delay=1):
    _light.set_power(False, rapid=True)
    sleep(delay)
    _light.set_power(True, rapid=True)


def get_lights(_interface, debug=False):

    try:
        if debug == True:
            print("[ get lights ] started...")
        return _interface.get_lights()

    except:
        if debug == True:
            print("[ get lights ] ERROR!")

    finally:
        if debug == True:
            print("[ get lights ] finished!")


def create_managed_lights(_lights):
    _ManagedLights = []
    for light in _lights:
        _ManagedLights.append(ManagedLight(light))
    return _ManagedLights


def rgbk2hsvk(r, g, b, k):
    """ convert rgb + kelvin to hsvk for bulbs (colors conversion/scaling) """
    h, s, v = rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    h = h * 0xFFFF
    s = s * 0xFFFF
    v = v * 0xFFFF
    k = k
    return (h, s, v, k)

def hsv2rgb(h, s, v):
    r, g, b = hsv_to_rgb(h/65535, s/65535, v/65535)
    return (r, g, b)

def prepare_ManagedLights(_ManagedLights):
    for ml in _ManagedLights:
        ml.ssave()
        ml.light.set_power(True)

def restore_ManagedLights(_ManagedLights):
    for ml in _ManagedLights:
        ml.sload()
