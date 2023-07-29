# Schreiben Sie eine Routine in Python, welche die Gewinne eines Teilnehmers an der Lotterie bei
# einem drei Türen Problem nach der Monty-Hall Strategie illustriert. 
# Hinweis: Nutzen Sie dabei die Grundlagen für ein Lotteriesystem nach Monty Hall mit drei Türen, 
# d. h. die Wahrscheinlichkeitstheorie einer Ziehung nach der Bayesschen Statistik
#__________________________________________________________________________________________________________________________________________________________________

import random

wins_stay = 0
wins_switch = 0

# Führe das Experiment 10.000 Mal durch
for _ in range(10000):
    doors = [1, 2, 3]
    winner = random.choice(doors)  # Zufällige Auswahl der Tür, hinter der der Preis liegt
    choice = random.choice(doors)  # Zufällige Auswahl der Tür durch den Teilnehmer

    monty_choices = [door for door in doors if door not in [winner, choice]]
    monty_choice = random.choice(monty_choices)

    # Verbleibende Türen nachdem Monty eine Tür geöffnet hat
    remaining_doors = [door for door in doors if door not in [choice, monty_choice]]

    if choice == winner:
        wins_stay += 1              # Inkrementieren wenn der Teilnehmer bei seiner Wahl bleibt
    else:
        wins_switch += 1            # Inkrementieren wenn der Teilnehmer die Tür wechselt

# Berechnung der Gewinnwahrscheinlichkeiten
probability_stay = wins_stay / 10000
probability_switch = wins_switch / 10000

print(f"Anzahl der Gewinne bei Beibehaltung der ersten Wahl: {probability_stay}")
print(f"Anzahl der Gewinne bei Wechseln der Wahl: {probability_switch}")





