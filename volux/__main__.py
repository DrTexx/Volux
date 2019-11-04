#!/usr/bin/env python3 -e

import argparse
import colorama
colorama.init()

def get_python_module_items(module):

    return [getattr(module,item_name) for item_name in dir(module)]

def filter_by_attr_value(module_items,attribute,attribute_value):

    valid_items = []

    for item in module_items:

        if hasattr(item,attribute):

            if getattr(item,attribute) == attribute_value:

                valid_items.append(item)

    return(valid_items)

def filter_by_superclass(items,superclass):
    """return all objects which have inherited a particular superclass"""

    return filter_by_attr_value(items, 'superclass', superclass)

def gen_demo_dict(demo_list):

    demo_dict = {demo._alias: demo for demo in demo_list}
    return demo_dict

def main():

    # Initialize the parser
    parser = argparse.ArgumentParser(description="High-level media/entertainment workflow automation platform")

    # Add the positional parameter
    parser.add_argument('-l','--list', action="store", choices=['demos','modules'], help="return a list of avaiable items", default=None)
    parser.add_argument('-d','--demo', action="store", help="run the specified demo")

    # Parse the arguments
    arguments = parser.parse_args()

    # Finally print the passed string
    if arguments.list == 'demos':

        from volux import demos, VoluxDemo

        items = get_python_module_items(demos) # for each item in the demos module
        demos_collected = filter_by_superclass(items,VoluxDemo) # filter out items not inherited from VoluxDemo class
        demo_aliases = [demo._alias for demo in demos_collected]
        print("available demos:",demo_aliases)

    elif arguments.list == 'modules':

        raise NotImplementedError()

    elif not arguments.demo == None:

        from volux import demos, VoluxDemo

        items = get_python_module_items(demos) # for each item in the demos module
        demos_collected = filter_by_superclass(items,VoluxDemo) # filter out items not inherited from VoluxDemo class
        demo_dict = gen_demo_dict(demos_collected)

        if arguments.demo in demo_dict:

            demo_dict[arguments.demo].run_demo()

        else:

            print("{}Error: '{}' is not a valid demo{}".format(colorama.Fore.RED,arguments.demo,colorama.Style.RESET_ALL))
            print("{}Tip: Type 'volux --list demos' for a list of available demos{}".format(colorama.Fore.YELLOW,colorama.Style.RESET_ALL))

    else:

        print("{}Error: Not enough arguments{}".format(colorama.Fore.RED,colorama.Style.RESET_ALL))
        print("{}Tip: Type 'volux --help' for a list of commands{}".format(colorama.Fore.YELLOW,colorama.Style.RESET_ALL))

    # for i in range(0, arguments.repeat):
    #
    #     print(arguments.printme)

if __name__ == '__main__':

    main()


# def main():
#
#     if len(sys.argv) > 1:
#
#         if sys.argv[1] == 'demo':
#
#             if len(sys.argv) > 2:
#
#                 if sys.argv[2] == 'bar':
#
#                     from volux.demos import demo_volbar
#                     demo_volbar.run_demo()
#
#                 else:
#
#                     raise Exception("'{}' is not a valid demo".format(sys.argv[2]))
#
#             else:
#
#                 raise Exception("Please specify a demo to run")
#
#         else:
#
#             raise Exception("'{}' is not a valid argument".format(sys.argv[1]))
#
#     else:
#
#         print("ERROR: too few arguments")
#
# if __name__ == '__main__':
#     main()
