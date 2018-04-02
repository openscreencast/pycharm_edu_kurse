class Square:

    def __init__(self):    # spezielle Methode __init__
        self.sides = 4

square = Square()
print(square.sides)

class Car:
    def __init__(self, color):
        self.color = color

car = Car("blau")    # Hinweis: Du solltest den self-Parameter nicht explizit übergeben, sondern nur den color-Parameter

print(car.color)
