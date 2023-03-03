#
# Befehle über SSH ausführen mit Fabric
#
# Installation
# pip install fabric
#
# Doku:
# https://docs.fabfile.org/en/stable/index.html

import os
from fabric import Connection


hostname = "ssh.pythonanywhere.com"
username = "krother"
password = os.getenv("SSH_PASSWORD")

c = Connection(
    host=hostname,
    user=username,
    port=22,
    connect_kwargs={'password': password}
)

# Befehl auf remote Server ausführen
result = c.run("echo 'hello world'")
print(result.ok)  # boolean ob es geklappt hat
ausgabe = result.stdout.strip()
print(f"Standardausgabe des Programms: {ausgabe}")


# Datei hochladen
# file transfer
c.put(remote="input.txt", local="input.txt")

# Ausgabe in Datei umleiten
c.run("cat input.txt > out.txt")
c.run("ls -a | head >> out.txt")
c.run("echo $HOSTNAME >> out.txt")

# Datei herungerladen
c.get(remote="out.txt", local="out.txt")
