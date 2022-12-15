import sys
sys.path.append("/usr/local/lib/python3.8/dist-packages")
import googlemaps
from googlemaps.maps import StaticMapMarker
from googlemaps.maps import StaticMapPath
from GoogleAPI.Route import Route
import geopy.distance
from geopy.geocoders import Nominatim
import json
import numpy as np
import pandas as pd

def calculate_routes(startlocation, stations):
    geolocation = turn_adress_into_coords(startlocation)
    routes = []
    for station in stations:
        routes.append(calculate_route_geopy(geolocation, station))
    return routes


def calculate_route_geopy(startlocation, station):
    coords_1 = (startlocation.latitude, startlocation.longitude)
    coords_2 = (station._location.y, station._location.y)
    distance = geopy.distance.geodesic(coords_1, coords_2).m
    return Route(startlocation, station, distance)
    

def turn_adress_into_coords(location):
    geolocator = Nominatim(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52')
    geolocation = geolocator.geocode(location)
    return geolocation

def get_nearest_stations(routes, quantity):
    routes.sort(key=lambda x: x.distance)
    nearest_stations = []
    # arr = np.array(routes, dtype)
    # arr = np.sort(arr, order='distance')
    for i in range (0, quantity):
        nearest_stations.append(routes[i].station)
    return nearest_stations


def calculate_route_googlemaps(startlocation, station, travelmode):
    gmaps = googlemaps.Client(key='insert_key')
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52'}
    gmaps.requests_kwargs.update({
            "headers": headers,
            "timeout": 2,
        })
    origins = [startlocation,]
    destinationstring = str(station._location.y) + ", " + str(station._location.x)
    matrix = gmaps.directions(origins, destinationstring, mode=travelmode)
    duration_as_text = matrix['rows'][0]['elements'][0]['duration']['text']
    duration_value = matrix['rows'][0]['elements'][0]['duration']['value']
    route = Route(startlocation, station, duration_value, duration_as_text)
    
    return route