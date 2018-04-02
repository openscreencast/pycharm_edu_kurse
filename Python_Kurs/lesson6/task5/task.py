for i in range(5):
    if i == 3:
        continue   # überspringt den Rest des Codes innerhalb der Schleife für den aktuellen i-Wert
    print(i)

for x in range(10):
    if x % 2 == 0:
        continue   # überspringt print(x) für diese Schleife
    print(x)
