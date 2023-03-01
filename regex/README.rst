
.. _regex:

Reguläre Ausdrücke
==================

.. card::
   :shadow: lg

   **Was haben diese vier Bilder gemeinsam?**

   .. figure:: regex.jpg

   Die Antwort läßt sich mit diesem Muster beschreiben:

   .. code::

       ^(\w+)i(\w+)[- ]\1o\2

Was sind reguläre Ausdrücke?
----------------------------

**Reguläre Ausdrücke** sind eine Grammatik, um Muster in Texten zu beschreiben.
Es gibt sie in allen gängigen Programmiersprachen.
Reguläre Ausdrücke sind immer dann nützlich, wenn man mit Standardwerkzeugen nicht mehr weiterkommt,
wenn beispielsweise für ein Dateiformat kein Parser existiert oder die Daten unsauber sind.
Das macht RegEx zu einem sehr nützlichen Werkzeug für allerlei textbasierte Aufgaben.


.. card::
   :shadow: lg

   **Übung:**

   Füge den folgenden Text auf `regex101.com <http://regex101.com/>`__ ein:
   
   ::

      thyme coriander rosemary cinnamon pepper
      tarragon basil salvia cumin nutmeg saffron

   Untersuche folgende Muster:

   ::

      pepper
      \w+
      c\w+
      c....
      c.+
      c[iou]
      c[aioumn]+
      salt|pepper
      \w{3,5}
      [^n]+

   Ermittle, was die Sonderzeichen bedeuten.

----

Reguläre Ausdrücke in Python
----------------------------

Mit dem Python-Modul ``re`` lassen sich reguläre Ausdrücke mit wenig Code in Python integrieren:

.. literalinclude:: regex.py


============================= ===================================================
Funktion                      Beschreibung
============================= ===================================================
:py:func:`re.findall`         liefert eine Liste gefundener Strings
:py:func:`re.search`          liefert ein Match-Objekt für den ersten Treffer
:py:func:`re.sub`             ersetzt ein Muster durch einen String
:py:func:`re.match`           prüft ob der gesamte String paßt
:py:func:`re.compile`         compiliert ein häufig verwendetes Muster (schneller)
`re.DOTALL`                   Schalter um Zeilenumbrüche mit ``.`` abzudecken
`re.IGNORECASE`               Schalter um Groß/Kleinschreibung zu ignorieren
============================= ===================================================

----

Links
-----

* `RegexOne Tutorial <http://regexone.com/>`__
* :download:`Regular Expression Cheatsheet <regex_cheatsheet.pdf>`
* `Python Regex HOWTO <https://docs.python.org/3.6/howto/regex.html>`__

----

.. note::

   Die Bilder wurden erstellt von (oben links nach unten rechts):

   -  By Source (WP:NFCC#4), Fair use [`link <https://en.wikipedia.org/w/index.php?curid=48711736>`__]
   -  unspecified, assuming Swarve~commonswiki, CC BY-SA 3.0 [`link <https://commons.wikimedia.org/w/index.php?curid=336076>`__]
   -  Gaël Marziou from Grenoble, France - IMG\_6266\_DXO, CC BY 2.0 [`link <https://commons.wikimedia.org/w/index.php?curid=47416377>`__]
   -  Derfu, CC BY-SA 3.0
