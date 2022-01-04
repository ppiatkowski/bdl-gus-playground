#!/usr/bin/python3

from logger import logger
from request_utils import *
from presets import *
from bdl_requests.subjects_request import BDLSubjectRequest


def explore_subjects():
    selection = None
    while True:
        try:
            request = BDLSubjectRequest(parent=selection)
            subjects = request.start()
            if subjects:
                parseSubjects(subjects)
            selection = input("> Enter subject ID: ")
        except Exception as err:
            logger.error(f"Error: {err}")
            exit(1)


def parseSubjects(subjects):
    for s in subjects:
        id = s["id"]
        name = s["name"]
        hasVariables = s["hasVariables"]
        if hasVariables:
            print(f" *{id}* {name}")
        else:
            print(f"[{id}] {name}")
