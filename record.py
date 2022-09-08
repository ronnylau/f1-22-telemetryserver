def getSessionID(data):
    return str(data['header']['session_uid'])


def trackLapHistoryData(packet, racedata, carstatus):
    print('begin processing laphistory data')
    lapdata = packet.to_dict()
    # print(lapdata['lap_data'])
    sessionID = getSessionID(lapdata)
    if carstatus:
        carstatus = carstatus.to_dict()
    # try to find the best lap time
    return racedata


def trackLapData(packet, racedata, carstatus):
    print('Print Lap Data Package')
    print(packet.to_dict())
    exit(1)
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
            racedata['data'][index] = {}
            newdriver = {'driver': driver}
            # update dict with new driver
            racedata['data'][index].update(newdriver)
    return racedata


def trackFinalClassification(packet, racedata):
    return racedata
