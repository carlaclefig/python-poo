import random


def num_rd():
    return random.randint(1, 10)


def compare(num_random):
    num = int(input("Ingrese un número: "))
    if num > num_random:
        print("El número es menor...")
    elif num == num_random:
        print("Has ganado!")
    else:
        print("El número es mayor...")
