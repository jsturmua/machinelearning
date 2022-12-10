from Metro_Bikes import Stations, Location, Station 
from GoogleAPI import calculations


stations = Stations.parse_json()
#choice = int(input("1. Find nearest bike station\n2. Find nearest station where docs are avaivable\n3. Find best route in Los Angeles\n"))

startlocation = "1600 Amphitheatre Parkway, Mountain View, CA"
distances = calculations.calculate_routes(startlocation, stations)

distances = Distances("test", stations)

# if choice == 1:
#     stations.find_nearest_station()

# elif choice == 2:
#     stations.find_nearest_station_with_docs()

# elif choice == 3:
#     stations.find_best_route()
# else:
#     print(choice)
#     print("Falsche Eingabe, Programm wird beendet!")