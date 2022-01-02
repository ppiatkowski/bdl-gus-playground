#!/usr/bin/python3

import coloredlogs
from logger import logger
import sys
from tablib import Dataset
from request_utils import *
from presets import *
from bdl_query import BDLQuery


def main(argv):
    try:
        query = BDLQuery(Variables.populationTotal, CITIES_10, lastYears())
        data = query.execute()
        if (data):
            exportToXLSX(data)
        else:
            logger.warning("No data exported")
    except Exception as err:
        logger.error(f"Error: {err}")


def exportToXLSX(data):
    xls = Dataset()
    for row in data:
        xls.append(row)

    with open('results.xlsx', 'wb') as f:
        f.write(xls.export('xlsx'))
    logger.info(f"Data exported successfully")


if __name__ == "__main__":
    main(sys.argv[1:])
