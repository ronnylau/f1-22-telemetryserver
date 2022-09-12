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
        for key, value in enumerate(self.participants):
            print(f'Write Setup data for Driver {self.participants[key].driver_id}')
            print(self.participants[key])
            self.participants[key].getCar().updateSetup(car_setups[key])

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                         sort_keys=True, indent=4)

    def __str__(self):
        return self.toJSON()
