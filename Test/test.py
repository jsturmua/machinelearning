import requests
import json

header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52'}

r = requests.get("https://bikeshare.metro.net/stations/json/", headers=header)

jsoninput = json.loads(r.content)


for object in jsoninput['features']:
    print (object['properties']['docksAvailable'])
