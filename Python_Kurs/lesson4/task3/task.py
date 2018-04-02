animals = ['elephant', 'lion', 'tiger', "giraffe", "monkey", 'dog']   # eine neue Liste erstellen
print(animals)

animals[1:3] = ['cat']    # Ersetze 2 Einträge -- 'lion' und 'tiger' durch den Eintrag -- 'cat'
print(animals)

animals[1:3] = []     # Lösche 2 Einträge -- 'cat' und 'giraffe' von der Liste
print(animals)

animals = []
print(animals)
