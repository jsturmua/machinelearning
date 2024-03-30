import sys
sys.path.append("/usr/local/lib/python3.8/dist-packages")
import folium
import polyline

def visualize_locations(startlocation, stations):
    """
    Creates map with waypoints and opens it
    Return value: void
    """
    #Create map with focus on the startlocation
    m = folium.Map(location=[startlocation.latitude, startlocation.longitude], zoom_start=12)
    marker = folium.Marker(location=[startlocation.latitude, startlocation.longitude],popup="Start", icon=folium.Icon(color='green'))
    marker.add_to(m)

    #Loop through all stations and create markers
    for station in stations:
        marker = folium.Marker(location=[station.location.y, station.location.x],popup=station.name)
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
    m = folium.Map(location=[route[0]['legs'][0]['start_location']['lat'], route[0]['legs'][0]['start_location']['lng']], zoom_start=12)
    #Create markers and polyline for waypoints and route
    points = polyline.decode(route[0]['overview_polyline']['points'])
    folium.PolyLine(points, color="red", weight=2.5, opacity=1).add_to(m)
    marker = folium.Marker(location=[route[0]['legs'][0]['start_location']['lat'], route[0]['legs'][0]['start_location']['lng']], title="Start", popup="Start", icon=folium.Icon(color='green'))
    marker.add_to(m)
    for i in range(1, len(route[0]['legs'])):
        marker = folium.Marker(location=[route[0]['legs'][i]['start_location']['lat'], route[0]['legs'][i]['start_location']['lng']], title=str(i), popup=str(i))
        marker.add_to(m)
    marker = folium.Marker(location=[route[0]['legs'][-1]['end_location']['lat'], route[0]['legs'][-1]['end_location']['lng']], popup="Destination", icon=folium.Icon(color='red'))
    marker.add_to(m)
    m.show_in_browser()
    m.save('map.html')