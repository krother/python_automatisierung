Dateiformate
============

Unter den mehr als 100,000 verfügbaren Python-Bibliotheken befinden sich zahlreiche nützliche Helfer, welche alle wichtigen Dateiformate lesen und schreiben können.
Hier stelle ich die wichtigsten kurz vor:

----

CSV-Dateien
-----------

Die Bibliothek ``pandas`` ist eine der meistgenutzten Python-Bibliotheken, wenn es darum geht, tabellarische Daten zu bearbeiten, auszuwerten und zu plotten.
``pandas`` ist ein mächtiges Werkzeug für kleine und mittelgroße Datensätze (bis ca. 1 GB).
Es ist darin vergleichbar zu R und Matlab.
Hinter den Kulissen verwendet pandas die Bibliothek ``numpy`` wodurch viele Berechnungen recht schnell sind.

Die Tabellen in ``pandas``, genannt *DataFrames*, haben zahlreiche nützliche Methoden zum Aggregieren, Laden und Speichern von Daten. Ein verbreitetes Format sind CSV-Dateien, die als Textdateien auch mehr oder weniger menschenlesbar sind.

Vor der Benutzung muß pandas installiert werden:

.. literalinclude::

    pip install pandas


Das Einlesen einer Datei wie :download:`penguins.csv` selbst ist wenig spektakulär:

.. literalinclude::

   import pandas as pd

   df = pd.read_csv("penguins.csv", sep=";")

   # Mittelwert numerischer Spalten
   print(df.mean())

   # ein Diagramm
   df["Species"].value_counts().plot.bar()

Alle Möglichkeiten von ``pandas`` auch nur aufzuzählen würde hier den Rahmen sprengen.
Zum Glück gibt es zahlreiche Videokurse und Infoseiten. 

.. seealso::

  `pandas Tutorial und Dokumentation <http://pandas.pydata.org/>`__

  Das Buch von Wes McKinney, dem ursprünglichen Autor von pandas, ist auf Deutsch erhältlich:

  `Datenanalyse mit Python <https://dpunkt.de/produkt/datenanalyse-mit-python-3/>`__

----

Excel-Dateien
-------------

``pandas`` macht auch mit Excel-Spreadsheets kurzen Prozeß:

.. code::

   import pandas as pd

   df = pd.read_excel("mein_spreadsheet.xlsx")
   print(df.head())

----

JSON-Dateien
------------

Das Format **JSON (JavaScript Object Notation)** hat sich als Standard für die Kommunikation zwischen APIs, Webseiten und NoSQL-Datenbanken etabliert.
Es ist deutlich angenehmer für Menschen und Maschinen zu lesen als z.B. XML.
JSON läßt sich fast 1:1 zu Listen und Dictionaries in Python übersetzen.
Darum kümmert sich das in Python bereits eingebaute Module ``json``.

.. literalinclude:: example_json.py

.. seealso::

   `docs.python.org/3/library/json.html <https://docs.python.org/3/library/json.html>`__

----

XML-Dateien
-----------

Das strukturierte Format XML ist schon etwas in die Jahre gekommen.
Trotzdem kann man es noch häufig in freier Wildbahn beobachten, wohl auch wegen der syntaktischen Nähe zu HTML.

Das standardmäßig installierte Python-Modul ``xml`` parst XML-Dateien.
Genaugenommen enthält es mehrere XML-Parser (wegen unterschiedlicher Behandlung von Fehlern in XML).

Jeder XML-Parser liefert eine Baumstruktur von DOM-Objekten zurück.
In diesem kann nach enthaltenen Tags gesucht werden, die Unterbäume des Dokuments sind.
Auch auf die Attribute und den allgemeinen Text kann zugegriffen werden.

Als Beispiel soll folgendes XML-Dokument eingelesen werden:

.. literalinclude:: hamlet.xml

Der folgende Python-Code liest es anstandslos ein:

.. literalinclude:: xml_example.py

.. seealso::

   `Dokumentation des Moduls XML <https://docs.python.org/3/library/xml.html>`__

----

ZIP-Archive
-----------

Das Modul ``zipfile`` kann ``.zip``-Dateien lesen und schreiben.
Es ist Bestandteil jeder Python-Distribution.

Du kannst mit Python sowohl Dateien als auch Strings zu einem zip-Archiv hinzufügen.
Bei Strings muß der Dateiname mit angegeben werden.
Beim Extrahieren von Dateien wird der Zielordner automatisch erstellt

.. literalinclude:: example_zipfile.py

.. seealso::
 
   `docs.python.org/3/library/zipfile.html <https://docs.python.org/3/library/zipfile.html>`__
