from telemetry.packets import session_data, lap_data, event_data, header, car_telemetry
import socket
import json
import datetime


def receive_data():
    UDP_IP = '192.168.10.1'
    UDP_PORT = 27001

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    telemetry = {
        'laps': {},
        'track_name': None,
        'session_name': None
    }
    print('Start capture')
    lap_data_received = False
    telemetry_data_received = False

    while True:
        data, addr = sock.recvfrom(2048)
        packet_id = header.PacketHeader(data).packet_id
        print(packet_id)
        if packet_id == 0:
            # Motion Data
            pass

        elif packet_id == 1:
            # Session Data
            track_length = session_data.SessionData(data).track_length
            track_name = session_data.SessionData(data).track_name
            session_name = session_data.SessionData(data).session_name

        elif packet_id == 2:
            # Lap Data
            lap_time = lap_data.LapData(data).current_lap_ms
            lap_number = lap_data.LapData(data).current_lap
            lap_distance = lap_data.LapData(data).lap_distance

            lap_data_received = True

        elif packet_id == 3:
            # Event Data
            event_string_code = event_data.EventData(data).event_string_code

        elif packet_id == 4:
            # Participants
            pass

        elif packet_id == 5:
            # Car Setups
            pass

        elif packet_id == 6:
            # Telemetry Data
            speed = car_telemetry.CarTelemetryData(data).speed
            throttle = car_telemetry.CarTelemetryData(data).throttle
            steer = car_telemetry.CarTelemetryData(data).steer
            brake = car_telemetry.CarTelemetryData(data).brake
            gear = car_telemetry.CarTelemetryData(data).gear

            telemetry_data_received = True

        elif packet_id == 7:
            # Car Status
            pass

        elif packet_id == 8:
            # Final Classification
            pass

        elif packet_id == 9:
            # Lobby Info
            pass

        elif packet_id == 10:
            # Car Damage
            pass

        elif packet_id == 11:
            # Session History
            pass

        else:
            print('Packet ID wrong')

        if lap_data_received and telemetry_data_received:
            if lap_time > 0 and lap_distance > 0:
                lap = f'Lap {lap_number}'

                try:
                    telemetry['laps'][lap]

                except KeyError:
                    telemetry['laps'][lap] = {}
                    telemetry['laps'][lap]['telemetry'] = []

                telemetry['laps'][lap]['telemetry'].append({
                    'Lap Time': lap_time,
                    'Lap Distance': lap_distance,
                    'Speed': speed,
                    'Throttle': throttle,
                    'Steer': steer,
                    'Brake': brake,
                    'Gear': gear
                })

                lap_data_received = False
                telemetry_data_received = False

        if event_string_code == 'SEND':
            # Close Socket when Session ends
            break

    for lap_key in telemetry['laps'].keys():
        lap_total_distance = telemetry['laps'][lap_key]['telemetry'][-1]['Lap Distance']

        if track_length - 5 < lap_total_distance < track_length + 5:
            telemetry['laps'][lap_key]['lap_completed'] = True

        else:
            telemetry['laps'][lap_key]['lap_completed'] = False

    telemetry['track_name'] = track_name
    telemetry['session_name'] = session_name

    # Write the telemetry data to JSON file for later use
    print('Saving data...')
    date = datetime.datetime.now()
    date_string = f'{date.year}.{date.month}.{date.day} - {date.hour}.{date.minute}.{date.second}'
    file_name = f'{track_name} {session_name} {date_string}.json'
    with open(f'./stored_telemetry/{file_name}', 'w') as outfile:
        json.dump(telemetry, outfile, indent=4)

    return telemetry


