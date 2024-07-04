# salario: precio por horas * cantidad de horas
# bonificación: (A:40%, B:25%, C:10%, D:5%) por el salario total
# salario final: salario + bonificación
def salario(h, c):
    return h * c


def bonificación(_):
    dic = {"A": 0.40, "B": 0.25, "C": 0.10, "D": 0.05}
    tp = input("Indicar el tipo de bonificación(A, B, C, D): ").upper()
    for tipo, valor in dic.items():
        if tp == tipo:
            return valor
    return 0.0


def total(s, b):
    t = b + s
    return t
