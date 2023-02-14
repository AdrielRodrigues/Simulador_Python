class Lightpath:
    def __init__(self, id, source, destination, path, modulationLevel):
        self.id = int(id)
        self.source = int(source)
        self.destination = int(destination)
        self.path = path
        self.modulationLevel = int(modulationLevel)

    def __lt__(self, other):
        return self.getID() < other.getID()

    def getID(self):
        return self.id

    def getSource(self):
        return self.source

    def getDestination(self):
        return self.destination

    def getPath(self):
        return self.path

    def getModulationLevel(self):
        return self.modulationLevel
