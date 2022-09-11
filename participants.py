from driver import Car, Driver


class Participants:
    participants = {}

    def __int__(self):
        self.car = Car()

    def update(self, data):
        print(data)
        for key, value in enumerate(data):
            self.participants[key] = Driver(value)
