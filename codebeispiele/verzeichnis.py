# Arten von imports
# bei imports wird immer das Wort auf der rechten Seite in den 
# lokalen Namensraum (namespace) übernommen

import os
from os import path
from os.path import exists

# from os import *  # bitte nicht machen

# Beispielauswahl von os-Funktionen
# os.path.exists(pfad) -> bool
# os.path.join(pfad1, pfad2) -> str

print(os.listdir("/home/kristian/automatisierung")) # -> Liste von Dateinamen

pfad = "/home/kristian/automatisierung"
for dateiname in os.listdir(pfad):
    fn = os.path.join(pfad, dateiname)
    if os.path.isfile(fn):
        with open(fn, "r") as f:
            print(f.read()[:20])
    else:
        print(fn, "ist ein Verzeichnis")

