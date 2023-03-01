
.. _scraping:

Web Scraping
============

.. include:: scraping_puzzle.rst

----

.. include:: downloading_web_pages.rst



.. _song_links:


.. container:: banner milestone

   Find Song Links

.. highlights::

   **Download the URLs of all songs of your favourite artist.**

   -  Go to the page listing all songs of your favourite artist on `lyrics.com <http://lyrics.com>`_.
   -  Copy the URL
   -  Use the ``requests`` module to download that page
   -  Save the page to a text file
   -  Open the page in a text editor
   -  Examine the HTML code and look for links to songs
   -  Extract all links using :ref:`Regular Expressions <regex>`


.. container:: banner milestone

   Download Songs

.. highlights::

   -  Write a loop that goes through all song URLs that you collected previously
   -  Construct a complete URL
   -  Test the URL in a browser manually
   -  Generate a unique file name (using the song name or a number)
   -  Download each song
   -  Save each song to a unique file


.. container:: banner reading

   Link

.. highlights::

   access Google spreadsheets from Python: `<https://developers.google.com/sheets/api/quickstart/python>`__

.. container:: banner recap

   Solve with One-Liners

.. highlights::

   Find the most frequent words on the Berlin Wikipedia page

   .. code:: python3

      import requests
      import re
      from collections import Counter

      # 1. retrieve the Berlin Wikipedia page
      url = "https://en.wikipedia.org/wiki/Berlin"
      response = ...

      # 2. check the status code
      print(...)

      # 3. store the html contents of the page
      html = ...

      # 4. write the html contents to a file
      with ("berlin.html", "w") as f:
          ...

      # 5. remove all html tags
      text = re.sub(..., '', html)

      # 6. extract words
      words = re.findall(..., text)

      # 7. remove words with less than 6 characters
      long_words =

      # 8. create a Counter object from the long words
      c = ...

      # 9. print how often the word 'Berlin' occurs
      print(...)

      # 10. print the 10 most common words
      print(c. ...)

