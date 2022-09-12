import json

from driver import Car, Driver


class Participants:
    participants = {}

    def __int__(self):
        pass

    def update(self, data):
        for key, value in enumerate(data):
            self.participants[key] = Driver(value)

    def hasparticipants(self):
        if len(self.participants) > 0:
            return True
        else:
            return False

    def updateSetups(self, car_setups):
        print(self.participants)
        for key, value in enumerate(self.participants):
            self.participants[key].getCar().updateSetup(car_setups[key])

    def toJSON(self):

        print(json.dumps(self, default=lambda o: o.__dict__,
                         sort_keys=True, indent=4))
        for key, value in enumerate(self.participants):
            print(self.participants[key])

    def __str__(self):
        return self.toJSON()
