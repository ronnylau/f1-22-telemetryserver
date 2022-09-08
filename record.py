def getSessionID(data):
    return str(data['header']['session_uid'])


def trackLapHistoryData(packet, racedata, carstatus):
    lapdata = packet.to_dict()
    # print(lapdata['lap_data'])
    sessionID = getSessionID(lapdata)
    carstatus = carstatus.to_dict()
    if carstatus and racedata.data and racedata.data[0] and racedata.data[0]['lap_data']:
        index = 0
        while index < len(lapdata):
            newBest = lapdata[index]['lap_history_data']['lap_time_in_ms']
            print(newBest)
            exit(1)
            ++index
    return racedata


def trackLapData(packet, racedata, carstatus):
    pass
def trackParticipantsData(packet, racedata):
    return racedata


def trackFinalClassification(packet, racedata):
    return racedata
