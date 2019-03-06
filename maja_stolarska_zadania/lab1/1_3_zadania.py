#1 calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100] (0.5p)

import math

for i in range(56, 101):
    print('The value of function for i=', i, 'is', 2*i**2+2*i+2)

#2 ask the user for a number and print its factorial (1p)

print('Insert your value here:')
x = int(input())
factorial = 1

print('your factorial is: ', math.factorial(x))

for i in range(1, x+1):
    factorial = factorial*i

print(factorial)

#3 write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value (1p)

array = [14, 1, 3, 4, 5, 1, 2, 1]


def my_function(arr):
    min_value = min(arr)

    print('The lowest value in the array:', min_value, 'and the index is:',)
    for i in range(len(arr)):
        if arr[i] == min_value:
            print(i)


my_function(array)
