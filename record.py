def getSessionID(packet):
    return packet['session_uid'].toString()


def trackLapData(packet, racedata, carstatus):
    lapdata = packet.to_dict()
    # print(lapdata['lap_data'])
    sessionID = getSessionID(lapdata)
    print(sessionID)
    exit(1)
    if carstatus and racedata.data and racedata.data[0] and racedata.data[0]['lap_data']:
        # for
        pass
    return racedata


def trackParticipantsData(packet, racedata):
    return racedata


def trackFinalClassification(packet, racedata):
    return racedata
