
import os
import time
from multiprocessing import Process

import pyautogui as pg
from pynput.keyboard import Controller


doc = "/home/kristian/Documents/dokument.docx"


def ergebnis_loeschen():
    if os.path.exists(doc):
        os.remove(doc)


def schreibprogramm_starten():
    os.system("libreoffice --writer")


if __name__ == '__main__':
    ergebnis_loeschen()

    p = Process(target=schreibprogramm_starten)
    p.start()

    time.sleep(5)

    # Bildschirmgröße und Mausposition ermitteln
    print(pg.size())
    print(pg.position())

    pg.moveTo(800, 300, duration=1) 
    pg.click()

    pg.typewrite("the quick brown fox jumps over the lazy dog.")

    pg.hotkey("ctrl", "a")
    pg.hotkey("ctrl", "b")

    pg.moveRel(0, 100, duration=1)
    pg.click()
    time.sleep(1)

    # Text mit Umlauten einfügen
    pg.press(['enter', 'enter', 'enter'])
    Controller().type("Falsches Üben von Xylophonmusik quält jeden größeren Zwerg.")
    time.sleep(1)

    # Rechtsklick ausprobieren
    pg.click(button="right")
    for i in range(10):
        pg.press("down")
        time.sleep(0.1)
    pg.press("escape")
    time.sleep(1)

    # Schriftgröße einstellen
    pg.hotkey("ctrl", "a")
    pg.moveTo(483, 144, duration=1)
    pg.click()
    pg.typewrite("32")
    pg.press("enter")
    
    pg.moveRel(300, 300, duration=1)
    pg.click()
    time.sleep(3)

    # Dokument speichern
    pg.hotkey("ctrl", "s")
    pg.typewrite("dokument.docx")
    pg.press("enter")

    time.sleep(3)

    # beenden
    pg.hotkey("ctrl", "q")

    pg.screenshot("screenshot.png")

    p.join()  # beenden

    # drag + drop (absolute und relative Position)
    """
    pg.dragTo(500,500, duration = 1)
    pg.dragRel(50,50, duration=1) 
    """
