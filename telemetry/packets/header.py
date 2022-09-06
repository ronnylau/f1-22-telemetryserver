from struct import unpack


class PacketHeader:
    def __init__(self, data):
        self.data = data
        self.header_data = unpack('<HBBBBQfIBB', data[0:24])
        self.packet_format = self.header_data[0]
        self.game_major_version = self.header_data[1]
        self.game_minor_version = self.header_data[2]
        self.packet_version = self.header_data[3]
        self.packet_id = self.header_data[4]
        self.session_uid = self.header_data[5]
        self.session_timestamp = self.header_data[6]
        self.frame_id = self.header_data[7]
        self.player_car_index = self.header_data[8]
        self.secondary_player_car_index = self.header_data[9]
