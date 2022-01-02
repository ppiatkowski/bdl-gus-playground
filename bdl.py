#!/usr/bin/python3

import coloredlogs
import logging
import sys
from tablib import Dataset
from request_utils import *
from presets import *
from bdl_query import BDLQuery


logger = logging.getLogger(__name__)
coloredlogs.install(level="DEBUG", fmt="%(asctime)s %(levelname)s %(message)s")


def main(argv):
    logger.debug("BDL Playground")
    try:
        query = BDLQuery(Variables.populationTotal, CITIES_10, lastYears())
        data = query.execute()
        if (data):
            exportToXLSX(data)
        else:
            logging.warning("No data exported")
    except Exception as err:
        logging.error(f"Error: {err}")


def exportToXLSX(data):
    xls = Dataset()
    for row in data:
        xls.append(row)

    with open('results.xlsx', 'wb') as f:
        f.write(xls.export('xlsx'))
    logging.info("Data exported successfully")


if __name__ == "__main__":
    main(sys.argv[1:])
