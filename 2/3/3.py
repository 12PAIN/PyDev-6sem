import argparse

parser = argparse.ArgumentParser()
parser.add_argument("arguments", nargs="*")

args = parser.parse_args().__dict__["arguments"]

if len(args) > 0:

    for arg in args:
        print(arg)

else:
    print("no args")
