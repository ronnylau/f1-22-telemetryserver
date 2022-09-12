import os

from session import Gamesession

from packets import *
from listener import TelemetryListener
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
session = None


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
    listener = _get_listener()
    global session
    try:
        racedata = {
            'sessionID': None,
            'data': {},
        }
        lastwrite = None
        carstatus = None
        with open('packets.log', 'w') as log:
            while True:
                # get the current packet
                packet = listener.get()
                packetdata = packet.to_dict()
                sessionID = packetdata['header']['session_uid']
                # skip packets without session_uid
                if sessionID == 0:
                    continue

                if isinstance(packet, PacketMotionData):
                    # skip motion packets
                    pass
                elif isinstance(packet, PacketSessionData):
                    log.write('\nPacketSessionData\n')
                    json.dump(packet.to_dict(), log)

                    # check if the session exist
                    if session and isinstance(session, Gamesession):
                        # update session
                        session.update(packetdata)
                    else:
                        session = Gamesession()
                        session.update(packetdata)
                elif isinstance(packet, PacketLapData):
                    # racedata = record.trackLapData(packet, racedata, carstatus)
                    # writefile(racedata)

                    log.write('\nPacketLapData\n')
                    json.dump(packet.to_dict(), log)
                elif isinstance(packet, PacketEventData):
                    log.write('\nPacketEventData\n')
                    json.dump(packet.to_dict(), log)

                    event = getEvent(packet.event_string_code)
                    # print(event)
                    if event == "SSTA":
                        # session starts
                        print('Session starts')
                    elif event == "SEND":
                        # session ends
                        print('Session ends')
                    elif event == "FTLP":
                        # a driver achieves the fastest lap
                        print('a driver achieves the fastest lap')
                    elif event == "RTMT":
                        # a driver retires
                        print('a driver retires')
                    elif event == "DRSE":
                        # drs was enabled by racecontrol
                        print("drs was enabled by racecontrol")
                    elif event == "DRSD":
                        # drs was disabeled by racecontrol
                        print("drs was disabled by racecontrol")
                    elif event == "TMPT":
                        # your teammate is in the pit
                        pass
                    elif event == "CHQF":
                        # the chequered flag has been waved
                        print("the chequered flag has been waved")
                    elif event == "RCWN":
                        # the racewinner was announced
                        print("the racewinner was announced")
                    elif event == "PENA":
                        # a penalty has been issued - details in the event
                        print("a penalty has been issued - details in the event")
                    elif event == "SPTP":
                        # speedtrap has been triggerd by fastest lap
                        print("speedtrap has been triggerd by fastest lap")
                    elif event == "STLG":
                        # start lights hase been changed
                        pass
                    elif event == "LGOT":
                        # lights out and here we go!
                        print("lights out and here we go!")
                    elif event == "DTSV":
                        # drive through penalty served
                        pass
                    elif event == "SGSV":
                        # stop and go penalty served
                        pass
                    elif event == "FLBK":
                        # flashback has been activated
                        pass
                    elif event == "BUTN":
                        # a button status has been changed
                        pass
                elif isinstance(packet, PacketParticipantsData):
                    # racedata = record.trackParticipantsData(packet, racedata)
                    # writefile(racedata)
                    log.write('\nPacketParticipantsData\n')
                    json.dump(packet.to_dict(), log)

                    # check if the session exist
                    if session and isinstance(session, Gamesession):
                        # if we have all participants already, skip the packet
                        if session.getparticipants().hasparticipants():
                            continue
                        # update participants
                        session.getparticipants().update(packetdata['participants'])
                    else:
                        # session does not exist, skip the paket
                        continue
                elif isinstance(packet, PacketCarSetupData):
                    log.write('\nPacketCarSetupData\n')
                    json.dump(packet.to_dict(), log)

                    # if we have all participants already, skip the packet
                    if session and not session.getparticipants().hasparticipants():
                        continue
                    # try to catch the setup data
                    session.updateCarSetups(packetdata['car_setups'])

                    print(session.getparticipants())
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
