"""Allows a user to use a cached version of an input to feed multiple outputs."""

# site
import volux


class VoluxCache(volux.VoluxModule):
    """Volux module for caching a value."""

    def __init__(self, *args, **kwargs):
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
            pollrate=None,
        )
        self.cache_val = 0

    def get(self):  # pylint: disable=method-hidden
        """Get cached value."""
        return self.cache_val

    def set(self, new_val):  # pylint: disable=method-hidden
        """Set cached value."""
        self.cache_val = new_val

    def _setup(self):  # pylint: disable=method-hidden

        pass

    def _cleanup(self):  # pylint: disable=method-hidden

        pass
