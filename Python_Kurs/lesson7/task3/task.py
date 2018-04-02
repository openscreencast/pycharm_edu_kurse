def sum_two_numbers(a, b):
    return a + b            # Ergebnis an den Funktionsaufrufer zurückgeben

c = sum_two_numbers(3, 12)  # Ergebnis der Funktion der Variable 'c' zuweisen


def fib(n):
    """Dies ist ein Dokumentationsstring für die Funktion. Er wird durch fib.__doc__() verfügbar sein
    Gibt eine Liste zurück, die die Fibonacci-Serie bis zu n enthält."""
    result = []
    a = 1
    b = 1
    while a < n:
        result.append(a)
        tmp_var = b
        b = a + b
        a = tmp_var
    return result

print(fib(10))
