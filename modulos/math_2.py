import math


def user():
    return int(input("Ingrese un número: "))


def numero(num):
    print("La raíz cuadrada de ", num, " es: ", math.sqrt(num))
    print("Elevado al cuadrado de ", num, " es: ", math.pow(num, 2))
    print("Elevado al cubo de ", num, " es: ", math.pow(num, 3))
