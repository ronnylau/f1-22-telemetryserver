from struct import unpack


class SessionData:
    def __init__(self, data):
        self.data = data
        self.session_data = unpack('<BbbBHBbBHHBBBBBB', data[24:43])
        self.track_length = self.session_data[4]
        self.session_type = self.session_data[5]
        self.session_name = self.session_types[self.session_type]
        self.track_id = self.session_data[6]
        self.track_name = self.tracks[self.track_id]

    tracks = [
        'Melbourne',
        'Paul Ricard',
        'Shanghai',
        'Sakhir',
        'Catalunya',
        'Monaco',
        'Montreal',
        'Silverstone',
        'Hockenheim',
        'Hungaroring',
        'Spa',
        'Monza',
        'Singapore',
        'Suzuka',
        'Abu Dhabi',
        'Texas',
        'Brazil',
        'Austria',
        'Sochi',
        'Mexico',
        'Baku',
        'Sakhir Short',
        'Texas Short',
        'Suzuka Short',
        'Hanoi',
        'Zandvoort',
        'Imola',
        'Portimao',
        'Jeddah',
        'Miami'
    ]

    session_types = [
        'unknown',
        'FP1',
        'FP2',
        'FP3',
        'Short P',
        'Q1',
        'Q2',
        'Q3',
        'Short Q',
        'One Shot Q',
        'R',
        'R2',
        'R3',
        'Time Trial'
    ]
