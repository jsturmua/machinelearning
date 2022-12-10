from MetroBike.Stations import Station, Stations
import sys
sys.path.append("/usr/local/lib/python3.8/dist-packages")
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyCj8S_a8wIqEiv0gx8XfVtdSJqDXvJb3jo')
import requests
class Distance:
    def __init__(self, startlocation, station, value, distance_as_text) -> None:
        self.startlocation = startlocation
        self.station = station
        self.value = value
        self.distance_as_text = distance_as_text


class Distances:
    """
    Describes different distances between to locations
    """
    def __init__(self, startlocation, stations):
        self.distances = []
        i = 0
        for station in stations.stations:
            i = i + 1
            tempstations = []
            destinationstring = destinationstring + str(station._location.y) + "%2C" + str(station._location.x) + "|"
            if i == 25:
                tempstations.append(station)
                url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=Washington%2C%20DC&mode=walking" + destinationstring + "&units=imperial&key=AIzaSyCj8S_a8wIqEiv0gx8XfVtdSJqDXvJb3jo"
                response = requests.request("GET", url)
                datei = open('temp.json','a')
                datei.write(response.text)
                destinationstring = "&destinations="
                i = 0
                tempstations = []
                self._safe_distances(response.text,startlocation, tempstations)


    def _calculate_distances(self, startlocation, stations):
        i = 0
        for station in stations.stations:
            
            tempstations = []
            destinationstring = destinationstring + str(station._location.y) + "%2C" + str(station._location.x) + "|"
            if i == 25:
                tempstations.append(station)
                url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=Washington%2C%20DC&mode=walking" + destinationstring + "&units=imperial&key=AIzaSyCj8S_a8wIqEiv0gx8XfVtdSJqDXvJb3jo"
                response = requests.request("GET", url)
                datei = open('temp.json','a')
                datei.write(response.text)
                destinationstring = "&destinations="
                i = 0
                tempstations = []
                self._safe_distances(response.text,startlocation, tempstations)
    
    def _safe_distances(self, json_distances,startlocation, tempstations):
        for i = 0 
