
from multiprocessing import Process
import os

a = 1

def aufgabe():  # Python-Funktion definieren
    global a
    os.system('sleep 3')
    a += 1  # nur in normalen Aufrufen relevant


aufgabe()  # normaler Aufruf
aufgabe()  # normaler Aufruf

p1 = Process(target=aufgabe)  # 1. übergebe die aufzurufende Funktion
p2 = Process(target=aufgabe)  # 1. übergebe die aufzurufende Funktion
p1.start()                    # 2. Starte den Prozeß 
p2.start()                    # 2. Starte den Prozeß 
p1.join()                     # 3. warte bis alles fertig ist
p2.join()                     # 3. warte bis alles fertig ist
print(a)  # am Ende immer noch 1
