# builtin
import importlib

# site
import colorama


class VoluxDemo:
    def __init__(
        self, demo_name, demo_method, alias, requirements=[], *args, **kwargs
    ):
        self._name = demo_name
        self._method = demo_method
        self._alias = alias
        self._requirements = requirements  # optional

    def run(self):

        self._method()

    # def __str__(self):
    #     header = "[DEMO:{name}]----".format(name=self._alias)
    #     divider = "-"*len(header)
    #     body = "Name: {name}\nAlias: {alias}\nRequirements: {requirements}".format(name=self._name,requirements=self._requirements, alias=self._alias)
    #
    #     return("{header}\n{body}\n{divider}".format(header=header,divider=divider,body=body))

    def __repr__(self):

        return "<VoluxDemo '{}'>".format(self._alias)

    def _check_reqs(self):

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
