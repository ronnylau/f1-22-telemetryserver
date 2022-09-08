def getSessionID(data):
    return str(data['header']['session_uid'])


def trackLapHistoryData(packet, racedata, carstatus):
    lapdata = packet.to_dict()
    # print(lapdata['lap_data'])
    sessionID = getSessionID(lapdata)
    if carstatus:
        carstatus = carstatus.to_dict()
    if carstatus and \
            racedata['data']:
        index = 0
        print('while')
        while index < len(lapdata):
            newBest = lapdata[index]['lap_history_data']['lap_time_in_ms']
            print(newBest)
            exit(1)
            ++index
    return racedata


def trackLapData(packet, racedata, carstatus):
    return racedata
def trackParticipantsData(packet, racedata):
    return racedata


def trackFinalClassification(packet, racedata):
    return racedata
