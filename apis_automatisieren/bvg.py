"""
Berlin public transport API

documentation: https://v5.vbb.transport.rest/
"""

import requests
from pprint import pprint


BASE_URL = 'https://v5.vbb.transport.rest'


#
# Eine Haltestelle finden
#
name = 'Alexanderpaltz'
url = f"{BASE_URL}/locations?poi=false&addresses=false&query={name}"

response = requests.get(url)
haltestelle = response.json()[0]  # erster Treffer

pprint(f"{haltestelle['name']=}   {haltestelle['id']=}")


#
# Abfahrtszeiten nachschlagen
#
print(f'\nNächste Verbindungen ab {haltestelle["name"]}:\n')

station_id = haltestelle['id']
minuten = 5

url = f'{BASE_URL}/stops/{station_id}/departures?duration={minuten}'

for e in requests.get(url).json():
    print(e['plannedWhen'][11:-9], e['line']['name'], e['direction'])
