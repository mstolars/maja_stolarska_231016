from cs50 import get_int
from math import pi


def circle():
    x = -1
    print("Enter a radius of the circle:")
    while x <= 0:
        x = get_int("x: ")
        if x <= 0:
            print("Enter a positive number!")
    print(f"Field of the circle for a given radius ({x}) is equal to: {pi*x**2}")


def rectangle():
    x = -1
    y = -1
    print("Enter the length of a rectangle's sides:")
    while x <= 0:
        x = get_int("x: ")
        if x <= 0:
            print("Enter a positive number!")
    while y <= 0:
        y = get_int("y: ")
        if y <= 0:
            print("Enter a positive number!")
    print(f"Field of the rectangle for given side lengths ({x}, {y}) is equal to: {x*y}")


def triangle():
    x = -1
    y = -1
    print("Enter the length of a triangle height and base:")
    while x <= 0:
        x = get_int("h: ")
        if x <= 0:
            print("Enter a positive number!")
    while y <= 0:
        y = get_int("b: ")
        if y <= 0:
            print("Enter a positive number!")
    print(f"Field of the rectangle for given side lengths ({x}, {y}) is equal to: {x*y/2}")


def rhombus():
    x = -1
    y = -1
    print("Enter the length of rhombus's diagonals:")
    while x <= 0:
        x = get_int("x: ")
        if x <= 0:
            print("Enter a positive number!")
    while y <= 0:
        y = get_int("y: ")
        if y <= 0:
            print("Enter a positive number!")
    print(f"Field of the rectangle for given side lengths ({x}, {y}) is equal to: {x*y/2}")


while True:
    print("Enter a desired figure (circle, rectangle, triangle or rhombus). When you're finished, type \"end\" ")
    figure = str(input())
    if figure == "circle":
        circle()
    elif figure == "rectangle":
        rectangle()
    elif figure == "triangle":
        triangle()
    elif figure == "rhombus":
        rhombus()
    elif figure == "end":
        break
    else:
        print("Enter a proper figure (circle, rectangle, triangle or rhombus)!!")


