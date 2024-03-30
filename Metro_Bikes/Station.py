class Station:
    """
    Class for a Station
    """
    def __init__(self, location, availablebikes, name):
        self.name = name
        self.location = location
        self.availablebikes = availablebikes