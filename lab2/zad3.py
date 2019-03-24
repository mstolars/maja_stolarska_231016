#4 Add rounding for the above x/y operation. Round to 2 decimal points. Hint: look up in Google "python limiting number of decimals". (1p)

from cs50 import get_int

x = get_int("x: ")
y = get_int("y: ")

print("Your x = ", x)
print("Your y = ", y)

print(f"x / y: {round(x / y, 1)}")