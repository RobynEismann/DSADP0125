#Entwickeln Sie eine Routine in Python, welche die Gewinne aus einer 6 aus 49 Lotterie berechnet.
#Wie hoch ist der Anteil, den man im Mittel bei einer Wiederholung von Spieleinsätzen wieder
#aus der Lotterie zurück erhält? 
#Wie kann man die Berechnung dieses Anteils noch realistischer gestalten?
#__________________________________________________________________________________________________________________________________________________________________

import random
import itertools

# Gewinnzahlen als Stichprobe von 6 Zahlen aus dem Zahlenpool von 1 bis 49
winning_numbers = random.sample(range(1, 50), 6)

won = 0                 
spent = 0

# Lotterie-Simulation für 100.000 Durchläufe
for _ in range(100000):

    # Generierte Spielerzahlen als Stichprobe von 6 Zahlen aus dem Zahlenpool von 1 bis 49
    players_numbers = random.sample(range(1, 50), 6)

    # Überprüfen, wie viele Zahlen in den Gewinnzahlen und den Spielerzahlen übereinstimmen
    match = sum(1 for i, j in itertools.product(range(6), range(6)) if winning_numbers[i] == players_numbers[j])

    won += 1 * match    # Addition des gewonnen Betrags, welcher von den matches abhängig ist
    spent += 1          # addition des gesamten eingesetzen Betrag des aktuellen Durchlaufs
    # Realistischer wird die Simulation durch tatsächliche Preise


print("Amount Won: ", won)
print("Amount Spent: ", spent)
print("Total Yield: ", won - spent)

