class MyClass:
    variable1 = 1
    variable2 = 2

    def foo(self):     # der self-Parameter wird später erläutert
        print("Hello from function foo")

my_object = MyClass()
my_object1 = MyClass()

my_object.variable2 = 3     # ändert den Wert von variable2 in my_object

print(my_object.variable2)
print(my_object1.variable2)

my_object.foo()   # Aufruf der Methode foo() vom Objekt my_object

print(my_object.variable1)

