from participants import Participants
from driver import Driver
import json


class Gamesession:
    event = None
    participants = {}
    classification = None
    lobbyinfo = None

    total_laps = 0
    track_length = 0
    session_type = 0
    track_id = 0
    formula = 0
    network_game = 0

    def __init__(self):
        self.event = None
        self.participants = {}
        self.classification = None
        self.lobbyinfo = None

    def update(self, packet):
        self.total_laps = packet['total_laps']
        self.track_length = packet['track_length']
        self.session_type = packet['session_type']
        self.track_id = packet['track_id']
        self.formula = packet['formula']
        self.network_game = packet['network_game']

    def addParticipant(self, key, driverInfo):
        for index, value in enumerate(driverInfo):
            self.participants[key] = Participants()
    def getevent(self):
        return self.event

    def getparticipants(self):
        return self.participants

    def getclassification(self):
        return self.classification

    def getlobbyinfo(self):
        return self.lobbyinfo

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def __str__(self):
        return f"Total Laps: {self.total_laps} Track lenght {self.track_length} Session Type {self.session_type}" \
               f"Track ID {self.track_id}"

    def updateCarSetups(self, car_setups):
        print('aufruf session.updateCarSetups')
        print('uebergabe an self.participants.updateSetups')
        self.participants.updateSetups(car_setups)
