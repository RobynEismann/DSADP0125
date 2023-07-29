# Schreiben Sie ein Programm in Python, welches die Kreiszahl π bis auf die zehnte Stelle hinter dem Komma berechnet. 
# Wie lautet die Kreiszahl im Rahmen dieser Genauigkeit?
#__________________________________________________________________________________________________________________________________________________________________

import math

my_pi = 0                               # Variable, um die Näherung von π (Pi) zu speichern
sign = 1                                # Variable, um das Vorzeichen in der Leibniz-Reihe zu steuern

# Schleife, um die Leibniz-Reihe zu berechnen
# Die Leibniz-Reihe ist eine unendliche Reihe zur Näherung von π/4 (Pi durch 4)
# Hier wird die Schleife 100.000.000 Mal ausgeführt, um die Näherung zu verbessern
for i in range(1, 100000000,2):
    my_pi += sign * (1 / i)             # Jedes Element der Reihe wird zur Näherung hinzugefügt
    sign *= -1                          # Das Vorzeichen wird bei jedem Schleifendurchlauf geändert (abwechselndes Vorzeichen)

# Die Näherung von π (Pi) wird vervierfacht, um den tatsächlichen Wert von π zu erhalten,
# da die Leibniz-Reihe π/4 annähert
rounded_pi = round(4 * my_pi, 10)       # Runden der Näherung auf 10 Nachkommastellen

# Ausgabe der berechneten Näherung von π
print("π bis zur zehnten Stelle hinter dem Komma:")
print(rounded_pi)

# Vergleich mit dem tatsächlichen Wert von π, der in der math-Bibliothek verfügbar ist
print("Tatsächlicher Wert von π:")
print(math.pi)

# Berechnung und Ausgabe des Unterschieds zwischen der berechneten Näherung und dem tatsächlichen Wert von π
print("Diff: '{:.10f}'".format(math.pi - rounded_pi))
