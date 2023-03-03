import requests
import re
from pprint import pprint
from bs4 import BeautifulSoup
import pandas as pd


def wikiseite_herunterladen(begriff: str) -> str:
    r = requests.get("https://de.wikipedia.org/wiki/Berlin")
    print(r.status_code)

    # Mit RegEx alle Tabellenzellen finden
    tags = "<td>([^<].+?)</td>"
    elemente = re.findall(tags, r.text)

    return r.text


def links_auslesen(html: str) -> list:
    # alle Links finden
    result = []  # [[link1, label1], [link2, label2]]
    soup = BeautifulSoup(html)

    for a in soup.find_all('a'):
        href = a.get('href', '')  # href ist ein string
        if href and href[:5] == '/wiki':   # if href gleich wie href != ''
            label = a.get_text()
            print(f"{label:30}{href:40}")
            result.append([href, label])
    return result


def links_als_excel_speichern(links: list, dateiname: str) -> None:
    # Export nach Excel
    df = pd.DataFrame(links, columns=["href", "label"])
    print(df.shape)
    df = df.drop_duplicates(subset="href")
    print(df.shape)
    print(df.head())
    df.to_excel(dateiname)


def main() -> None:
    seite = wikiseite_herunterladen("Berlin")
    links = links_auslesen(seite)
    links_als_excel_speichern(links, "wikipedia_links.xlsx")


main()
