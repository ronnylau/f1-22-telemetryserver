class Car:
    def __int__(self):
        self.motion = None
        self.lap = None
        self.setup = {}
        self.telemetry = None
        self.status = None
        self.damage = None
        self.laphistory = None

    def updateSetup(self, setup):
        for key, value in enumerate(setup):
            self.setup[key] = value


class Driver:
    driver_id = 0
    network_id = 0
    team_id = 0
    race_number = 0
    name = ""
    car = Car()

    def __init__(self, driver):
        self.driver_id = driver['driver_id']
        self.network_id = driver['network_id']
        self.team_id = driver['team_id']
        self.race_number = driver['race_number']
        self.name = driver['name']
        self.car = Car()

    def getCar(self):
        return self.car
