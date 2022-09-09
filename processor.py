import os
import sys
import json

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
path = os.path.join(directory, filename)
print(path.is_file())

with open(path) as json_file:
    racedata = json.load(json_file)
    print(racedata)

    # remove padding items
    # if race_data.m_position < 0 hold the item
    deletekeys = list()
    for index, item in enumerate(racedata['data']):
        if racedata['data'][index]['race_data']['position'] == 0:
            deletekeys.append(index)
    print(deletekeys)


