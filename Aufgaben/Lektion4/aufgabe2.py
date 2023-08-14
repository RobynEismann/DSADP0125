# Entwickeln Sie eine Routine in Python, welche dem Textstring S = “Eine alte Dame geht heute
# einkaufen.” einen Zahlenwert zuordnet, durch die Definition a = b mod 26. Dabei ist b ∈ Z ein
# Zahlenwert, welcher den Index der Buchstabenfolge a, b, c, d, ..., bzw. A, B, C, D, ..., beschreibt
# und a ∈ Z26 der resultierende Zahlenwert (mod 26) für einen Buchstaben aus dem Textstring S.
#---------------------------------------------------------------------------


def getAlphabetNumber(letter):                          # Diese Funktion berechnet den numerischen Wert eines Buchstabens im Alphabet
    
    res = ord(str(letter).lower())-ord('a')             # Berechne den Abstand zum Buchstaben 'a'
    return 0 if res > 25 or res < 0 else res            # sicherstellen, dass der Wert im Bereich von 0 bis 25 ist (mod 26)


S = "Eine alte Dame geht heute einkaufen."
sum = 0

for letter in S:
    number = getAlphabetNumber(letter)                  # Erhalten des numerischen Wert des Buchstabens
    sum += number                                       # Addieren der Werte aus dem String

print(sum)