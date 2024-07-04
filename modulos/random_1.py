import random


def carga(amount):
    lista = []
    for _ in range(amount):  # cuando no se usa la variable se coloca "_"
        num = random.randint(0, 1000)
        lista.append(num)
    return lista


def imprimir(lista):
    for x in lista:
        print(x)
