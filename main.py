import copy
import json
import pickle
from pathlib import Path

from packets import HEADER_FIELD_TO_PACKET_TYPE
from listener import TelemetryListener
import record


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
        while True:
            packet = listener.get()
            #print('packet: ' + packet.to_json())
            header = packet.get_value('header')

            key = (header.get('packet_format'), header.get('packet_version'), header.get('packet_id'))
            print(key)
            print(HEADER_FIELD_TO_PACKET_TYPE.get(key))
            if HEADER_FIELD_TO_PACKET_TYPE[key] == 'PacketMotionData':
                print('Track Motion Data')
                #data = record.trackLapData(packet)
            elif HEADER_FIELD_TO_PACKET_TYPE[key] == 'PacketSessionData':
                print('Track Session Data')
            elif HEADER_FIELD_TO_PACKET_TYPE[key] == 'PacketLapData':
                print('Track Lap Data')
            elif HEADER_FIELD_TO_PACKET_TYPE[key] == 'PacketEventData':
                print('Track Event Data')
            elif HEADER_FIELD_TO_PACKET_TYPE[key] == 'PacketParticipantsData':
                print('Track Participants Data')
            elif HEADER_FIELD_TO_PACKET_TYPE[key] == 'PacketCarSetupData':
                print('Track Car Setup Data')
            elif HEADER_FIELD_TO_PACKET_TYPE[key] == 'PacketCarTelemetryData':
                print('Track PacketCarTelemetryData')
            elif HEADER_FIELD_TO_PACKET_TYPE[key] == 'PacketCarStatusData':
                print('Track PacketCarStatusData')
            elif HEADER_FIELD_TO_PACKET_TYPE[key] == 'PacketFinalClassificationData':
                print('Track PacketFinalClassificationData')
            elif HEADER_FIELD_TO_PACKET_TYPE[key] == 'PacketLobbyInfoData':
                print('Track PacketLobbyInfoData')
            elif HEADER_FIELD_TO_PACKET_TYPE[key] == 'PacketCarDamageData':
                print('Track PacketCarDamageData')
            elif HEADER_FIELD_TO_PACKET_TYPE[key] == 'PacketSessionHistoryData':
                print('Track PacketSessionHistoryData')

                # json.dump(data.to_dict(), outfile, indent=4, sort_keys=True)
    except KeyboardInterrupt:
        print('Stop the car, stop the car Checo.')
        print('Stop the car, stop at pit exit.')
        print('Just pull over to the side.')


if __name__ == '__main__':
    main()
