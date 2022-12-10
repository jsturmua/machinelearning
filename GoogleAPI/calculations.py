import sys
sys.path.append("/usr/local/lib/python3.8/dist-packages")
import googlemaps

def calculate_routes(startlocation, stations):
    gmaps = googlemaps.Client(key='AIzaSyCj8S_a8wIqEiv0gx8XfVtdSJqDXvJb3jo')
    distances = []
    origins = [startlocation,]
    destinations = []
    i = 0
    tempstations = []
    for station in stations:
        i = i+1
        tempstations.append(station)
        temp_destination_string = station.name + "[" + station.location.y + ", " + station.location.x + "]"
        destinations.append(temp_destination_string)
