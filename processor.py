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
filename = sys.argv[0]
directory = config['path']
pathstr = os.path.join(directory, filename)
path = Path(pathstr)
print(path.is_file())
print(path)

contents = json.loads(pathstr)

# remove padding items
# if race_data.m_position < 0 hold the item
deletekeys = list()
for index, item in enumerate(racedata['data']):
    if racedata['data'][index]['race_data']['position'] == 0:
        deletekeys.append(index)
print(deletekeys)


