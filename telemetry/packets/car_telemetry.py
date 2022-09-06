from struct import unpack


class CarTelemetryData:
    def __init__(self, data):
        self.data = data
        self.telemetry_data = unpack('<HfffBbHBBHHBBHfB', data[24:57])
        self.speed = self.telemetry_data[0]
        self.throttle = self.telemetry_data[1]
        self.steer = self.telemetry_data[2]
        self.brake = self.telemetry_data[3]
        self.clutch = self.telemetry_data[4]
        self.gear = self.telemetry_data[5]
        self.engine_rpm = self.telemetry_data[6]
        self.drs = self.telemetry_data[7]
