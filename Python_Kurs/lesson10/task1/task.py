
f = open("input.txt", "r")   # hier öffnen wir die Datei "input.txt". r wird verwendet, um zu identifizieren, dass wir die Datei lesen wollen
                             # Hinweis: Wenn du in die Datei schreiben willst, verwende "w" als zweites Argument

for line in f.readlines():   # Zeilen lesen
    print(line)

f.close()                   # Es ist wichtig, die Datei zu schließen, um alle Systemressourcen freizugeben.

f1 = open("input1.txt", "r")

print(f1.readline())

f1.close()
