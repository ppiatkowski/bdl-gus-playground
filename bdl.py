#!/usr/bin/python3

import argparse
from datetime import datetime
from logger import logger
import sys
from tablib import Dataset
from request_utils import *
from presets import *
from bdl_query import BDLMultiCityQuery, BDLMultiVariableQuery
from explore import explore_subjects


class Requests:
    births = "births"
    deaths = "deaths"
    population_by_age_and_gender = "population_by_age_and_gender"
    population = "population"


def main(argv):
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-r", "--request", help=f"One of the following:{requestHelp()}")
    parser.add_argument("-y", "--year", required=False)
    parser.add_argument("-e", "--export", action="store_true")
    parser.add_argument("-x", "--explore-subjects", action='store_true')
    args = parser.parse_args()
    if args.request:
        handleRequest(args)

    if args.explore_subjects:
        explore_subjects()


def exportToXLSX(data):
    xls = Dataset()
    for row in data:
        xls.append(row)
    now = datetime.now()
    timestamp = f"{now.year}-{now.month}-{now.day}T{now.hour}:{now.minute}:{now.second}"
    filename = f"results_{timestamp}.xlsx"
    with open(filename, "wb") as f:
        f.write(xls.export("xlsx"))
    logger.info(f"Data exported successfully ({filename})")


def handleRequest(args):
    try:
        requestType = args.request
        if requestType == Requests.population:
            query = BDLMultiCityQuery(Variable.Population.total, CITIES_10, lastYears())
        elif requestType == Requests.population_by_age_and_gender:
            if args.year == None:
                raise Exception(f"Year parameter is required in request {requestType}")
            query = BDLMultiVariableQuery(FEMALES, Unit.lublin, args.year)
        elif requestType == Requests.births:
            query = BDLMultiCityQuery(Variable.Demographics.births, CITIES_10, lastYears())
        elif requestType == Requests.deaths:
            query = BDLMultiCityQuery(Variable.Demographics.deaths, CITIES_10, lastYears())
        else:
            raise Exception(f"Invalid request {requestType}.\nValid request types are:{requestHelp()}")

        data = query.execute()
        if data:
            logger.info(data)
            if args.export:
                exportToXLSX(data)
        else:
            logger.warning("No data exported")
    except Exception as err:
        logger.error(f"Error: {err}")


def requestHelp():
    return f"\b - {Requests.births}\n - {Requests.deaths}\n - {Requests.population}\n - {Requests.population_by_age_and_gender}"


if __name__ == "__main__":
    main(sys.argv[1:])
