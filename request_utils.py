#!/usr/bin/python3

from datetime import date


class RequestParameter:
    @classmethod
    def yearString(cls, years):
        return "&".join([f"year={year}" for year in years])


def lastYears(n=12):
    thisYear = date.today().year
    return list(range(thisYear - n, thisYear+1))
