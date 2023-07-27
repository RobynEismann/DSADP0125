import random

stack = [random.randint(0, 100) for _ in range(25)]

print (stack)

# Die Wahrscheinlichkeit für das Vorkommen eines solchen Stapels ist
# 1/(100^25) da jede der 25 Stellen einen wert von 0 bis 100 belegen kann