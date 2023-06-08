import math

#Zadanie 1
def sqrtQuadraticEquation(a, b, c):
    if a == 0:
        return "this is not a quadratic equation"
    d = b * b - 4 * a * c
    if d < 0:
        return "No roots"
    elif d == 0:
        return -b / 2 * a
    else:
        return (-b + math.sqrt(d)) / 2 * a, (-b - math.sqrt(d)) / 2 * a

#Zadanie 2
def numberOfNegativeNumbers(array):
    licznik = 0
    for i in range(0, len(array)):
        if array[i] < 0:
            licznik = licznik + 1
    return licznik

#Zadanie 3
def isNumberExistInArray(array, x):
    for i in range(0, len(array)):
        if array[i] == x:
            return True
    return False

#Zadanie 4
def minInArray(array):
    min = array[0]
    for i in range(1, len(array)):
        if array[i] < min:
            min = array[i]
    return min
