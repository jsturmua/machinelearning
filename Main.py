from Metro_Bikes import Location, Station, parser 
from Geo_Api import calculations, visualisation

#Get all stations from MetroBike Website
stations = parser.parse_json()

#User has to choose one of the three options
print("Please select one the three options:")
choice = int(input("1. Find nearest bike station\n2. Find nearest station with available docs\n3. Find best route in Los Angeles\n"))

#Get startlocation of user
choice_location= input("Would you like to use your current location as start location? y/n\n")
if choice_location == 'y':
    startlocation = calculations.get_current_location()
else:
    startaddress = "Franklin Ave, CA"
    startlocation = calculations.turn_adress_into_geolocation(startaddress)

# Find nearest stations with available bikes
if choice == 1:
    # User sets the quantity and the function returns the specified amount of neaerest stations
    quantity = int(input("How many stations would you like to see?\n"))
    # all Stations get sorted by distances and the quantity communicates how many station should be outputed
    nearest_stations = calculations.get_nearest_stations(startlocation, stations, quantity)

    print("The nearest stations are these:")
    for station in nearest_stations:
        print(station.name)
    visualisation.visualize_locations(startlocation, nearest_stations)

# Find the nearest station with available docs
elif choice == 2:
    # User sets the quantity and the function returns the specified amount of neaerest stations with docs
    quantity = int(input("How many stations would you like to see?\n"))
    nearest_stations = calculations.get_nearest_stations_with_docs(startlocation, stations, quantity)
    print("The nearest stations are these:")
    for station in nearest_stations:
        print(station.name)
    visualisation.visualize_locations(startlocation, nearest_stations)

#Find the best route
elif choice == 3:
    # Enter a destination location
    # endlocation = input("Enter address of your destination: ")
    # To easy up debugging endlocation hard corded
    destination_address = "Burbank Blvd, CA"
    endlocation = calculations.turn_adress_into_geolocation(destination_address)
    #calculate the stations of the route
    beststations = calculations.get_best_stations(startlocation, endlocation, stations)
    maps_route = calculations.create_google_maps_route(startlocation, endlocation, beststations)
    visualisation.visualize_route(maps_route)


#User made an invalid input
else:
    print(choice)
    print("Invalid input, Program ends")