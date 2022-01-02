#!/usr/bin/python3

import json
import logging
import requests
from request_utils import *
from presets import *

BASE_URL = "https://bdl.stat.gov.pl/api/v1"

''' Helper class '''


class BDLRow(object):
    def __init__(self, headers, row):
        self.headers = headers
        self.row = row


class BDLRequest(object):
    def __init__(self, city, variable, years):
        self.variable = variable
        self.city = city
        self.years = years

    ''' Performs request and return one row of data'''

    def start(self):
        yearsString = RequestParameter.yearString(self.years)
        url = f"{BASE_URL}/data/by-variable/{self.variable}?format=json&unit-parent-id={self.city}&{yearsString}"
        response = requests.get(url)
        if (response.ok):
            data = json.loads(response.content)
            results = data["results"]
            cityName = results[0]["name"]
            values = results[0]["values"]

            datapoints = {}  # year -> value
            for value in values:
                datapoints[value["year"]] = value["val"]
            years = sorted(list(datapoints.keys()))
            vals = []
            for year in years:
                vals.append(datapoints[year])
            return BDLRow([""] + years, [cityName] + vals)
        else:
            logging.error(f"Request failed [{response.status_code} {response.reason}]")
            logging.error(response.text)
