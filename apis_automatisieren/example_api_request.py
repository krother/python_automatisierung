
import requests
from pprint import pprint


query = "skywalker"

response = requests.get(f'https://swapi.dev/api/people/?search={query}')
print(response.status_code)

result = response.json()
pprint(result)