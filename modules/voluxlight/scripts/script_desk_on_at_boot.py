# builtin
import time
import threading
from datetime import datetime

# site
import voluxlight

COLORS = {
    "default_day": (0, 0, 65535 * 0, 5000),
    "default_night": (0, 0, 65535 * 0.50, 3500),
    "off": (0, 0, 0, 6500),
    "ultra_soft_white": (0, 0, 1, 6500),
    "soft_daylight_30": (0, 0, 65535 * 0.30, 5000),
    "elec_blue": (29854, 56360, 65535 * 0.25, 6500),
    "soft_deep_red": (0, 65535, 65535 * 0.25, 6500),
}


def set_light_as_thread(light, color, pause_seconds=1, transition_seconds=1):

    og_color = light.get_color()
    og_color_soft = (og_color[0], og_color[1], 65535 * 0.10, og_color[3])
    light.set_color(og_color_soft, duration=100, rapid=True)
    print("dimmed '{}'".format(light.get_label()))
    time.sleep(0.100)

    for i in range(3):
        light.set_power(True, rapid=True)
    print("turned on '{}'".format(light.get_label()))
    time.sleep(pause_seconds)

    print("set color on '{}'".format(light.get_label()))
    light.set_color(color, duration=transition_seconds * 1000, rapid=True)


lights = voluxlight.search_until_found(
    ["Demo Bulb", "Strip", "Office Ceiling"], attempts=10
)


threads = []
hour = datetime.now().hour

for light in lights:

    light_label = light.get_label()

    if light_label == "Demo Bulb":

        color = COLORS["elec_blue"]

    elif light_label == "Strip":

        color = COLORS["soft_daylight_30"]

    elif light_label == "Bedroom Ceiling":

        color = COLORS["off"]

    else:

        if hour >= 19 or hour <= 6:

            color = COLORS["default_night"]

        else:

            color = COLORS["default_day"]

    threading.Thread(target=set_light_as_thread, args=(light, color)).start()
