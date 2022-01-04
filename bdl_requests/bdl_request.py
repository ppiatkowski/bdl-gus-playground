#!/usr/bin/python3


import json
import os
import requests
from logger import logger
from request_utils import *
from presets import *


class BDLRequest(object):
    BASE_URL = "https://bdl.stat.gov.pl/api/v1"

    def get(self, url):
        logger.debug(f"HTTP GET {url} ...")
        apiKey = os.environ.get('BDL_API_KEY')
        return requests.get(url, headers={"X-ClientId": apiKey})

    def handleError(self, response):
        if response.status_code == 429:
            logger.warning(
                "In case of 'Too Many Requests' error register on https://api.stat.gov.pl/Home/BdlApi"
                " and set BDL_API_KEY environment variable to increase your request limits"
            )
        logger.error(f"Request failed [{response.status_code} {response.reason}]")
        logger.error(response.text)


''' Helper class '''


class BDLRow(object):
    def __init__(self, headers, row):
        self.headers = headers
        self.row = row


class BDLUnitRequest(BDLRequest):
    def __init__(self, city, variable, year):
        self.variable = variable
        self.city = city
        self.year = year

    def start(self):
        url = f"{BDLRequest.BASE_URL}/data/by-unit/{self.city}?format=json&year={self.year}&var-id={self.variable}"
        response = super().get(url)
        if response.ok:
            data = json.loads(response.content)
            results = data["results"]
            if len(results) == 0:
                raise Exception("Empty response")
            values = results[0]["values"]
            return values[0]["val"]
        else:
            super().handleError(response)


class BDLVariableRequest(BDLRequest):
    def __init__(self, city, variable, years):
        self.variable = variable
        self.city = city
        self.years = years

    ''' Performs request and return data'''

    def start(self):
        yearsString = RequestParameter.yearString(self.years)
        url = f"{BDLRequest.BASE_URL}/data/by-variable/{self.variable}?format=json&unit-parent-id={self.city}&{yearsString}"
        response = super().get(url)
        if response.ok:
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
            super().handleError(response)
