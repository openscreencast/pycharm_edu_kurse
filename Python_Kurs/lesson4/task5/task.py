# ein neues Dictionary erstellen
phone_book = {"John": 123, "Jane": 234, "Jerard": 345}    # "John", "Jane" and "Jerard" sind Schlüssel (Keys) und die Zahlen sind die Werte
print(phone_book)

# einen neuen Wert zum Dictionary hinzufügen
phone_book["Jill"] = 345
print(phone_book)

# ein Schlüssel-Wert-Paar von phone_book löschen
del phone_book['John']

print(phone_book["Jane"])
