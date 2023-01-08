import requests
import json
from Metro_Bikes.Location import Location
from Metro_Bikes.AvailableBikes import AvailableBikes
from Metro_Bikes.Station import Station
        

def parse_json():
    """
    Get data of MetroBike website and store this information in the class station
    return value: Array with stations
    """
    stations = []
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
        bikesavailable = AvailableBikes(amount_free_bikes, amount_free_docks, amount_classic_bikes, amount_smart_bikes, amount_electric_bikes, amount_trikes)
        
        stations.append(Station(location, bikesavailable, name))
    return stations