square = 1

while square <= 10:
    print(square)    # dies wird 10 mal ausgeführt
    square += 1      # dies wird 10 mal ausgeführt

print("Finished")  # dies wird 1 mal ausgeführt

square = 0
number = 1

while number < 10:
    square = number ** 2
    print(square)
    number += 1
