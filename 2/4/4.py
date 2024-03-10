import argparse
import os.path


def copyFile(inputPath, outputPath, toUpper, linesCount):

    if not os.path.isfile(inputPath):
        print("File not found!")
        return

    inputFile = open(inputPath, 'r', encoding='utf-8')
    rows = inputFile.readlines()
    inputFile.close()

    outputFile = open(outputPath, 'w+', encoding='utf-8')

    for i, row in enumerate(rows):



        if linesCount is not None and i >= linesCount:
            break

        row = row.upper() if toUpper else row
        row = row if linesCount is not None and (i < linesCount - 1) and i < len(rows) else row.rstrip()

        outputFile.write(row)

    outputFile.close()


parser = argparse.ArgumentParser(prog="File Copy", description="Copying text files")
parser.add_argument("-u", "--upper", action="store_true")
parser.add_argument("-l", "--lines", action="store", type=int)
parser.add_argument("inputFilePath")
parser.add_argument("outputFilePath")

args = parser.parse_args()

copyFile(args.inputFilePath, args.outputFilePath, args.upper, args.lines)