
Dateiverwaltung automatisieren
=============================

.. figure:: pfade.svg

----

Python für die Datei-Automatisierung verwenden
----------------------------------------------

Dateiverwaltung mit Python ist auch für Einsteiger ein dankbares Thema.
Sämtliche notwendigen Bibliotheken sind in Python eingebaut und funktionieren
unabhängig von Entwicklungsumgebung und Betriebssystem.

Folgende Bibliotheken sind dazu nützlich:

====================== ================================================
Bibliothek             Beschreibung
====================== ================================================
`os`                   Allgemeine Schnittstelle zum Dateisystem
`os.path`              Manipulation von Verzeichnissen und Pfaden
`tempfile`             temporäre Dateien erzeugen
`glob`                 Dateinamen über Ausdrücke mit `*` ansprechen
`pathlib`              Verzeichnisse mit `/` als Operator verknüpfen
====================== ================================================

----

Dateien lesen
-------------

Die Python-Funktion `open()` liefert ein Datei-Objekt.
Aus diesem läßt sich der Inhalt Zeile für Zeile auslesen:

.. code:: python

   with open('hallo.txt', 'r') as f:
       for zeile in f:
           print(zeile)

Es ist auch möglich die gesamte Datei in einen einzigen String zu lesen:

.. code:: python

   with open('hallo.txt', 'r') as f:
       text = f.read()

Der `with`-Ausdruck (*Context Manager*) kümmert sich automatisch um das Schließen offener Dateien.
Vom Betriebssystem ist eine maximale Anzahl offener Dateien vorgegeben.
Auch beim Schließen von Python oder bei Programmabbruch weden Dateien geschlossen.

   
.. card::
   :shadow: lg

   **Übung:**

   Erzeuge eine Textdatei `hallo.txt` mit einem Texteditor, schreibe etwas herein und gib den Inhalt mit dem obigen Code aus.

----

Dateien schreiben
-----------------

Das Schreiben von Dateien funktioniert äquivalent zum Lesen.
Die Zeilenumbrüche müssen jedoch explizit hinzugefügt werden:

.. code:: python

   with open('hallo.txt', 'w') as f:
       text = f.write("Hallo Welt\n")

Der Parameter `w` erzeugt eine leere Datei (und überschreibt eine bereits vorhandene).
Mit `a` lässen sich an eine vorhandene Datei neue Zeilen anhängen.

.. card::
   :shadow: lg

   **Übung:**

   Schreibe mehrere Zeilen in eine Datei und lies sie wieder aus.

.. hint::

   Wenn du Binärdateien lesen oder schreiben möchtest, verwende statt `r` und `w` die Strings `rw` oder `wb` .

----

Verzeichnisse organisieren
--------------------------

Mit dem Modul `os` lassen sich Pfade und Verzeichnisse navigieren.
Es enthält zahlreiche nützliche Funktionen, die alle nicht sonderlich schwierig sind.
Die wichtigsten sind:

.. code:: python

   import os

   os.chdir(verzeichnis)
   os.getcwd()
   os.listdir(verzeichnis)
   os.remove(dateiname)
   os.rmdir(verzeichnis)

   os.path.exists(pfad)
   os.path.isdir(pfad)
   os.path.isfile(pfad)
   os.path.join(pfad1, pfad2)
   os.path.split(pfad)

.. hint::

   Bei Verzeichnisnamen unter Windows empfiehlt es sich, **raw strings** zu verwenden, z.B. `r"C:\Users\myself\"`` um Ärger mit Backslashes zu vermeiden.

.. seealso::

    `os Dokumentation <https://docs.python.org/3/library/os.html>`__

    `os.path Dokumentation <https://docs.python.org/3/library/os.path.html#module-os.path>`__ 


.. card::
   :shadow: lg

   **Übung:**

   Führe einige der obigen Befehle in einem interaktiven Python-Terminal aus.
   Finde heraus was sie tun (z.B. auf `devdocs.io <devdocs.io/>`__)


----

Ausführen von Systembefehlen
----------------------------

Die Befehle aus einer Konsole wie **bash** oder **Powershell** lassen sich auch aus Python ausführen.
Hier gibt es zwei wichtige Varianten.

Die Funktion `os.system()` führt einen Befehl einfach nur aus:

.. code:: python

    import os

    os.system('dir')

Bei komplizierteren Befehlen ist diese Vorgehensweise nicht besonders günstig.
Falls Fehler auftreten, bricht Python einfach ab und man erfährt mitunter nicht warum.

Besser ist es einen eigenen Prozeß zu starten.
Dazu dient das Modul `multiprocessing`:

.. code:: python

    from multiprocessing import Process
    import os

    def aufgabe():
       os.system('docker run data_pipeline')

    p = Process(target=aufgabe)
    p.start()
    p.join()

.. seealso::

    `multiprocessing Dokumentation <https://docs.python.org/3/library/multiprocessing.html>`__

----

Umgebungsvariablen
------------------

Für eine effektive Automatisierung sind **Umgebungsvariablen** sehr nützlich, da sich ein Programm so ohne Änderungen konfigurieren läßt. Das Modul `os` erlaubt Zugriff auf diese.

Beispielsweise ist die Variable `PATH` auf den meisten Systemen gesetzt:

.. code::

   import os

   print(os.getenv('PATH'))


----

Beispiel: Babynamen
-------------------

.. figure:: baby.png

Lade die US-Geburtsstatistiken von `https://www.ssa.gov/oact/babynames/limits.html <https://www.ssa.gov/oact/babynames/limits.html>`__ herunter (national data).

Vervollständige das folgende Programm und bringe es zum Laufen:

.. code:: python

    # Bibliotheken importieren
    import os
    import pandas as pd

    # Entpacken der ZIP-Datei nach names/
    os.system(...)

    # Iterieren über alle Dateien im Verzeichnis
    path = "names/"
    for filename in ...(path):
        if filename.startswith("yob"):
            year = filename[3:...]
            filepath = os.join(..., ...)

            # eine Datei einlesen und zusammenfassen
            table = pd.read_csv(filepath, sep=",", columns=["name", "gender", "count"])
            babies = table["count"].sum()
            print(f"Im Jahr {year} wurden in den USA {...} Geburten registriert.")


----


.. note:: 
    
   **Fragen**

   * wie machen sich falsch geschriebene Pfade und Dateinamen bemerkbar?
   * worin unterscheiden sich absolute und relative Pfade?
   * was sind **character encodings**?
