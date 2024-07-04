from modulos.sales import *  # pylint: disable=wildcard-import

p = float(input("Precio: "))
c = float(input("Cantidad: "))

imp = amount(p, c)
iGv = igv(imp)
t = total(imp, iGv)

print("Importe: ", imp)
print("IGV: ", iGv)
print("Total: ", t)
