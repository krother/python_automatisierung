#
# gesucht: 3 zuletzt geänderten Dateien
#
import os


dateien = os.listdir(".")
geaendert = [os.path.getmtime(fn) for fn in dateien]  # List Comprehension

md = list(zip(geaendert, dateien))
md.sort()
neueste = md[-3:]  # slicing: von der vorvorletzten Position bis zum Ende

print(neueste)
