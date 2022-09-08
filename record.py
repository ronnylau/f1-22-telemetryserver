def getSessionID(packet):
    return packet.get_value('header').m_sessionUID.toString()


def trackLapData(packet, racedata, carstatus):
    lapdata = packet.get_value('m_lapData')
    print(lapdata)
    pass
    sessionID = getSessionID(packet)
    if carstatus and racedata.data and racedata.data[0] and racedata.data[0]['lap_data']:
        # for
        pass
    return racedata


def trackParticipantsData(packet, racedata):
    return racedata


def trackFinalClassification(packet, racedata):
    return racedata
