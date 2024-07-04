cadena = "Curso de Python"
print(cadena.count("o"))  # retorna el número de veces que se repite el argumento
print(cadena.upper())  # retorna en mayuscula toda la cadena de texto
print(cadena.lower())  # retorna en minuscula toda la cadena de texto

# retorna la ubicación en la que se encuentra el argumento, si no existe lanza -1
print(cadena.find("t"))

# retorna la ubicación en la que se encuentra el argumento, si no existe lanza ValueError
print(cadena.index("u"))

# retorna tru o false, si el argumento es el incial en la cadena de texto
print(cadena.startswith("Curso"))

# retorna tru o false, si el argumento es el final en la cadena de texto
print(cadena.startswith("de"))

print(cadena.split())  # retorna como lista el argumento
