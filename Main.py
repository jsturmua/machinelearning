from Metro_Bikes import Stations, Location, Station 
from Distance_Api import calculations

#Get all stations from MetroBike Website
stations = Stations.parse_json()

#Get startlocation of user
startlocation = "1600 Amphitheatre Parkway, Mountain View, CA"

#calculate all routes (startlocations, stations, distances)
#routes = calculations.calculate_routes(startlocation, stations)

#User has to choose one of the three options
choice = int(input("1. Find nearest bike station\n2. Find nearest station where docs are avaivable\n3. Find best route in Los Angeles\n"))

# User sets the quantity and the function returns the specified amount of neaerest stations
if choice == 1:
    quantity = int(input("How many stations would you like to see?"))
    # all Stations get sorted by distances and the quantity communicates how many station should be outputed
    nearest_stations = calculations.get_nearest_stations(startlocation, stations, quantity)

    print("The nearest stations are these:")
    for station in nearest_stations:
        print(station.name)

# User sets the quantity and the function returns the specified amount of neaerest stations with docs
elif choice == 2:
    quantity = int(input("How many stations would you like to see?"))
    nearest_station = calculations.get_nearest_stations_with_docs(startlocation, stations, quantity)
    print(nearest_station.name)

#User enters a startlocation and and endlocation and the function returns the best route
elif choice == 3:
    stations.find_best_route()

#User made an invalid input
else:
    print(choice)
    print("Falsche Eingabe, Programm wird beendet!")