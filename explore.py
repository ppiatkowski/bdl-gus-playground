#!/usr/bin/python3

from logger import logger
from request_utils import *
from presets import *
from bdl_requests.explore_request import BDLExploreRequest, BDLItem


def explore_subjects():
    selection = None
    while True:
        try:
            request = BDLExploreRequest(parent=selection)
            rawItems = request.start()
            items = []
            if rawItems:
                items = parseItems(rawItems)
            if items:
                for i in items:
                    print(f" [{i.id}] {i.name}")
            chosenId = input("\n> Enter subject/variable ID: ")
            filteredItems = [item for item in items if item.id == chosenId]
            if filteredItems:
                selection = filteredItems[0]
            else:
                logger.warning(f"Invalid input: {chosenId}")

            print(f"selection: {selection}")
        except Exception as err:
            logger.error(f"Error: {err}")
            exit(1)


def parseItems(itemsRaw):
    items = []
    for i in itemsRaw:
        print(i)
        id = i["id"]
        name = None
        if "name" in i:
            name = i["name"]
        else:
            name = mergeName(i)
        hasVariables = False
        if "hasVariables" in i:
            hasVariables = i["hasVariables"]

        items.append(
            BDLItem(
                type=BDLItem.TYPE_VARIABLE if hasVariables else BDLItem.TYPE_SUBJECT,
                id=id,
                name=name,
            )
        )
    return items


def mergeName(item):
    names = []
    names = addName(item, "n1", names)
    names = addName(item, "n2", names)
    names = addName(item, "n3", names)
    return " ".join(names)


def addName(item, key, names):
    if key in item:
        names.append(item[key])
    return names
