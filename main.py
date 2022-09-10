import copy
import json
import os
import pickle
from pathlib import Path

from packets import *
from listener import TelemetryListener
import record
import time


def getconfig():
    config = {
        'path': '.',
        'write-frequency': 5,
        'prefix': '',
    }
    return config


lastwrite = 0
sessionID = None


def writefile(racedata, force=0):
    global lastwrite
    config = getconfig()
    print('force=' + str(force))
    if racedata and (force or ((time.time() - lastwrite) > config['write-frequency'])):
        filename = config['prefix'] + 'racedata_' + racedata['sessionID'] + '.json'
        directory = config['path']
        path = os.path.join(directory, filename)
        print(f'Write data to file {path}')
        print(force)
        with open(path, 'w') as f:
            f.write(to_json(racedata))
        print('Job done!')
        lastwrite = time.time()


def _get_listener():
    try:
        print('Starting listener on localhost:20777')
        return TelemetryListener()
    except OSError as exception:
        print(f'Unable to setup connection: {exception.args[1]}')
        print('Failed to open connector, stopping.')
        exit(127)


def getEvent(eventStringCode):
    eventCode = chr(eventStringCode[0]) + chr(eventStringCode[1]) + chr(eventStringCode[2]) + chr(eventStringCode[3])
    return eventCode


def main():
    global sessionID
    listener = _get_listener()

    try:
        racedata = {
            'sessionID': None,
            'data': {},
        }
        lastwrite = None
        carstatus = None
        with open('packets.log', 'w') as log:
            while True:
                packet = listener.get()

                packetdata = packet.to_dict()

                # skip packets without session_uid
                if packetdata['session_uid'] == 0:
                    pass

                if isinstance(packet, PacketMotionData):
                    # skip motion packets
                    pass
                elif isinstance(packet, PacketSessionData):
                    log.write('\nPacketSessionData\n')
                    json.dump(packet.to_dict(), log)
                elif isinstance(packet, PacketLapData):
                    # racedata = record.trackLapData(packet, racedata, carstatus)
                    # writefile(racedata)

                    log.write('\nPacketLapData\n')
                    json.dump(packet.to_dict(), log)
                elif isinstance(packet, PacketEventData):
                    log.write('\nPacketEventData\n')
                    json.dump(packet.to_dict(), log)

                    event = getEvent(packet.event_string_code)
                    print(event)

                elif isinstance(packet, PacketParticipantsData):
                    # racedata = record.trackParticipantsData(packet, racedata)
                    # writefile(racedata)
                    log.write('\nPacketParticipantsData\n')
                    json.dump(packet.to_dict(), log)
                elif isinstance(packet, PacketCarSetupData):
                    log.write('\nPacketCarSetupData\n')
                    json.dump(packet.to_dict(), log)
                elif isinstance(packet, PacketCarTelemetryData):
                    log.write('\nPacketCarTelemetryData\n')
                    json.dump(packet.to_dict(), log)
                elif isinstance(packet, PacketCarStatusData):
                    carstatus = packet

                    log.write('\nPacketCarStatusData\n')
                    json.dump(packet.to_dict(), log)
                elif isinstance(packet, PacketFinalClassificationData):
                    # print('Track PacketFinalClassificationData')
                    # racedata = record.trackFinalClassification(packet, racedata)
                    # write data
                    # print('Session complete')
                    # writefile(racedata, force=1)
                    # reset data
                    """if (racedata['sessionID'] != sessionID):
                        racedata = {
                            'sessionID': None,
                            'data': {},
                        }"""
                    # sessionID = racedata['sessionID']

                    log.write('\nPacketFinalClassificationData\n')
                    json.dump(packet.to_dict(), log)
                elif isinstance(packet, PacketLobbyInfoData):
                    log.write('\nPacketLobbyInfoData\n')
                    json.dump(packet.to_dict(), log)
                elif isinstance(packet, PacketCarDamageData):
                    log.write('\nPacketCarDamageData\n')
                    json.dump(packet.to_dict(), log)
                elif isinstance(packet, PacketSessionHistoryData):
                    # racedata = record.trackLapHistoryData(packet, racedata, carstatus)
                    log.write('\nPacketSessionHistoryData\n')
                    json.dump(packet.to_dict(), log)
    except KeyboardInterrupt:
        print('Stop the car, stop the car Checo.')
        print('Stop the car, stop at pit exit.')
        print('Just pull over to the side.')


if __name__ == '__main__':
    main()
