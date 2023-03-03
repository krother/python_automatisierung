
# pip install requests
#
# (besser als urllib)

import requests
from pprint import pprint
import pandas as pd


result = []
for pid in range(1, 6):
    url = f"https://swapi.dev/api/planets/{pid}"

    response = requests.get(url)
    print(pid, response.status_code)

    j = response.json()
    pprint(j)

    print(j["name"])
    print(j["climate"])

    open('temp.json', 'w').write(response.text)
    s = pd.read_json("temp.json", typ="series")
    result.append(s)

df = pd.DataFrame(result)
df.to_excel("planeten.xlsx")
