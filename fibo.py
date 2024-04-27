# Die Fibonacci-Folge ist definiert fuer n>2 als fn = fn-1 + fn-2 mit den Anfangswerten f1 = f2 = 1
    # schreiben Sie ein Programm fibo.py in MicroPython, dass ZWEI Funktionen zur Ermittlung einer Fibonacci-Zahl enthuelt. 
    # Die Funktion fibo soll nicht rekursiv (Schleife!) programmiert sein.
    # Die zweite Funktion fibo_r soll rekursiv programmiert sein
    # Die in der Bibliothek time enthaltene Funktionen time.ticks_us() und 
    # time.ticks_ms() liefert ihnen die seit dem Systemstart vergangene Zeit in Mikrosekunden oder Millisekunden.
    # Ermitteln Sie mit dieser Funktion die Laufzeit der beiden FibonacciFunktionen fuer Uebergabewerte 5, 10, 15 und 20.

import time
def fibo(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    a,b = 1,1
    for i in range(2,n):
        a, b = b, (a+b)
    return b

def fibo_r(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo_r(n - 1) + fibo_r(n - 2)

if __name__ == "__main__":
    # Jede Zahl einzelnd eingeben 
    zahl = 5

    start = time.ticks_us()
    ergebnis = fibo(zahl)
    # Beide Funktion einzelnd testen fue jede Zahl!
    #ergebnis = fibo_r(zahl)
    ende = time.ticks_ms()

    zeit = (ende - start)
    print("Zahl:", zahl, ", Ergebnis:", ergebnis, ", Zeit:", zeit)
