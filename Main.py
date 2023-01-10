from Metro_Bikes import Stations, Location, Station 
from Distance_Api import calculations, visualisation

#Get all stations from MetroBike Website
stations = Stations.parse_json()

#Get startlocation of user
choice_location= input("Would you like to use your current location? y/n")
if choice_location == 'y':
    startlocation = calculations.get_current_location()
else:
    startadress = "1600 Amphitheatre Parkway, Mountain View, CA"
    startlocation = calculations.turn_adress_into_geolocation(startadress)

#User has to choose one of the three options
choice = int(input("1. Find nearest bike station\n2. Find nearest station where docs are avaivable\n3. Find best route in Los Angeles\n"))

# Find nearest stations with available bikes
if choice == 1:
    # User sets the quantity and the function returns the specified amount of neaerest stations
    quantity = int(input("How many stations would you like to see?"))
    # all Stations get sorted by distances and the quantity communicates how many station should be outputed
    nearest_stations = calculations.get_nearest_stations(startlocation, stations, quantity)

    print("The nearest stations are these:")
    for station in nearest_stations:
        print(station.name)
    visualisation.visualize_locations(startlocation, nearest_stations)

# Find the nearest station with available docs
elif choice == 2:
    # User sets the quantity and the function returns the specified amount of neaerest stations with docs
    quantity = int(input("How many stations would you like to see?"))
    nearest_stations = calculations.get_nearest_stations_with_docs(startlocation, stations, quantity)
    print("The nearest stations are these:")
    for station in nearest_stations:
        print(station.name)
    visualisation.visualize_locations(startlocation, nearest_stations)

#Find the best route
elif choice == 3:
    # Enter a destination location
    endlocation = "Irvine, Kalifornien, USA"
    endlocation = calculations.turn_adress_into_geolocation(endlocation)
    stations = calculations.get_best_route(startlocation, endlocation, stations) #calculate the stations of the route
    maps_route = calculations.create_google_maps_route(startlocation, endlocation, stations)
    visualisation.visualize_route(maps_route)


#User made an invalid input
else:
    print(choice)
    print("Falsche Eingabe, Programm wird beendet!")