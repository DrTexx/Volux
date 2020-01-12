"""Allows a user to use a cached version of an input to feed multiple outputs."""

# builtin
from typing import Any

# site
import volux


class VoluxCache(volux.VoluxModule):
    """Volux module for caching a value."""

    def __init__(self, pollrate: int = 1, *args: Any, **kwargs: Any):
        """Instantiate cache module."""
        super().__init__(
            module_name="Volux Cache",
            module_attr="cache",
            module_get=self.get,
            get_type=int,
            get_min=0,
            get_max=100,
            module_set=self.set,
            set_type=int,
            set_min=0,
            set_max=100,
            module_setup=self._setup,
            module_cleanup=self._cleanup,
            shared_modules=[],
            pollrate=pollrate,
        )
        self.cache_val: int = 0

    def get(self) -> int:  # pylint: disable=method-hidden
        """Get cached value."""
        return self.cache_val

    def set(self, new_val: int) -> None:  # pylint: disable=method-hidden
        """Set cached value."""
        self.cache_val = new_val

    def _setup(self) -> None:  # pylint: disable=method-hidden

        pass

    def _cleanup(self) -> None:  # pylint: disable=method-hidden

        pass
