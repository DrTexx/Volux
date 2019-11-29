# builtin
import logging

# site
import lifxlan

log = logging.getLogger("voluxlight - get all lights")
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


def get_all_lights():
    log.info("discovering LIFX devices on network...")
    lifx = lifxlan.LifxLAN(None)
    devices = lifx.get_devices()
    log.info("finished LIFX device discovery")
    log.debug("LIFX devices found: {}".format(devices))
    return devices
