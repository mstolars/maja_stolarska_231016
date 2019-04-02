from math import pi


def field(figure_type, x = -1, y = -1):
    if figure_type == "circle":
        if x <= 0:
            print("Length cannot be equal to or below zero")
            exit()
        else:
            circle_field = pi*x**2
            print(f"Field of the circle for a given radius ({x}) is equal to: {circle_field}")
            return circle_field
    elif figure_type == "rectangle":
        if x <= 0 or y <= 0:
            print("Length cannot be equal to or below zero")
            exit()
        else:
            rectangle_field = x*y
            print(f"Field of the rectangle for given side lengths ({x}, {y}) is equal to: {rectangle_field}")
            return rectangle_field
    elif figure_type == "triangle":
        if x <= 0 or y <= 0:
            print("Length cannot be equal to or below zero")
            exit()
        else:
            triangle_field = x*y/2
            print(f"Field of the rectangle for given side lengths ({x}, {y}) is equal to: {triangle_field}")
            return triangle_field
    elif figure_type == "rhombus":
        if x <= 0 or y <= 0:
            print("Length cannot be equal to or below zero")
            exit()
        else:
            rhombus_field = x*y/2
            print(f"Field of the rectangle for given side lengths ({x}, {y}) is equal to: {rhombus_field}")
            return rhombus_field
    else:
        print("Enter a proper figure (circle, rectangle, triangle or rhombus)!!")


def compare(f1=[], f2=[]):
    if len(f1) > 3 or len(f2) > 3:
        print("You entered too many arguments!")
        exit()
    elif len(f1) < 3 or len(f2):
        for i in range(3-len(f1)):
            f1.append(None)
        for i in range(3-len(f2)):
            f2.append(None)

    field1 = field(f1[0], f1[1], f1[2])
    field2 = field(f2[0], f2[1], f2[2])
    print(field1, field2)
    if field1 > field2:
        print(f"The first figure ({f1[0]}) has a larger field")
    elif field1 < field2:
        print(f"The second figure ({f2[0]}) has a larger field")
    elif field1 == field2:
        print(f"The figures ({f1[0]}, {f2[0]}) have equal fields")
    else:
        print("The values must have been wrong!")


compare(['circle', 5],['triangle', 15, 8])