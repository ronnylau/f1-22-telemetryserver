#from matplotlib import pyplot as plt
i#mport fastf1.plotting
#import pandas as pd
import os
import json


def analyze_data():
    sessions = os.listdir('stored_telemetry')[1:]
    print('Stored sessions')
    print('')
    for count, session in enumerate(sessions):
        print(f'{count + 1}. {session}')

    print('')
    selected_session = input('Select session: ')

    try:
        int(selected_session)
        selected_session_name = sessions[int(selected_session) - 1]

        with open(f'./stored_telemetry/{selected_session_name}') as file:
            data = json.load(file)

            #fastf1.plotting.setup_mpl()

            track = data['track_name']
            #session = fastf1.get_session(2022, track, 'Q')

            session.load()
            #driver = session.laps.pick_driver('LEC').pick_fastest()
            #lec_car_data = driver.get_car_data()

            # Sort the laps by quickest time
            laps = data['laps']
            laps_sorted = sorted(laps, key=lambda k: len(laps[k]['telemetry']))

            fastest_lap_telemetry = None

            # Loop through laps, to find first fully completed lap
            for lap in laps_sorted:
                if data['laps'][lap]['lap_completed']:
                    fastest_lap_telemetry = data['laps'][lap]['telemetry']
                    break

                else:
                    pass

            if fastest_lap_telemetry:
                pass

            else:
                print('No complete lap was recorded during this session')

    except ValueError:
        print('Invalid input, exiting program!')
