"""Base class for creating derived module classes."""

import uuid
import colorama
import logging
from typing import Dict, Callable
from uuid import UUID

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
    """Provides common metadata for every Volux module. All modules (including core) are a subclass of VoluxModule."""

    def __init__(
        self,
        module_name: str,
        module_attr: str,
        module_get: Callable,
        get_type: type,
        get_min: int,
        get_max: int,
        module_set: Callable,
        set_type: type,
        set_min: int,
        set_max: int,
        module_setup: Callable,
        module_cleanup: Callable,
        shared_modules: list,
        pollrate: int,
    ):
        """Do not instansiate this class directly. It should always be used as a base for a derived module class."""
        if not type(shared_modules) == list:
            raise TypeError(
                "VoluxModule: kwarg 'shared_modules' must be of type list"
            )

        self.UUID: UUID = uuid.uuid4()
        self._module_name: str = module_name
        self._module_attr: str = module_attr
        self.get: Callable = module_get
        self._get_type: type = get_type
        self._get_min: int = get_min
        self._get_max: int = get_max
        self.set: Callable = module_set
        self._set_type: type = set_type
        self._set_min: int = set_min
        self._set_max: int = set_max
        self._setup: Callable = module_setup
        self._cleanup: Callable = module_cleanup
        self._shared_modules: list = shared_modules
        self._pollrate: int = pollrate  # todo: change this to be an optional module limit (a max polling rate the module is capable of)

    def _loaded(self) -> None:
        log.debug(
            "loaded module: {} (pollrate={}) [{color_UUID}{UUID}{color_reset}]".format(
                self._module_name,
                self._pollrate,
                color_UUID=colorama.Fore.GREEN,
                UUID=self.UUID,
                color_reset=colorama.Style.RESET_ALL,
            )
        )

    def get_module_info(self) -> Dict[str, str]:
        """Return information about the module."""
        return {"name": self._module_name, "attr": self._module_attr}
