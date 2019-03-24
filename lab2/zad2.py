#2 Find X & Y that satisfy: X is divisible by Y and both X & Y are even. (0.5p)

from cs50 import get_int


def even(number):
    is_even = number % 2 == 0
    return is_even


def divisible(number1, number2):
    is_even = number1 % number2 == 0
    return is_even


yourRange = -1

while yourRange <= 0:
    yourRange = get_int("Your range is: ")
    if yourRange <= 0:
        print("Enter a positive number!")


for x in range(1, yourRange+1):
    for y in range(1, x+1):
        even(x)
        even(y)
        divisible(x, y)
        if even(x) and even(y) and divisible(x, y):
            print(x, "and", y, "meet the requirements")
        else:
            print(x, "and", y, "do not meet the requirements")

