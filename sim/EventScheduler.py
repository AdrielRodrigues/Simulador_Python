class EventScheduler:
    def __init__(self):
        self.events = []

    # TODO: Elaborar um método mais eficiente de enfileirar os eventos
    def addEvent(self, event):
        self.events.append(event)

    def getEvents(self):
        return self.events
