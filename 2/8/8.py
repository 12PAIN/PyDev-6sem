import argparse


def reformatIncomeDict(incomesDict):

    newIncomesDict = {}


    for key, value in incomesDict.items():
        if "per_" not in key:
            continue
        newIncomesDict[key.split("per_")[1]] = float(value) if "+" not in value else float(value.split("+")[1])

    return newIncomesDict


def calcIncomePerDay(incomesDict):
    income = 0

    for key, value in incomesDict.items():

        incomePeriod: float = 0.

        if "day" in key:
            incomePeriod = 1.
        elif "week" in key:
            incomePeriod = 7.
        elif "month" in key:
            incomePeriod = 30.
        elif "year" in key:
            incomePeriod = 360.

        income += value / incomePeriod

    return income

def calcPLReport(incomePerDay, calcPeriodName):

    calcDays = 1 if calcPeriodName == "day" else 30 if calcPeriodName == "month" else 360

    return int(incomePerDay * calcDays)



parser = argparse.ArgumentParser()


#(--per-day, --per-week, --per-month, --per-year
parser.add_argument("--per-day", type=str, default="+0")
parser.add_argument("--per-week", type=str,  default="+0")
parser.add_argument("--per-month", type=str, default="+0")
parser.add_argument("--per-year", type=str, default="+0")
parser.add_argument("--get-by", choices=["day", "month", "year"], default="day")


args = parser.parse_args().__dict__

reformattedIncomesDict = reformatIncomeDict(args)

print(calcPLReport(calcIncomePerDay(reformattedIncomesDict), args["get_by"]))

