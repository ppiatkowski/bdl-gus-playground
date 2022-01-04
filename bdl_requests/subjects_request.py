#!/usr/bin/python3


import json

from logger import logger
from presets import *
from request_utils import *

from bdl_requests.bdl_request import BDLRequest


class BDLSubjectRequest(BDLRequest):
    def __init__(self, parent=None):
        self.parent = parent

    def start(self):
        url = f"{BDLRequest.BASE_URL}/subjects?format=json&page-size=50"
        if self.parent:
            url += f"&parent-id={self.parent}"
        response = super().get(url)
        if response.ok:
            data = json.loads(response.content)
            results = data["results"]
            if len(results) == 0:
                raise Exception("Empty response")
            return results
        else:
            super().handleError(response)
