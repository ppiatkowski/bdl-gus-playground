#!/usr/bin/python3

from bdl_request import BDLRequest
import logging


class BDLQuery(object):
    def __init__(self, variable, cities, years):
        self.variable = variable
        self.cities = cities
        self.years = years
        self.data = []

    def execute(self):
        rows = []
        for city in self.cities:
            request = BDLRequest(city, self.variable, self.years)
            row = request.start()
            if (row):
                rows.append(row)
            else:
                raise Exception(f"No data found for city {city}")
        data = []
        if (rows):
            data.append(rows[0].headers)
        for row in rows:
            data.append(row.row)
        return data
