"""A metamodule for inverting the value of an input based on the inputs min/max output."""

# builtin
from typing import Any

# site
import volux


class VoluxInvert(volux.VoluxModule):
    """Volux module for inverting inputs from 0 to 100."""

    def __init__(
        self,
        pollrate: int = 1,
        min: int = 0,
        max: int = 100,
        *args: Any,
        **kwargs: Any
    ):
        """Instantiate invert module."""
        super().__init__(
            module_name="Volux Invert",
            module_attr="invert",
            module_get=self.get,
            get_type=int,
            get_min=min,
            get_max=max,
            module_set=self.set,
            set_type=int,
            set_min=min,
            set_max=max,
            module_setup=self._setup,
            module_cleanup=self._cleanup,
            shared_modules=[],
            pollrate=pollrate,
        )
        self.val: int = 0

    def get(self) -> int:  # pylint: disable=method-hidden
        """Return the value minus the set_max."""
        return self._set_max - self.val

    def set(self, new_val: int) -> None:  # pylint: disable=method-hidden
        """Store the value for later inversion."""
        self.val = new_val

    def _setup(self) -> None:  # pylint: disable=method-hidden

        pass

    def _cleanup(self) -> None:  # pylint: disable=method-hidden

        pass
