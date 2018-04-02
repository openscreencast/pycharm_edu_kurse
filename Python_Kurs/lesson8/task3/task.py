class Car:
    color = ""
    def description(self):
        description_string = "Das ist ein %s Auto." % self.color    # der self-Parameter wird später erläutert
        return description_string

car1 = Car()
car2 = Car()

car1.color = "blaues"
car2.color = "rotes"

print(car1.description())
print(car2.description())
