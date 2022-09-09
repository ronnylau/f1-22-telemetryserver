import os
import sys
import json
from pathlib import Path


def getconfig():
    config = {
        'path': '.',
        'write-frequency': 5,
        'prefix': '',
    }
    return config


config = getconfig()
filename = sys.argv[1]
directory = config['path']
pathstr = os.path.join(directory, filename)
path = Path(pathstr)
print(path.is_file())
print(pathstr)

with open(pathstr, "r") as read_file:
    racedata = json.load(read_file)
print(type(racedata))

# remove padding items
# if race_data.m_position < 0 hold the item
deletekeys = list()
for key, item in racedata['data'].items():
    print(racedata['data']['0'])
    if racedata['data'][key]['race_data']['position'] == 0:
        deletekeys.append(key)
print(deletekeys)
