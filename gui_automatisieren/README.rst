
GUI-Programme automatisieren
============================

**Bei der GUI-Automatisierung kapert ein Programm die Eingabegeräte.
Damit lassen sich theoretisch beliebige Programme fernsteuern. Dazu gehören:**

- Programme starten
- die Tastatur steuern inklusive Tastenkombinationen
- Die Maus steuern
- warten
- Screenshots erzeugen

Es gibt mehrere Python-Bibliotheken zur GUI-Automatisierung.
Diese sind jedoch recht unterschiedlich. Hier ein kurzer Überblick.

----

PyAutoGui
---------

Die Bibliothek `PyAutoGui <https://pyautogui.readthedocs.io/en/latest/>`__ erlaubt die direkte Steuerung des Desktops.
Sie funktioniert auf allen Betriebssystemen:

.. code::

   pip install pyautogui

Unter Linux sind einige Pakete zusätzlich nötig:

.. code::

    sudo apt-get install scrot
    sudo apt-get install python3-tk
    sudo apt-get install python3-dev

Der Code ist recht selbsterklärend. Hier ist ein Beispiel für eine Automatisierung von LibreOffice unter Ubuntu 20:

.. literalinclude:: gui.py

.. seealso::

   `PyAutoGui <https://pyautogui.readthedocs.io/en/latest/>`__

----

Robot Framework
---------------

Möchte man mehrere Umgebungen testen oder automatisieren, kann es hilfreich sein, von den konkreten Anweisungen auf Testfälle zu abstrahieren.
Das **RobotFramework** bietet eine solche Abstraktionsebene, mit der sich unterschiedliche Arten von Testfällen beschreiben und ausführen lassen.

.. seealso::

   `Robot Framework <https://github.com/robotframework/robotframework>`__

----

Weitere Tools
-------------

Auch `RPA-Python <https://github.com/tebelorg/RPA-Python>`__ (vormals TagUI) kann zur Automatisierung der GUI eingesezt werden.
Das Paket ist prinzipiell in der Lage, den Bildschirminhalt zu analysieren, indem es:

* nach bestimmten Bildern auf dem Bildschirm sucht
* Text über OCR erkennt

Die Installation ist jedoch deutlich komplizierter.

.. literalinclude:: web.py

