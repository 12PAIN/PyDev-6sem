import argparse
import sys



class ArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        self.exit(2)


def calc():

    try:
        parser = ArgumentParser()

        parser.add_argument("args", nargs="*", type=int)
        args = parser.parse_args()

        if len(args.args) > 2:
            print("TOO MANY PARAMS")
        elif len(args.args) == 0:
            print("NO PARAMS")
        elif len(args.args) < 2:
            print("TOO FEW PARAMS")

        if len(args.args) != 2:
            return

        print(args.args[0] + args.args[1])

    except BaseException as ex:
        print(ex.__class__.__name__)

calc()