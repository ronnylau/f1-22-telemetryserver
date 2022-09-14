import json
from utils import DictDiffer

class Driver:
    class Car:
        def __init__(self):
            self.motion = None
            self.lap = None
            self.setup = {}
            self.telemetry = None
            self.status = None
            self.damage = {
                "tyres_wear": [0.0, 0.0, 0.0, 0.0],
                "tyres_damage": [0, 0, 0, 0],
                "brakes_damage": [0, 0, 0, 0],
                "front_left_wing_damage": 0,
                "front_right_wing_damage": 0,
                "rear_wing_damage": 0,
                "floor_damage": 0,
                "diffuser_damage": 0,
                "sidepod_damage": 0,
                "drs_fault": 0,
                "gear_box_damage": 0,
                "engine_damage": 0,
                "engine_mguhwear": 0,
                "engine_eswear": 0,
                "engine_cewear": 0,
                "engine_icewear": 0,
                "engine_mgukwear": 0,
                "engine_tcwear": 0}
            self.laphistory = None

        def updateSetup(self, setup):
            for key, value in enumerate(setup):
                self.setup[value] = setup.get(value)

        def updateDamage(self, damage):
            diff = DictDiffer(self.damage, damage)
            for key, index in enumerate(diff.changed()):
                self.damage[key] = damage[key]

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
