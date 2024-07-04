from modulos.planilla import salario, bonificación, total

h = float(input("Precio por hora: "))
c = float(input("Cantidad de horas: "))

sl = salario(h, c)
bn = bonificación(sl)
x = sl * bn
t = total(sl, x)

print("**************************")
print("Salario: ", sl)
print("Bonificación: ", bn)
print("Total: ", t)
