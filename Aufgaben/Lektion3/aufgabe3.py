#Schreiben Sie eine Routine in Python, welche die Kreiszahl π durch parallele Berechnung approximiert. 
#Berechnen Sie damit die Kreiszahl π bis zur zwölften Stelle hinter dem Komma. Was lässt
#sich über die Genauigkeit der Berechnung im Vergleich zur der nicht-parallelisierten Berechnung
#aussagen?
#__________________________________________________________________________________________________________________________________________________________________


# der Leibniz-Algorithmus bietet leider aufgrund des Global Interpreter Lock (GIL) in Python nicht wirklich parallele Ausführungsvorteile
# bei einer multiprocessing variante mit der Monte Carlo Methode hat aber leider mein Rechner nicht mitgespielt 

import threading

def calculate_pi(start, end, result_list):
    my_pi = 0
    sign = 1

    # Berechne die Teilsumme der Leibniz-Reihe für den angegebenen Bereich
    for i in range(start, end, 2):
        my_pi += sign * (1 / i)
        sign *= -1

    result_list.append(my_pi)

def parallel(num_terms):
    result_list = []

    mid = num_terms // 2        # Aufteilen der Terme der Leibniz Reihe

    # Erster Thread: Berechne die Leibniz-Reihe von 1 bis mid
    thread1 = threading.Thread(target=calculate_pi, args=(1, mid, result_list))
    thread1.start()

    # Zweiter Thread: Berechne die Leibniz-Reihe von mid+1 bis num_terms
    thread2 = threading.Thread(target=calculate_pi, args=(mid+1, num_terms, result_list))
    thread2.start()

    # Warte auf das Ende der Threads
    thread1.join()
    thread2.join()

    # Summiere die Ergebnisse der beiden Threads, um die Gesamtapproximation von π zu erhalten
    total_pi_approximation = sum(result_list)

    return 4 * total_pi_approximation

# Anzahl der Terme in der Leibniz-Reihe (je höher, desto genauer)
num_terms = 1000000

# Berechnung von π durch parallele Leibniz-Reihe mit zwei Threads
pi_approximation = parallel(num_terms)

print("π bis zur zwölften Stelle hinter dem Komma (parallele Leibniz-Reihe mit zwei Threads):", round(pi_approximation, 12))



