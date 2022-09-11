class Car:
    def __int__(self):
        self.motion = None
        self.lap = None
        self.setup = None
        self.telemetry = None
        self.status = None
        self.damage = None
        self.laphistory = None


class Driver:
    driver_id = 0
    network_id = 0
    team_id = 0
    race_number = 0
    name = ""

    def __int__(self, driver):
        self.driver_id = driver['driver_id']
        self.network_id = driver['network_id']
        self.team_id = driver['team_id']
        self.race_number = driver['race_number']
        self.name = driver['name']
