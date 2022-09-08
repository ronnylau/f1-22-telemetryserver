import copy
import json
import pickle
from pathlib import Path

from packets import *
from listener import TelemetryListener
import record


def getconfig():
    config = {
        'path': '.',
        'write-frequency': 2500,
        'prefix': '',
    }
    return config


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
        racedata = {
            'sessionID': None,
            'data': {}
        }
        lastwrite = None
        carstatus = None

        while True:
            packet = listener.get()
            if isinstance(packet, PacketMotionData):
                pass
            elif isinstance(packet, PacketSessionData):
                pass
            elif isinstance(packet, PacketLapData):
                print('Track Lap Data')
                racedata = record.trackLapData(packet, racedata, carstatus)
            elif isinstance(packet, PacketEventData):
                pass
            elif isinstance(packet, PacketParticipantsData):
                print('Track Participants Data')
                racedata = record.trackParticipantsData(packet, racedata)
            elif isinstance(packet, PacketCarSetupData):
                pass
            elif isinstance(packet, PacketCarTelemetryData):
                pass
            elif isinstance(packet, PacketCarStatusData):
                print('Track PacketCarStatusData')
                carstatus = packet
            elif isinstance(packet, PacketFinalClassificationData):
                print('Track PacketFinalClassificationData')
                racedata = record.trackFinalClassification(packet, racedata)
                # write data
                print('Session complete')
                # reset data
            elif isinstance(packet, PacketLobbyInfoData):
                pass
            elif isinstance(packet, PacketCarDamageData):
                pass
            elif isinstance(packet, PacketSessionHistoryData):
                print('Track Lap History Data')
                racedata = record.trackLapHistoryData(packet, racedata, carstatus)

                # json.dump(data.to_dict(), outfile, indent=4, sort_keys=True)
    except KeyboardInterrupt:
        print('Stop the car, stop the car Checo.')
        print('Stop the car, stop at pit exit.')
        print('Just pull over to the side.')


if __name__ == '__main__':
    main()
