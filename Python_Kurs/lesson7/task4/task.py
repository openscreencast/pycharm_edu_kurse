def multiply_by(a, b=2):
    return a * b

print(multiply_by(3, 47))
print(multiply_by(3))    # Aufruf der Funktion mit Default-Wert für b-Parameter


def hello(subject, name="John"):
    print("Hello %s! My name is %s" % (subject, name))

hello("PyCharm", "Jane")    # Aufruf der 'hello'-Funktion mit "PyCharm" als Betreffparameter und "Jane" als Name
hello("PyCharm")            # Aufruf der 'hello'-Funktion mit "PyCharm" als Betreffparameter und der default-Wert als name
