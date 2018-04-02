count = 0

while True:  # diese kann niemals False sein
    print(count)
    count += 1
    if count >= 5:
        break           # beendet die Schleife wenn count >= 5


zoo = ["lion", 'tiger', 'elephant']
while True:                         # diese kann niemals False sein
    animal = zoo.pop()       # extrahiert ein Element vom Schleifenende
    print(animal)
    if animal == 'elephant':
        break           # beendet die Schleife
