import math

def square(side):
    area = side ** 2
    return math.ceil(area)

print(square(5))
print(square(4.2))
print(square(3.1))
