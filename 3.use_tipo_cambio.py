from modulos.tipo_cambio import *  # pylint: disable=wildcard-import

soles = ingresar_valor()

print("Monto en dolares: ", tipo_dolar(soles))
print("Monto en euros: ", tipo_euro(soles))
print("Monto en yen: ", tipo_yen(soles))
