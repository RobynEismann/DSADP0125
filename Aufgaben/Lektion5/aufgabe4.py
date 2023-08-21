# Entwickeln Sie in Python ein Programm, welches die statistische Verteilung der Pfad|änge in einem
# ungerichteten Graphen (E, K, f) mit n = 250 Knoten durch eine Monte-Carlo Simulation nach
# dem Greedy-Algorithmus berechnet. Dabei sollen den Verbindungen k1 bis km aus K mit m = 100
# zwischen den Graphenknoten e1 bis en aus E zufällige numerische Werte durch die Abbildung f :
# K → N mit einer Gaußverteilung der Werte kj um den Mittelwert kj = 50 mit Standardabweichung
# σ =√50 zugeordnet werden.
#--------------------------------------------------------------------------------------------------------------------------------------
# (mithilfe von Chatgpt)


import random
import numpy as np
import matplotlib.pyplot as plt

n = 250         # Anzahl der Knoten im Graphen
m = 100         # Anzahl der Verbindungen (Kanten)
mu = 50         # Mittelwert und Standardabweichung für Gaußverteilung
sigma = np.sqrt(50)

graph = [[0] * n for _ in range(n)]             # Erzeuge eine leere Matrix für den Graphen

for _ in range(m):                              # Fülle die Matrix mit zufälligen numerischen Werten (Simuliere Kanten)
    
    source = random.randint(0, n - 1)           # Wähle zufällige Quell- und Zielknoten
    target = random.randint(0, n - 1)
    
    while source == target:                     # Stelle sicher, dass Quell- und Zielknoten unterschiedlich sind
        target = random.randint(0, n - 1)
    
    value = int(np.random.normal(mu, sigma))    # Generiere einen zufälligen Wert für die Kante mit Gaußverteilung
    
    graph[source][target] = value               # Füge die Kante zur Matrix hinzu (gewichteter Graph)
    graph[target][source] = value


def calculate_path_length(graph, source, target):   # Berechne die Pfadlänge zwischen zwei Knoten im Graphen

    visited = set()                                 # Menge der besuchten Knoten
    queue = [(source, 0)]                           # Warteschlange für die BFS, mit Startknoten und Pfadlänge
    while queue:
        node, path_length = queue.pop(0)            # Entferne den ersten Knoten aus der Warteschlange
        if node == target:
            return path_length                      # Wenn der Zielknoten erreicht wurde, gib die Pfadlänge zurück
        if node not in visited:
            visited.add(node)                       # Füge den aktuellen Knoten zu den besuchten Knoten hinzu
            for neighbor in range(len(graph[node])):
                weight = graph[node][neighbor]
                if weight > 0:                                      # Wenn es eine Kante zwischen den Knoten gibt
                    queue.append((neighbor, path_length + weight))  # Füge den Nachbarn zur Warteschlange hinzu mit erhöhter Pfadlänge
    return float('inf')                                             # Wenn kein Pfad gefunden wurde, gib Unendlich zurück

# Berechne die Pfadlängen zwischen allen Knotenpaaren
all_path_lengths = [[calculate_path_length(graph, i, j) for j in range(n)] for i in range(n)]

# Verteilung der Pfadlängen (Filtere unendliche Pfadlängen heraus)
path_lengths = [
    length
    for lengths in all_path_lengths
    for length in lengths
    if length not in [0, float('inf')]
]

# Zeige die Verteilung der Pfadlängen in einem Histogramm
plt.hist(path_lengths, bins=20, density=True, alpha=0.7, color='m')
plt.xlabel('Pfadlänge')
plt.ylabel('Relative Häufigkeit')
plt.title('Verteilung der Pfadlängen')
plt.show()

#print(graph)