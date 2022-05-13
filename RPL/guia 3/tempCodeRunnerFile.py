def sumar_caracteres_numericos(cadena):
    suma = 0
    for caracter in cadena:
        if caracter.isnumeric():
            suma += int(caracter)
    return suma