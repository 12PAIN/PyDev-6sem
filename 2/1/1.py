import sys


def getSysArgs(args_list: list[str]):
    args = {}

    for i, arg in enumerate(args_list):

        if i == 0: continue

        if arg.startswith("--"):
            if "=" not in arg:
                args[arg.lstrip("--")] = True
                continue
            else:
                args[arg.lstrip("--")] = bool(arg.split("=")[1])
                continue

        splitted_arg = arg.split("=")
        key = splitted_arg[0]
        value = splitted_arg[1]

        args[key] = value

    return args


def printSysArgs(argsDict: dict[str]):
    localArgsDict = {}
    if "sort" in argsDict.keys():
        if argsDict["sort"] is True:
            del argsDict["sort"]
            localArgsDict = dict(sorted(argsDict.items()))
        else:
            del argsDict["sort"]
            localArgsDict = argsDict
    else:
        localArgsDict = argsDict

    for key, value in localArgsDict.items():
        print(f"Key: {key}, value: {value}")


argsDict = getSysArgs(sys.argv)
printSysArgs(argsDict)
