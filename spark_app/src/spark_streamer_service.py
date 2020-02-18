import json
from urllib.parse import urlparse

INVALID_EVENT = (-1, ("", -1))
MAX_EVENTS = 5

def line_to_json(line):
    try:
        line_as_json = json.loads(line)
        id = int(line_as_json["Id"])
        url = str(line_as_json["Url"])
        if urlparse(url).netloc == '':
            print("Invalid url")
            return INVALID_EVENT
        time = int(line_as_json["Time"])
        return (id, (url, time))
    except Exception:
        return INVALID_EVENT

def saveStateFunc(newValues, oldValues):
    if oldValues is None:
        oldValues = []
    for newValue in newValues:
        oldValues.append(newValue)
    newState = nlargest(MAX_EVENTS, oldValues, key=lambda k: k[1]) 
    return newState 
