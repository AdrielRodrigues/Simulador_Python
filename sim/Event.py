class Event:
    def __init__(self, type, flow, time):
        self.type = type
        self.flow = flow
        self.time = time

    def __lt__(self, other):
        return self.getTime() < other.getTime()

    def getType(self):
        return self.type

    def getFlow(self):
        return self.flow

    def getTime(self):
        return self.time
