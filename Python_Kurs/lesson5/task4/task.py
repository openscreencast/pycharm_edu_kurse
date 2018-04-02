x = 28

if x < 0:
    print('x < 0')                     # nur ausführen wenn x < 0
elif x == 0:
    print('x is zero')                 # Wenn es nicht wahr ist, dass x < 0 ist, prüfen ob x == 0 ist
elif x == 1:
    print('x == 1')                    # Wenn es nicht stimmt, dass x < 0 und x != 0, überprüfen ob x == 1
else:
    print('nichts davon ist wahr')

name = "John"

if name == "John":
    print(True)
else:
    print(False)
