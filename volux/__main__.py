#!/usr/bin/env python3 -e

import argparse
import colorama
colorama.init()

def main():

    list_choices = ['demos','modules','scripts']
    wip_string = "{}not yet implemented{}".format(colorama.Fore.YELLOW,colorama.Style.RESET_ALL)

    # create the top-level parser
    parser = argparse.ArgumentParser()

    # optional arguments before sub-commands
    parser.add_argument('-V','--version', action="store_true", help="print version information and exit")
    parser.add_argument('--lists', action="store_true", help="show available lists")

    # create subparsers object
    subparsers = parser.add_subparsers(dest="subcommand",help='available sub-commands')

    # create the parser for the "list" command
    parser_list = subparsers.add_parser('list', help='list available demos, modules or scripts')
    parser_list.add_argument('LIST', action="store", help='name of list to retrieve')

    # create the parser for the "demo" command
    parser_demo = subparsers.add_parser('demo', help='run the specified demo')
    parser_demo.add_argument('DEMO', action="store", help='name of the demo to run')
    parser_demo.add_argument('--baz', choices='XYZ', help='baz help')

    # create the parser for the "script" command
    parser_script = subparsers.add_parser('script', help="run the specified script")
    parser_script.add_argument("SCRIPT", action="store", help="name of script to run")

    # create the parser for the "info" command
    parser_info = subparsers.add_parser('info', help="show information for a specified module")
    parser_info.add_argument("MODULE", action="store", help="name of the module to get info for")

    # create the parser for the "launch" command
    parser_launch = subparsers.add_parser('launch', help="launch the volux GUI", description="launches the volux GUI")
    parser_launch.add_argument("--foo", action="store_true", help="a test optional argument")

    # Parse the arguments
    arguments = parser.parse_args()

    if arguments.version == True:

        from volux import __name__, __version__
        print(__name__,__version__)
        exit()

    elif arguments.lists == True:

        print("Available lists:",", ".join(list_choices))
        exit()

    if arguments.subcommand == 'launch':

        print("launching...")
        from volux.scripts import launch_gui
        launch_gui()
        exit()

    elif arguments.subcommand == 'list':

        if arguments.LIST == 'demos':
            from volux import VoluxCore
            _core = VoluxCore()
            demos_string = ",".join(_core.get_demo_aliases())
            print("Available demos:",demos_string)

        elif arguments.LIST == 'modules':
            print("Available modules:",wip_string)

        elif arguments.LIST == 'scripts':
            print("Available scripts:",wip_string)

        else:

            print("{}Error: '{}' is not a valid list name{}".format(colorama.Fore.RED,arguments.LIST,colorama.Style.RESET_ALL))
            print("{}Tip: See 'volux --lists'{}".format(colorama.Fore.YELLOW,colorama.Style.RESET_ALL))

        exit()

    elif arguments.subcommand == 'demo':

        from volux import demos, VoluxDemo, VoluxCore

        _core = VoluxCore()
        demo_dict = _core.get_demo_dict()
        if arguments.DEMO in demo_dict:
            demo_dict[arguments.DEMO].run_demo()
        else:
            print("{}Error: '{}' is not a valid demo{}".format(colorama.Fore.RED,arguments.DEMO,colorama.Style.RESET_ALL))
            print("{}Tip: See 'volux list demos'{}".format(colorama.Fore.YELLOW,colorama.Style.RESET_ALL))

        exit()

    elif arguments.subcommand == 'script':

        print("script launching is {}".format(wip_string))

        exit()

    elif arguments.subcommand == 'info':

        print("module info is {}".format(wip_string))

        exit()

    else:

        print("{}Error: No command specified{}".format(colorama.Fore.RED,colorama.Style.RESET_ALL))
        print("{}Tip: See 'volux --help'{}".format(colorama.Fore.YELLOW,colorama.Style.RESET_ALL))

        exit()

if __name__ == '__main__':

    main()
