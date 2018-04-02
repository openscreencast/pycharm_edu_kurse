Aufteilung (Slicing) wird verwendet,
um mehrere Zeichen
(eine Teilzeichenkette) aus einer
Zeichenkette (String) zu erhalten.
Die Syntax ist ähnlich wie bei
der Indexierung, aber statt nur
einem Index verwende zwei Indexe
(Zahlen), die durch einen
Doppelpunkt getrennt sind,
z.B. `str[ind1:ind2]`.

Beispiel

```
str[start:end] # Einträge starten durch end-1
str[start:] # Einträge starten durch den Rest des Arrays
str[:end] # Einträge von Anfang bis Ende-1
str[:] # eine Kopie des gesamten Arrays
```

Verwende Slicing, um `"Python"`
aus der Variable `monty_python`
zu erhalten.

