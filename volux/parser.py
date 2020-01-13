"""Define the class for handling argparsing."""

# builtin
import argparse
import logging
from typing import Dict

# site
import colorama

log = logging.getLogger("Volux CLI")
log.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter and add it to the handlers
# formatter = logging.Formatter(
#     "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
# )
# ch.setFormatter(formatter)
# add the handlers to the logger
log.addHandler(ch)


class VoluxParser:
    """Class to assist in handling argparse stuff."""

    def __init__(self) -> None:
        """See class docstring."""
        # create the top-level parser
        self.wip_string = "{}not yet implemented{}".format(
            colorama.Fore.YELLOW, colorama.Style.RESET_ALL
        )

        self.parser = argparse.ArgumentParser()

        self._add_optionals(self.parser)
        self.subparsers = self._add_subparser(self.parser)

        self.launch_parser = self._add_launch_parser(self.subparsers)
        self.demo_parser = self._add_demo_parser(self.subparsers)
        self.module_parser = self._add_module_parser(self.subparsers)
        self.script_parser = self._add_script_parser(self.subparsers)

        self.arguments = self.parser.parse_args()

    def print_version(self) -> None:
        """Print the volux verison."""
        from volux import __name__, __version__

        print(__name__, __version__)

    def launch_gui(self, preset: str = "") -> None:
        """Launch the volux gui."""
        print("launching...")
        try:
            import voluxgui as gui

            if preset == "":
                gui.launch()
            else:
                preset_str = str(preset)  # ensure preset is a string
                gui.launch(connection_preset=preset_str)

        except ImportError:
            self._err_missing_module("voluxgui")

        exit()

    def print_demo_list(self) -> None:
        """Print a list of available demos as aliases."""
        from volux import VoluxCore

        core = VoluxCore()
        demo_dict = core.gen_demo_dict()
        demo_aliases = demo_dict.keys()
        demos_string = ", ".join(demo_aliases)
        print("Available demos:", demos_string)

    def _err_missing_module(self, module_name: str) -> None:
        print(
            "{}Error: Couldn't find {module_name}, please make sure you have it installed{}".format(
                colorama.Fore.RED,
                colorama.Style.RESET_ALL,
                module_name=module_name,
            )
        )

    def _err_invalid_demo_alias(self, demo_alias: str) -> None:
        print(
            "{}Error: '{}' is not a valid demo alias{}".format(
                colorama.Fore.RED, demo_alias, colorama.Style.RESET_ALL,
            )
        )

    def _err_internal(self, message: str) -> None:
        print(
            "{}Internal Error: {message}{}".format(
                colorama.Fore.RED, colorama.Style.RESET_ALL, message=message
            )
        )

    def _validate_demo_alias(self, demo_alias: str) -> bool:
        log.debug("...checking demo alias is valid")
        from .core import VoluxCore
        from .demo import VoluxDemo

        core: VoluxCore = VoluxCore()
        valid_demo_aliases: Dict[str, VoluxDemo] = core.gen_demo_dict()

        if demo_alias in valid_demo_aliases:
            return True
        else:
            return False

    def run_demo_alias(self, demo_alias: str) -> None:
        """Run the demo with the alias specified."""
        log.debug(f"[[ DEMO: ]] {demo_alias}")

        from volux import VoluxCore

        core = VoluxCore()

        demo_dict = core.gen_demo_dict()
        demo_is_valid = demo_alias in demo_dict

        if demo_is_valid is True:

            log.info(f"Launching demo with alias '{demo_alias}'")
            demo_instance = demo_dict[demo_alias]()  # type: ignore
            demo_instance.run()
            exit()

        elif demo_is_valid is False:

            self._err_invalid_demo_alias(demo_alias)
            self.print_demo_list()
            exit()

        else:

            self._err_internal("demo validation didn't return a bool")

    def print_module_list(self) -> None:
        """Print list of available volux modules."""
        print("MODULE LIST")
        # import modulefinder

        # print(modulefinder.ModuleFinder())

    def print_module_info(self, vmod_name: str) -> None:
        """Print info on a specific volux module."""
        print(f"MODULE INFO: {vmod_name}")

    def handle_arguments(self, arguments: argparse.Namespace) -> None:
        """Handle inputed arguments."""
        log.debug(f"[[ ARGUMENTS: ]] {arguments}")
        log.debug(f"[[ SUBCOMMAND: ]] {arguments.subcommand}")

        if arguments.version is True:

            self.print_version()
            exit()

        elif arguments.subcommand == "launch":

            self.launch_gui()
            exit()

        elif arguments.subcommand == "demo":

            if arguments.DEMO is None:

                self.print_demo_list()
                exit()

            elif isinstance(arguments.DEMO, str):

                self.run_demo_alias(arguments.DEMO)
                exit()

            else:

                self._err_internal("demo name must be a string")
                exit()

        elif arguments.subcommand == "module":

            if arguments.MODULE is None:

                self.print_module_list()
                exit()

            elif isinstance(arguments.MODULE, str):

                self.print_module_info(arguments.MODULE)
                exit()

            else:

                self._err_internal("module name must be a string")
                exit()

        print("CANCELLING, PAST WIP POINT")
        exit()

        if arguments.subcommand == "list":

            if arguments.LIST == "demos":
                from volux import VoluxCore

                _core = VoluxCore()
                demos_string = ", ".join(_core.get_demo_aliases())
                print("Available demos:", demos_string)

            elif arguments.LIST == "modules":
                print("Available modules:", self.wip_string)

            elif arguments.LIST == "scripts":
                from volux import VoluxCore

                _core = VoluxCore()
                scripts_string = ", ".join(_core.get_script_names())
                print("Available scripts:", scripts_string)

            else:

                print(
                    "{}Error: '{}' is not a valid list name{}".format(
                        colorama.Fore.RED,
                        arguments.LIST,
                        colorama.Style.RESET_ALL,
                    )
                )
                print(
                    "{}Tip: See 'volux --lists'{}".format(
                        colorama.Fore.YELLOW, colorama.Style.RESET_ALL
                    )
                )

            exit()

        elif arguments.subcommand == "demo":

            print("RUN DEMO (OLD)")

        elif arguments.subcommand == "script":

            print("script launching is {}".format(self.wip_string))

            exit()

        elif arguments.subcommand == "info":

            print("module info is {}".format(self.wip_string))

            exit()

        else:

            print(
                "{}Error: No command specified{}".format(
                    colorama.Fore.RED, colorama.Style.RESET_ALL
                )
            )
            print(
                "{}Tip: See 'volux --help'{}".format(
                    colorama.Fore.YELLOW, colorama.Style.RESET_ALL
                )
            )

            exit()

    def _add_optionals(self, root_parser: argparse.ArgumentParser) -> None:
        # optional arguments before sub-commands
        root_parser.add_argument(
            "-V",
            "--version",
            action="store_true",
            help="print version information and exit",
        )
        root_parser.add_argument(
            "--lists", action="store_true", help="show available lists"
        )

    def _add_subparser(
        self, root_parser: argparse.ArgumentParser
    ) -> argparse._SubParsersAction:
        # create subparsers object
        subparsers = root_parser.add_subparsers(
            dest="subcommand", help="available sub-commands"
        )
        return subparsers

    def _add_launch_parser(
        self, child_parser: argparse._SubParsersAction
    ) -> argparse.ArgumentParser:
        # create the parser for the "launch" command
        parser_launch = child_parser.add_parser(
            "launch",
            help="launch the volux GUI",
            description="launch the volux GUI",
        )
        parser_launch.add_argument(
            "-lfx",
            "--lightshow",
            action="store_true",
            help="launch with lightshow preset",
        )
        return parser_launch

    def _add_demo_parser(
        self, child_parser: argparse._SubParsersAction
    ) -> argparse.ArgumentParser:
        """Return parser for the 'demo' subcommand."""
        parser_demo = child_parser.add_parser(
            "demo", help="list available demos"
        )
        parser_demo.add_argument(
            "DEMO", action="store", help="name of the demo to run", nargs="?"
        )
        return parser_demo

    def _add_module_parser(
        self, child_parser: argparse._SubParsersAction
    ) -> argparse.ArgumentParser:
        parser_module = child_parser.add_parser(
            "module", help="list available volux modules"
        )
        parser_module.add_argument(
            "MODULE",
            action="store",
            help="list available volux modules",
            nargs="?",
        )
        return parser_module

    def _add_script_parser(
        self, child_parser: argparse._SubParsersAction
    ) -> argparse.ArgumentParser:
        # create the parser for the "script" command
        parser_script = child_parser.add_parser(
            "script", help="run the specified script"
        )
        parser_script.add_argument(
            "SCRIPT", action="store", help="name of script to run"
        )
        return parser_script

    def _add_info_parser(
        self, child_parser: argparse._SubParsersAction
    ) -> argparse.ArgumentParser:
        # create the parser for the "info" command
        parser_info = child_parser.add_parser(
            "info", help="show information for a specified module"
        )
        parser_info.add_argument(
            "MODULE", action="store", help="name of the module to get info for"
        )
        return parser_info
