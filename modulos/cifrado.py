# --------------------- Exercise 01 ----------------------


def cifrar(mensaje, codigo):
    msj_cifrado = ""
    # Bucle para iterar por cada letra del mensaje original
    for x in mensaje:  # computadora
        x = x.upper()  # C
        # ascii; ord es obtener el valor ASCII del carácter
        ascii = ord(x) + codigo  # 67+1=68
        if ascii > ord("Z"):
            ascii = ord("A")
        # Concatenar cada caracter en el mensaje cifrado
        # chr: retorna de número a letra
        msj_cifrado += chr(ascii)  # D

    return msj_cifrado


# --------------------- Exercise 02 ----------------------


def descifrar(mensaje, codigo):
    msj_descifrado = ""
    # Bucle para iterar por cada letra del mensaje original
    for x in mensaje:
        # ascii; ord es obtener el valor ASCII del carácter
        ascii = ord(x) - codigo  # 67+1=68
        if ascii < ord("A"):
            ascii = ord("Z")
        # Concatenar cada caracter en el mensaje cifrado
        # chr: retorna de número a letra
        msj_descifrado += chr(ascii)  # D

    return msj_descifrado
