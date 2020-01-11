"""Volux module for printing messages to the CLI."""

import volux


class VoluxCliPrint(volux.VoluxModule):
    """Volux module for printing a value to CLI."""

    def __init__(self, *args, **kwargs):
        """Instantiate cli module."""
        super().__init__(
            module_name="Volux CLI Print",
            module_attr="cli",
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
        self.cli_val: int = 0

    def get(self) -> int:  # pylint: disable=method-hidden
        """Return value last printed."""
        return self.cli_val

    def set(self, new_val: int) -> None:  # pylint: disable=method-hidden
        """Set new value and print it to CLI."""
        self.cli_val = new_val
        print("VoluxCliPrint new value: {}".format(self.cli_val))

    def _setup(self):  # pylint: disable=method-hidden

        pass

    def _cleanup(self):  # pylint: disable=method-hidden

        pass
