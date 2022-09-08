def getSessionID(packet):
    header = packet.to_dict().header
    return header['sessionUID'].toString()


def trackLapData(packet, racedata, carstatus):
    lapdata = packet.to_dict()
    # print(lapdata['lap_data'])
    sessionID = getSessionID(packet)
    print(sessionID)
    if carstatus and racedata.data and racedata.data[0] and racedata.data[0]['lap_data']:
        # for
        pass
    return racedata


def trackParticipantsData(packet, racedata):
    return racedata


def trackFinalClassification(packet, racedata):
    return racedata
