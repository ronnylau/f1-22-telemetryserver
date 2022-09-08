import json


def getSessionID(data):
    return str(data['header']['session_uid'])


def trackLapHistoryData(packet, racedata, carstatus):
    print('begin processing laphistory data')

    # get dict
    # lapdata = packet.to_dict()

    # carIndex = lapdata['car_idx']


    #try to find a new best lap

    #current best lap


    # update session id
    # racedata['sessionID'] = getSessionID(lapdata)




    return racedata


def trackLapData(packet, racedata, carstatus):
    # print('Print Lap Data Package')
    # print(json.dumps(packet.to_dict(), sort_keys=True, indent=4))

    #get dict
    lapdata = packet.to_dict()

    # update session id
    racedata['sessionID'] = getSessionID(lapdata)

    #unpack carstatus
    if carstatus is None:
        # car status is not in place yet
        return racedata

    carstatus = carstatus.to_dict()

    laps = lapdata['lap_data']

    for index, lap in enumerate(laps):
        if index in racedata['data'].keys():

            # try to find best lap
            if 'bestLapTime' not in racedata['data'][index]['costom'].keys():
                #first lap, set to 0
                racedata['data'][index]['costom']['bestLapTime'] = 0

            # check if the last lap was the fastest
            if lap['last_lap_time_in_ms'] is not 0 and (racedata['data'][index]['costom']['bestLapTime'] > lap['last_lap_time_in_ms']):
                #last lap was the new fastest lap for the driver
                racedata['data'][index]['costom']['bestLapTime'] = lap['last_lap_time_in_ms']
                racedata['data'][index]['costom']['bestLapTyre'] = carstatus['car_status_data'][index]['visual_tyre_compound']
                racedata['data'][index]['costom']['bestLapTyreAge'] = carstatus['car_status_data'][index]['tyres_age_laps']

            newlap = {'lap_data': lap}
            racedata['data'][index].update(newlap)
    return racedata


def trackParticipantsData(packet, racedata):
    # update session id
    participantsdata = packet.to_dict()
    racedata['sessionID'] = getSessionID(participantsdata)

    #get participants
    participants = participantsdata['participants']
    for index, driver in enumerate(participants):
        #check for existing key
        if index not in racedata['data'].keys():
            # add new index
            racedata['data'][index] = {'costom' : {}}
            newdriver = {'driver': driver}
            # update dict with new driver
            racedata['data'][index].update(newdriver)
    return racedata


def trackFinalClassification(packet, racedata):
    return racedata
