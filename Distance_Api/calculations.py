import sys
sys.path.append("/usr/local/lib/python3.8/dist-packages")
import googlemaps
from Distance_Api.Route import Route
import geopy.distance
from geopy.geocoders import Nominatim
import numpy as np
import pandas as pd

def calculate_routes(startlocation, stations):
    """
    Calculate all routes between startlocation and stations
    Return value: Array of routes
    """
    routes = []
    for station in stations:
        routes.append(calculate_route_geopy(startlocation, station))
    return routes


def calculate_route_geopy(startlocation, station):
    """
    Calculates a route between a location and a station
    Return value: Route
    """
    coords_1 = (startlocation.latitude, startlocation.longitude)
    coords_2 = (station._location.y, station._location.x)
    distance = geopy.distance.geodesic(coords_1, coords_2).m
    return Route(startlocation, station, distance)

def turn_adress_into_geolocation(location):
    """
    Turns adress into an geolocation object
    Return value: geolocation
    """
    geolocator = Nominatim(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52')
    geolocation = geolocator.geocode(location)
    return geolocation

def get_nearest_stations(startlocation, stations, quantity):
    """
    Sorts the stations by distance and puts specified quantity of stations in an array
    Return value: Array of stations
    """
    routes = calculate_routes(startlocation, stations)
    routes.sort(key=lambda x: x.distance)
    nearest_stations = []
    amount = 0
    for route in routes:
        if route.station.availablebikes.amount_free_bikes != 0:
            nearest_stations.append(route.station)
            amount = amount + 1
        if amount == quantity:
            break
    return nearest_stations

def get_nearest_stations_with_docs(startlocation, stations, quantity):
    """
    Sorts the stations by distance and puts specified quantity of stations in an array
    Return value: Array of stations
    """
    routes = calculate_routes(startlocation, stations)
    routes.sort(key=lambda x: x.distance)
    nearest_stations = []
    amount = 0
    for route in routes:
        if route.station.availablebikes.amount_free_docks != 0:
            nearest_stations.append(route.station)
            amount = amount + 1
        if amount == quantity:
            break
    return nearest_stations

def get_best_route(startlocation, destinationlocation, stations):
    """
    Calculates a route between two locations using MetroBike stations
    Return value: Array of used stations
    """
    nearest_startstation=get_nearest_stations(startlocation, stations, 1)
    nearest_endstation=get_nearest_stations_with_docs(destinationlocation, stations, 1)
    #Will ich das wirklich machen?
    #nearest_startstation = get_nearest_stations(destinationlocation, nearest_startstations, 1)
    #nearest_endstation = get_nearest_stations_with_docs(startlocation, nearest_endstations, 1)
    stations = [nearest_startstation[0], nearest_endstation[0]]
    return stations

    
def create_google_maps_route(startlocation, endlocation, stations):
    gmaps = googlemaps.Client(key='AIzaSyCj8S_a8wIqEiv0gx8XfVtdSJqDXvJb3jo')
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52'}
    gmaps.requests_kwargs.update({
            "headers": headers,
            "timeout": 2,
        })
    origins = (startlocation.latitude, startlocation.longitude)
    destination = (endlocation.latitude, endlocation.longitude)
    waypoint_stations = []
    for station in stations:
        waypoint_stations.append((station._location.y, station._location.x))
    matrix = gmaps.directions(origins, destination, waypoints=waypoint_stations)
    return matrix

#optimize old implementation
def calculate_route_googlemaps(startlocation, station, travelmode): #not in use
    gmaps = googlemaps.Client(key='')
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