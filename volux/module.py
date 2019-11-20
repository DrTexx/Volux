import uuid
import colorama
import logging

colorama.init()

log = logging.getLogger("volux module")
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


class VoluxModule:
    """Provides common metadata for every Volux module. All modules (including core) are a subclass of VoluxModule"""

    def __init__(
        self,
        module_name,
        module_attr,
        module_get,
        get_type,
        get_min,
        get_max,
        module_set,
        set_type,
        set_min,
        set_max,
        shared_modules,
        pollrate,
    ):

        if not type(shared_modules) == list:
            raise TypeError(
                "VoluxModule: kwarg 'shared_modules' must be of type list"
            )

        self.UUID = uuid.uuid4()
        self._module_name = module_name
        self._module_attr = module_attr
        self.get = module_get
        self._get_type = get_type
        self._get_min = get_min
        self._get_max = get_max
        self.set = module_set
        self._set_type = set_type
        self._set_min = set_min
        self._set_max = set_max
        self._shared_modules = shared_modules
        self._pollrate = (
            pollrate
        )  # todo: change this to be an optional module limit (a max polling rate the module is capable of)

    def _loaded(self):
        log.debug(
            "loaded module: {} (pollrate={}) [{color_UUID}{UUID}{color_reset}]".format(
                self._module_name,
                self._pollrate,
                color_UUID=colorama.Fore.GREEN,
                UUID=self.UUID,
                color_reset=colorama.Style.RESET_ALL,
            )
        )

    def get_module_info(self):
        return {"name": self._module_name, "attr": self._module_attr}
