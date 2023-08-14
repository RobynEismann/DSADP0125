# Schreiben Sie ein Programm in der Programmiersprache Python, welches die Häufigkeitsverteilung
# von Wörtern in einem Textstring berechnet. Die zu suchenden Wörter sollen dabei durch einen
# Nutzer von außen eingegeben werden und in dem Text gesucht werden, der unter der Domain
# https://github.com/alexej-schelle/AlgDatPro/ unter dem Dateinamen PythonString.txt
# zu finden ist.
#----------------------------------------------------------------------------------------------------------------

def count (sentence,word):              # Funktion zur Zählung der Häufigkeit eines Wortes im Satz

    word = word.lower()
    counted = sentence.count(word)

    return counted/len(sentence)*100    # Berechnen des Prozentsatzes der Wortvorkommen im Satz


example = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."
example = example.lower().split()     # Bereinigen und Aufteilen des Satzes in Wörter

search = input("Please enter a word to be searched: ")
result = count(example,search)

print(f"The word '{search}' appears in the sentence with a frequency of {result:.2f}%.")
