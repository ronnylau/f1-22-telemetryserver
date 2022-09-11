from car import Car


class Participants:
    participants = {}

    def __int__(self):
        self.car = Car()

    def update(self, data):
        for key, value in data:
            self.participants[key] = value
