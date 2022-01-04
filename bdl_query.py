#!/usr/bin/python3

from bdl_requests.bdl_request import *
from logger import logger


class BDLMultiVariableQuery(object):
    def __init__(self, variables, city, year):
        self.variables = variables
        self.city = city
        self.year = year

    def execute(self):
        vals = []
        for variable in self.variables:
            request = BDLUnitRequest(self.city, variable, self.year)
            val = request.start()
            if (val):
                vals.append(val)
            else:
                raise Exception(f"No data found for city {self.city} and variable {variable}")
        return [vals]


class BDLMultiCityQuery(object):
    def __init__(self, variable, cities, years):
        self.variable = variable
        self.cities = cities
        self.years = years

    def execute(self):
        rows = []
        for city in self.cities:
            request = BDLVariableRequest(city, self.variable, self.years)
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
