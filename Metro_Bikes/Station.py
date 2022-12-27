class Station:
    def __init__(self, location, availablebikes, name):
        self.name = name
        self._location = location
        self.availablebikes = availablebikes