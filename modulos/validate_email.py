def validar(email):
    arroba = email.count("@")
    # != si no hay 1 o más de un @ es incorrecto
    # rfind = recorre de derecha a izquierda (para ver si el @ esta en la ultima posición)
    # find = recorre de izquierda a derecha (para ver si el @ esta en la primera posición)
    if arroba != 1 or email.rfind("@") == len(email) - 1 or email.find("@") == 0:
        return "Email es incorreto"
    else:
        return "Email es correcto"
