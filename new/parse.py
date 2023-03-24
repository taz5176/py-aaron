import argparse, sys


class Arg_Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument(
            '-d', '--debug',
            dest='debug',
            help='display more information',
            action='store_true'
        )

        cmds = self.parser.add_subparsers(dest='commands')
        run = cmds.add_parser(
            'run',
            help='run test'
        )
        analyse = cmds.add_parser(
            'analyse',
            help='analyse test data file'
        )
        analyse.add_argument(
            '-i',
            dest='input',
            help='test data file .csv',
            type=str,
            required=True
        )
        args = self.parser.parse_args()
        print(args)

        if args.debug:
            self.debug = True
        else:
            self.debug = False

arg_parser = Arg_Parser()
# print(arg_parser.debug)

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d', '--debug',
        help='display more information',
        action='store_false'
    )
    
    cmds = parser.add_subparsers(dest='commands')
    run = cmds.add_parser(
        'run',
        help='run test'
    )
    analyse = cmds.add_parser(
        'analyse',
        help='analyse test data file'
    )
    analyse.add_argument(
        '-i',
        dest='input',
        help='test data file .csv',
        type=str
    )

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()
    print(args)