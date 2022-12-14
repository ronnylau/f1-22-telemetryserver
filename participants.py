import json

from driver import Driver


class Participants:
    participants = {}

    def update(self, data):
        for key, value in enumerate(data):
            self.participants[key] = Driver(value)

    def hasparticipants(self):
        if len(self.participants) > 0:
            return True
        else:
            return False

    def updateSetups(self, car_setups):
        print('aufruf Participants.updateSetups')
        print('beginn for schleife in Participants.updateSetups')
        for key, value in enumerate(self.participants):
            print('driver info')
            print(self.participants[key])
            print(f'key = {key} value = {value}')
            print('prüfe ob driver_id == 255')
            if self.participants[key].driver_id == 255:
                print('padding gefunden, continue')
                continue
            print('aufruf self.participants[key].getCar().updateSetup(car_setups[key])')
            print('daten:')
            print(car_setups[key])
            self.participants[key].getCar().updateSetup(car_setups[key])
            print('setup nach update')
            print(self.participants[key].getCar().setup)
        print('zeige alle setups nach den updates')
        for key, value in enumerate(self.participants):
            print('driver info')
            print(self.participants[key])
            print(f'key = {key} value = {value}')
            print(self.participants[key].getCar().setup)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def __str__(self):
        return self.toJSON()
