from driver import Car, Driver


class Participants:
    participants = {}

    def __int__(self):
        self.car = Car()

    def update(self, data):
        for key, value in enumerate(data):
            self.participants[key] = Driver(value)

    def hasparticipants(self):
        if len(self.participants) > 0:
            return True
        else:
            return False
