import sys
sys.path.append("/usr/local/lib/python3.8/dist-packages")
import googlemaps
from Geo_Api.Route import Route
import geopy.distance
from geopy.geocoders import Nominatim
import geocoder

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
    coords_2 = (station.location.y, station.location.x)
    distance = geopy.distance.geodesic(coords_1, coords_2).m
    return Route(startlocation, station, distance)

def get_current_location():
    """
    Gets location of user
    Return value: geolocation
    """
    g = geocoder.ip('me')
    return turn_adress_into_geolocation(g.current_result.address)

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
    #calculate distances to all stations
    routes = calculate_routes(startlocation, stations)
    #sort routes by distance
    routes.sort(key=lambda x: x.distance)
    #return given amount of nearest stations
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
    #calculate distances to all stations
    routes = calculate_routes(startlocation, stations)
    #sort routes by distance
    routes.sort(key=lambda x: x.distance)
    #return given amount of nearest stations
    nearest_stations = []
    amount = 0
    for route in routes:
        if route.station.availablebikes.amount_free_docks != 0:
            nearest_stations.append(route.station)
            amount = amount + 1
        if amount == quantity:
            break
    return nearest_stations

def get_best_stations(startlocation, destinationlocation, stations):
    """
    Calculates a route between two locations using MetroBike stations
    Return value: Array of used stations
    """
    nearest_startstation=get_nearest_stations(startlocation, stations, 1)
    nearest_endstation=get_nearest_stations_with_docs(destinationlocation, stations, 1)
    stations = [nearest_startstation[0], nearest_endstation[0]]
    return stations

    
def create_google_maps_route(startlocation, endlocation, stations):
    #init gmaps module
    gmaps = googlemaps.Client(key='AIzaSyCj8S_a8wIqEiv0gx8XfVtdSJqDXvJb3jo')
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52'}
    gmaps.requests_kwargs.update({
            "headers": headers,
            "timeout": 2,
        })
    origins = (startlocation.latitude, startlocation.longitude)
    destination = (endlocation.latitude, endlocation.longitude)
    #create waypoints
    waypoint_stations = []
    for station in stations:
        waypoint_stations.append((station.location.y, station.location.x))
    #calculate route
    matrix = gmaps.directions(origins, destination, waypoints=waypoint_stations, mode='bicycling')
    return matrix