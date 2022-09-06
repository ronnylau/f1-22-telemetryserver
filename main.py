import copy
import json
import pickle
from pathlib import Path

from packets import HEADER_FIELD_TO_PACKET_TYPE

from listener import TelemetryListener


def _get_listener():
    try:
        print('Starting listener on localhost:20777')
        return TelemetryListener()
    except OSError as exception:
        print(f'Unable to setup connection: {exception.args[1]}')
        print('Failed to open connector, stopping.')
        exit(127)


def main():
    listener = _get_listener()

    try:
        with open('json_data.json', 'w') as outfile:
        while True:
            packet = listener.get()
            #print(json.dumps(packet.to_dict(), indent=4, sort_keys=True))
            json.dump(packet.to_dict(), outfile, indent=4, sort_keys=True)
    except KeyboardInterrupt:
        print('Stop the car, stop the car Checo.')
        print('Stop the car, stop at pit exit.')
        print('Just pull over to the side.')


if __name__ == '__main__':
    main()