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
    # open
    return racedata


def trackLapData(packet, racedata, carstatus):
    return racedata
def trackParticipantsData(packet, racedata):
    # update session id
    participantsdata = packet.to_dict()
    racedata['sessionID'] = getSessionID(participantsdata)

    #get participants
    participants = participantsdata['participants']
    for driver in participants:
        print(driver)
    exit(1)
    return racedata


def trackFinalClassification(packet, racedata):
    return racedata
