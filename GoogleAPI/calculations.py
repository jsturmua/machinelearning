def calculate_routes(startlocation, stations):
    distances = []
    origins = ["Perth, Australia",]
    destinations = []
    i = 0
    tempstations = []
    for station in stations:
        i = i+1
        tempstations.append(station)
