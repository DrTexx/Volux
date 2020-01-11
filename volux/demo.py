"""Base class for volux demos."""

# builtin
import importlib

# site
import colorama


class VoluxDemo:
    """Base class for creating volux demos. Ensures certain metadata is provided in demos for use elsewhere."""

    def __init__(
        self,
        demo_name,
        demo_method,
        alias,
        requirements: list = [],
        *args,
        **kwargs
    ):
        """Do not directly instansiate, this class should always be used as a base for other specific demo classes."""
        self._name = demo_name
        self._method = demo_method
        self._alias = alias
        self._requirements = requirements  # optional

    def run(self) -> None:
        """Run the demo."""
        self._method()

    # def __str__(self):
    #     header = "[DEMO:{name}]----".format(name=self._alias)
    #     divider = "-"*len(header)
    #     body = "Name: {name}\nAlias: {alias}\nRequirements: {requirements}".format(name=self._name,requirements=self._requirements, alias=self._alias)
    #
    #     return("{header}\n{body}\n{divider}".format(header=header,divider=divider,body=body))

    def __repr__(self) -> str:
        """Give the demo class a custom repr."""
        return "<VoluxDemo '{}'>".format(self._alias)

    def _check_reqs(self) -> None:

        failed_imports = []
        for req in self._requirements:

            try:
                importlib.import_module(req)

            except ImportError:
                failed_imports.append(req)

        if len(failed_imports) > 0:
            print(
                "{}Error: unable to start demo, you're missing some requirements: {}{}".format(
                    colorama.Fore.RED,
                    ", ".join(failed_imports),
                    colorama.Style.RESET_ALL,
                )
            )
            print(
                "{}Tip: try seeing if the package/s are available in pip ('pip search {}'){}".format(
                    colorama.Fore.YELLOW,
                    " ".join(failed_imports),
                    colorama.Style.RESET_ALL,
                )
            )
            exit()
