#1 Perimeter & field of circles with given radius X for the first circle & Y for the second one.

from cs50 import get_int
from math import pi

y = -1
x = -1

while x <= 0:
    x = get_int("x: ")
    if x <= 0:
        print("Enter a positive number!")

while y <= 0:
    y = get_int("y: ")
    if y <= 0:
        print("Enter a positive number!")

print("Your x = ", x)
print("Your y = ", y)

print(f"Perimeter of the first circle is equal to: {2*pi*x} and the field is equal to: {pi*x**2}")
print("Perimeter of the second  circle is equal to:", 2*pi*y, 'and the field is equal to:', pi*y**2)
