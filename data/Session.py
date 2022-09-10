import Participants


class Session:
    def __int__(self):
        self.event = None
        self.participants = Participants()
        self.classification = None
        self.lobbyinfo = None

    def getevent(self):
        return self.event

    def getparticipants(self):
        return self.participants

    def getclassification(self):
        return self.classification

    def getlobbyinfo(self):
        return self.lobbyinfo
