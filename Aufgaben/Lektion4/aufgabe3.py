# Berechnen Sie die Shannon Entropie für den Textstring S = “Eine alte Dame geht heute einkaufen.” 
# mithilfe der in Aufgabe 2 festgelegten Berechnungsvorschriften. Zur
# Berechnung der Shannon Entropie wird die Wahrscheinlichkeitsverteilung pi durch die Häufigkeitsverteilung 
# der Buchstaben in dem Textstring S definiert.
#----------------------------------------------------------------------------------------------------------------
import math


S = "Eine alte Dame geht heute einkaufen."

def getAlphabetnumber(letter):
    res = ord(str(letter).lower())-ord('a')
    return 0 if res > 25 or res < 0 else res 

sentence = S.lower()
counts = {}
length = 0
letterCounts = {}

for letter in sentence:
    if getAlphabetnumber(letter) > 0 or letter == 'a':  # überprüfen ob es ein Buchstabe ist
        letterCounts[letter] = sentence.count(letter)   # Zählen wie oft der Buchstabe vorkommt
        length += 1

probs = [count/length for count in letterCounts.values()]
result = sum((-prob*math.log2(prob)) for prob in probs)

print(result)
