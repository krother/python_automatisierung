"""
pip install pytest

pytest
(findet Funktionen namens test_* in Dateien test_*)
"""
from taschenrecher import addieren


def test_addiere_zahlen():
    assert addieren(3, 4) == 7


def test_addiere_mehr_zahlen():
    assert addieren(2, 8) == 10


def test_addiere_drei_zahlen():
    assert addieren(3, 4, 5) == 12

