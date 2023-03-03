
import pandas as pd

df = pd.read_excel("ergebnisse.xlsx", header=None)

df.iloc[2:9, 1].to_list()
df.shape[0]  # --> Zeilen
df.shape[1]  # --> Spalten


# Datentypen:

# liste: [26, 8]
# tuple: (26, 8)
# dictionary: {'zeilen': 26, 'spalten': 8}