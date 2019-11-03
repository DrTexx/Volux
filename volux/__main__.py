# import argparse
#
# parser = argparse.ArgumentParser(description='A platform for controlling your media/entertainment workflows.')
#
# parser.add_argument(
#     'command'
# )
#
# parser.add_argument(
#     'integers',
#     metavar='N',
#     type=int,
#     nargs='+',
#     help='an integer for the accumulator'
# )
#
# parser.add_argument(
#     '--sum',
#     dest='accumulate',
#     action='store_const',
#     const=sum,
#     default=max,
#     help='sum the integers (default: find the max)'
# )
# args = parser.parse_args()
#
# print(args.accumulate(args.integers))

import sys

if len(sys.argv) > 1:

    if sys.argv[1] == 'demo':

        if len(sys.argv) > 2:

            if sys.argv[2] == 'bar':

                from volux.demos import demo_volbar
                demo_volbar.run_demo()

            else:

                raise Exception("'{}' is not a valid demo".format(sys.argv[2]))

        else:

            raise Exception("Please specify a demo to run")

    else:

        raise Exception("'{}' is not a valid argument".format(sys.argv[1]))

else:

    print("ERROR: too few arguments")
