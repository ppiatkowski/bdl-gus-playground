#!/usr/bin/python3

import json
from presets import *
from request_utils import *
from bdl_requests.bdl_request import BDLRequest


class BDLItem:
    TYPE_SUBJECT = 1
    TYPE_VARIABLE = 2

    def __init__(self, type, id, name):
        self.type = type
        self.id = id
        self.name = name


class BDLExploreRequest(BDLRequest):
    def __init__(self, parent=None):
        self.parent = parent

    def start(self):
        if self.parent and self.parent.type == BDLItem.TYPE_VARIABLE:
            url = f"{BDLRequest.BASE_URL}/Variables?format=json&page-size=50&subject-id={self.parent.id}"
        else:
            url = f"{BDLRequest.BASE_URL}/subjects?format=json&page-size=50"
            if self.parent:
                url += f"&parent-id={self.parent.id}"
        response = super().get(url)
        if response.ok:
            data = json.loads(response.content)
            results = data["results"]
            if len(results) == 0:
                raise Exception("Empty response")
            return results
        else:
            super().handleError(response)
