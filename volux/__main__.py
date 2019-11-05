#!/usr/bin/env python3 -e

import argparse
import colorama
colorama.init()

def main():

    # Initialize the parser
    parser = argparse.ArgumentParser(description="High-level media/entertainment workflow automation platform")

    # Add the positional parameter
    parser.add_argument('-l','--list', action="store", help="prints a list of available demos/modules", default=None)
    parser.add_argument('-d','--demo', action="store", help="run the specified demo", default=None)
    parser.add_argument('-i','--info', action="store", help="show info for installed volux module", default=None)
    parser.add_argument('-V','--version', action="store_true", help="Print version information and exit")

    # Parse the arguments
    arguments = parser.parse_args()

    if arguments.version == True:

        from volux import __name__, __version__
        print(__name__,__version__)

    elif arguments.list == 'demos':

        from volux import demos, VoluxDemo, VoluxCore

        _core = VoluxCore()

        items = _core.get_python_module_items(demos) # for each item in the demos module
        demos_collected = _core.filter_by_superclass(items,VoluxDemo) # filter out items not inherited from VoluxDemo class
        demo_aliases = [demo._alias for demo in demos_collected]
        print("available demos:",demo_aliases)

    elif arguments.list == 'modules':

        raise NotImplementedError()

    elif not arguments.demo == None:

        from volux import demos, VoluxDemo, VoluxCore

        _core = VoluxCore()

        items = _core.get_python_module_items(demos) # for each item in the demos module
        demos_collected = _core.filter_by_superclass(items,VoluxDemo) # filter out items not inherited from VoluxDemo class
        demo_dict = _core.gen_demo_dict(demos_collected)

        if arguments.demo in demo_dict:

            demo_dict[arguments.demo].run_demo()

        else:

            print("{}Error: '{}' is not a valid demo{}".format(colorama.Fore.RED,arguments.demo,colorama.Style.RESET_ALL))
            print("{}Tip: Type 'volux --list demos' for a list of available demos{}".format(colorama.Fore.YELLOW,colorama.Style.RESET_ALL))

    elif not arguments.info == None:

        raise NotImplementedError()

    else:

        print("{}Error: No command specified{}".format(colorama.Fore.RED,colorama.Style.RESET_ALL))
        print("{}Tip: See 'volux --help'{}".format(colorama.Fore.YELLOW,colorama.Style.RESET_ALL))

    # for i in range(0, arguments.repeat):
    #
    #     print(arguments.printme)

if __name__ == '__main__':

    main()
