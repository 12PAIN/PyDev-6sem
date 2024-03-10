import os
import argparse

def fileExists(path):
    return os.path.isfile(path)


def printFile(path: str, sort, num, count):

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


parser = argparse.ArgumentParser()

parser.add_argument("filePath")
parser.add_argument("--sort", action="store_true")
parser.add_argument("--num", action="store_true")
parser.add_argument("--count", action="store_true")

argsDict = parser.parse_args()

filePath = argsDict.filePath

sort = argsDict.sort
num = argsDict.num
count = argsDict.count


if filePath is not None and fileExists(filePath):
    printFile(filePath, sort, num, count)
else:
    print("ERROR!")
