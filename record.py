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
    if lapdata.best_lap_time_lap_num > 0:
        print(lapdata['lap_history_data'][lapdata.best_lap_time_lap_num-1]['lap_time_in_ms'])
        exit(1)
    return racedata


def trackLapData(packet, racedata, carstatus):
    return racedata
def trackParticipantsData(packet, racedata):
    return racedata


def trackFinalClassification(packet, racedata):
    return racedata
