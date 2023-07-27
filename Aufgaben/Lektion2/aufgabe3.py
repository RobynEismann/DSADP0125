import random
import numpy as np
import math

#mehrdim array erstellen

n = 100 # Anzahl knoten und Kanten
m = 50 # Mittelwert und 
u = 50 # Standardabweichung
sigma = np.sqrt(50)

graph = np.zeros
matrix = [[0 for _ in range(n)]for _ in range(n)]

for x in range(n):
    for y in range (n):
        v = np.random.normal(loc=m,scale=u)
        matrix[x][y] = v
        matrix[y][x] = v

print(matrix)



# ein wenig verloren hier :(