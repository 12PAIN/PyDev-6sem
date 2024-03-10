import os
import sys


def getSysArgs(args_list: list[str]):
    args = {}

    unnamedArgCounter = 0

    for i, arg in enumerate(args_list):

        if i == 0: continue

        if arg.startswith("--"):
            if "=" not in arg:
                args[arg.lstrip("--")] = True
                continue
            else:
                args[arg.lstrip("--")] = bool(arg.split("=")[1])
                continue

        if "=" not in arg:
            args[f"unnamed_{unnamedArgCounter}"] = arg
            unnamedArgCounter += 1
            continue

        splitted_arg = arg.split("=")
        key = splitted_arg[0]
        value = splitted_arg[1]

        args[key] = value

    return args


def fileExists(path):
    return os.path.isfile(path)


def printFile(path: str, args: dict[str]):
    sort = args["sort"] if "sort" in args.keys() else False
    num = args["num"] if "num" in args.keys() else False
    count = args["count"] if "count" in args.keys() else False

    f = open(path, "r")
    rows = [line.rstrip() for line in f.readlines()]
    f.close()

    if sort:
        rows = sorted(rows)


    counter = 0
    for i, line in enumerate(rows):


        counter += 1
        if num:
            print(i + 1, line)
        else:
            print(line)

    if count:
        print("Total rows count:", counter)


argsDict = getSysArgs(sys.argv)

filePath = argsDict["unnamed_0"]

if fileExists(filePath):
    printFile(filePath, argsDict)
else:
    print("ERROR!")
