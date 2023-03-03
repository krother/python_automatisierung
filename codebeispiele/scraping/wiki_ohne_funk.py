import requests
import re
from bs4 import BeautifulSoup
import pandas as pd


wort = "Berlin"

r = requests.get(f"https://de.wikipedia.org/wiki/{wort}")
print(r.status_code)

# Mit RegEx alle Tabellenzellen finden
tags = "<td>([^<].+?)</td>"
elemente = re.findall(tags, r.text)

html = r.text

# alle Links finden
links = []  # [[link1, label1], [link2, label2]]
soup = BeautifulSoup(html)

for a in soup.find_all('a'):
    href = a.get('href', '')  # href ist ein string
    if href and href[:5] == '/wiki':   # if href gleich wie href != ''
        label = a.get_text()
        print(f"{label:30}{href:40}")
        links.append([href, label])


# Export nach Excel
df = pd.DataFrame(links, columns=["href", "label"])
print(df.shape)
df = df.drop_duplicates(subset="href")
print(df.shape)
print(df.head())
df.to_excel("wikipedia_links.xlsx")
