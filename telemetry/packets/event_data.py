from struct import unpack


class EventData:
    def __init__(self, data):
        self.data = data
        self.event_string_code = data[24:28].decode()
        self.event_data = data[28:]
