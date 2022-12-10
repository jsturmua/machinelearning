import sys
sys.path.append("/usr/local/lib/python3.8/dist-packages")
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyCj8S_a8wIqEiv0gx8XfVtdSJqDXvJb3jo')
new_york_coordinates = (40.75, -74.00)
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

print(geocode_result)