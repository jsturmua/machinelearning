import sys
sys.path.append("/usr/local/lib/python3.8/dist-packages")
import googlemaps
import folium
import polyline

def visualize_locations(startlocation, stations):
    """
    Creates map with waypoints and opens it
    Return value: void
    """
    #Create map with focus on the startlocation
    m = folium.Map(location=[startlocation.latitude, startlocation.longitude], zoom_start=8)
    marker = folium.Marker(location=[startlocation.latitude, startlocation.longitude],popup="Start")
    marker.add_to(m)

    #Loop through all stations and create markers
    for station in stations:
        marker = folium.Marker(location=[station._location.y, station._location.x],popup=station.name)
        marker.add_to(m)
    #show and save map
    m.show_in_browser()
    m.save('map.html')


def visualize_route(route):
    """
    Creates map with waypoints and opens it
    Return value: void
    """
    # Creation of a folium map
    m = folium.Map(location=[route[0]['legs'][0]['start_location']['lat'], route[0]['legs'][0]['start_location']['lng']], zoom_start=8)
    #Create markers and polyline for waypoints
    points = polyline.decode(route[0]['overview_polyline']['points'])
    folium.PolyLine(points, color="red", weight=2.5, opacity=1).add_to(m)
    for i in range(0, len(route[0]['legs'])):
        # polyline = folium.PolyLine(
        #     [[step['start_location']['lat'], step['start_location']['lng']] for step in route[0]['legs'][i]['steps']],
        #     color='blue',
        #     weight=2,
        #     opacity=1
        #     )
        # polyline.add_to(m)
        marker = folium.Marker(location=[route[0]['legs'][i]['start_location']['lat'], route[0]['legs'][i]['start_location']['lng']], popup=str(i))
        marker.add_to(m)
    marker = folium.Marker(location=[route[0]['legs'][-1]['end_location']['lat'], route[0]['legs'][-1]['end_location']['lng']], popup="Destination")
    marker.add_to(m)
    m.show_in_browser()
    m.save('map.html')



# def visualize_route(route):
#     gmaps = googlemaps.Client(key='AIzaSyCj8S_a8wIqEiv0gx8XfVtdSJqDXvJb3jo')
#     headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52'}
#     gmaps.requests_kwargs.update({
#             "headers": headers,
#             "timeout": 2,
#         })
#     #Create the map
#     fig = gmaps.data.addGeoJson(route)
#     #Add the layer
#     fig
#     return fig