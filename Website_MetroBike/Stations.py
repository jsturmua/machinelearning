import requests
import json
#import pandas

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Availablebikes:
    def __init__(self, amount_free_bikes, amount_free_docks, amount_classic_bikes, amount_smart_bikes, amount_electric_bikes, amount_trikes):
        self.amount_free_bikes = amount_free_bikes
        self.amount_free_docks = amount_free_docks
        self.amount_classic_bikes = amount_classic_bikes
        self.amount_smart_bikes = amount_smart_bikes
        self.amount_electric_bikes = amount_electric_bikes
        self.amount_trikes = amount_trikes

class Station:
    def __init__(self, location, avaivablebikes, name):
        self.name = name
        self._location = location
        self._avaivablebikes = avaivablebikes


class Stations:
    def __init__(self):
        self.stations = []
        self.parse_json()

    def add_station(self, station):
        self.station.append(station)

    def definestations(self):
        self.stations = []
        

    def parse_json(self):
        header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52'}
        r = requests.get("https://bikeshare.metro.net/stations/json/", headers=header)
        jsoninput = json.loads(r.content)
        for object in jsoninput['features']:
            x_coordinate = object['geometry']['coordinates'][0]
            y_coordinate = object['geometry']['coordinates'][1]
            location = Location(x_coordinate, y_coordinate)
            name = object['properties']['name']
            amount_free_bikes = object['properties']['bikesAvailable']
            amount_free_docks = object['properties']['docksAvailable']
            amount_classic_bikes = object['properties']['classicBikesAvailable']
            amount_smart_bikes = object['properties']['smartBikesAvailable']
            amount_electric_bikes = object['properties']['electricBikesAvailable']
            amount_trikes = object['properties']['trikesAvailable']
            bikesavailable = Availablebikes(amount_free_bikes, amount_free_docks, amount_classic_bikes, amount_smart_bikes, amount_electric_bikes, amount_trikes)
            
            self.stations.append(Station(location, bikesavailable, name))