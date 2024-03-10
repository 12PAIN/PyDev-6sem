import argparse
import sys

def printSysArgs(argsDict: dict):
    localArgsDict = {}
    if argsDict["sort"]:
        del argsDict["sort"]
        localArgsDict = dict(sorted(argsDict.items()))
    else:
        localArgsDict = argsDict

    for key, value in localArgsDict.items():
        print(f"Key: {key}, value: {value}")

def reformatArgsDict(argsDict):

    newArgsDict = argsDict

    for arg in newArgsDict['args']:
        newArgsDict[arg.split("=")[0]] = arg.split("=")[1]

    del newArgsDict["args"]

    return newArgsDict


parser = argparse.ArgumentParser()
parser.add_argument("--sort", action="store_true")
parser.add_argument("args", nargs="+")


args = reformatArgsDict(parser.parse_args().__dict__)

printSysArgs(args)


