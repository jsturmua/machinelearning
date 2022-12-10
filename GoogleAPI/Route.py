class Route:
    def __init__(self, startlocation, station, value, distance_as_text) -> None:
        self.startlocation = startlocation
        self.station = station
        self.value = value
        self.distance_as_text = distance_as_text