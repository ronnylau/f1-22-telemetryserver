from struct import unpack


class LapData:
    def __init__(self, data):
        self.data = data
        self.lap_data = unpack('<IIHHfffBBBBBBBBBBBBBHH', data[24:65])
        self.last_lap_ms = self.lap_data[0]
        self.current_lap_ms = self.lap_data[1]
        self.sector_1_ms = self.lap_data[2]
        self.sector_2_ms = self.lap_data[3]
        self.lap_distance = self.lap_data[4]
        self.current_lap = self.lap_data[8]
        self.driver_status = self.lap_data[18]
