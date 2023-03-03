
import os

# Achtung backslashes
win_pfad = "C:\\Users\\kristian\\"  # Escape character

pfad = "C:" + os.sep + "Users" + os.sep + "kristian"

pfad = "/home/kristian/automatisierung/"  # / funktioniert auch auf Win

with open(pfad + 'hallo.txt', 'r') as f:
    for zeile in f:
        print(zeile)
    # schließt automatisch die Datei

    # r: read ; w: write ; a: append
    # rb, wb : binary
