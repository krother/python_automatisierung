
import multiprocessing as mp
import os


def aufgabe():  # Python-Funktion definieren
    os.system('dir')


if __name__ == '__main__':
    # dieser Block wird nur ausgeführt 
    # wenn das Programm prozess_windows.py direkt ausgeführt
    # also mit "python prozess_windows.py"
    #
    # --> im Gegensatz zu "import prozess_windows"
    #
    mp.freeze_support()
    
    aufgabe()  # normaler Aufruf
    aufgabe()  # normaler Aufruf

    pool = mp.Pool(3)

    p1 = pool.apply_async(aufgabe)
    p2 = pool.apply_async(aufgabe)

    pool.close()
    pool.join()
    pool.terminate()
