""" ------------Example 01------------ """

try:  # indicar la exepción
    print(2 / 0)
except:  # pylint: disable=bare-except
    print("No se puede dividir con 0, \n")

# ------------Example 02------------

lista = ["Cesar", "Mario", "Juan"]

try:
    print(lista[4])
except:  # pylint: disable=bare-except
    print("Indice no existe, \n")

# ------------Example 03------------

try:
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    importe = precio * cantidad
    print("Importe: ", importe)
except:  # pylint: disable=bare-except
    print("Ingreso de tipos de datos erroneo")
