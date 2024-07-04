def ingresar_valor():
    return float(input("Valor monetario a convertir: "))


def tipo_dolar(valor):
    return round(valor / 3.84, 2)


def tipo_euro(valor):
    return round(valor / 4.08, 2)


def tipo_yen(valor):
    return round(valor / 0.024, 2)
