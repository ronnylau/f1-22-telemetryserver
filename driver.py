import json


class Driver:
    driver_id = 0
    network_id = 0
    team_id = 0
    race_number = 0
    name = ""

    class Car:
        def __init__(self):
            self.motion = None
            self.lap = None
            self.setup = {}
            self.telemetry = None
            self.status = None
            self.damage = None
            self.laphistory = None

        def updateSetup(self, setup):
            print('aufruf von Car.updatesetup mit Daten:')
            print(setup)
            print('beginn for schleife in Car.updatesetup')
            for key, value in enumerate(setup):
                print(f'key = {key} value={value}')
                print(f'setze neuen wert {value} auf {setup.get(value)}')
                self.setup[value] = setup.get(value)

        def toJSON(self):
            return json.dumps(self, default=lambda o: o.__dict__,
                              sort_keys=True, indent=4)

        def __str__(self):
            return self.toJSON()

    def __init__(self, driver):
        self.driver_id = driver['driver_id']
        self.network_id = driver['network_id']
        self.team_id = driver['team_id']
        self.race_number = driver['race_number']
        self.name = driver['name']
        self.car = self.Car()

    def getCar(self):
        return self.car

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def __str__(self):
        return f"\tDriverID {self.driver_id} NetworkID {self.network_id} TeamID {self.team_id} Name {self.name}"
