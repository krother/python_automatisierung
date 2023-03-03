
import os

rezept = """
1 Pizzateig
4 Tomaten
3 Chillis
2 Zucchini
Käse
"""

pfad = "/home/kristian/automatisierung"
dateiname = "pizza.txt"

fn = os.path.join(pfad, dateiname)

# prüfe ob es die Datei schon gibt:
if os.path.exists(fn):
    print("DATEI GIBT ES SCHON")
else:
    with open(fn, 'w') as f:
        f.write(rezept)
