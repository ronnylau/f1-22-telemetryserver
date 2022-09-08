def getSessionID(data):
    return str(data['header']['session_uid'])


def trackLapHistoryData(packet, racedata, carstatus):
    print('begin processing laphistory data')
    lapdata = packet.to_dict()
    # print(lapdata['lap_data'])
    sessionID = getSessionID(lapdata)
    if carstatus:
        carstatus = carstatus.to_dict()
    print(lapdata)
    exit(1)
    return racedata


def trackLapData(packet, racedata, carstatus):
    return racedata
def trackParticipantsData(packet, racedata):
    return racedata


def trackFinalClassification(packet, racedata):
    return racedata
