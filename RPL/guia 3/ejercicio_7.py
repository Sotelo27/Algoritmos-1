'''
Completar el cuerpo de la función. La misma recibe una cadena como parámetro y 
debe retornar el resultado de sumar todos los caracteres numéricos que aparezcan en la misma.

Ejemplo:

    sumar_caracteres_numericos("1") => 1
    sumar_caracteres_numericos("a1") => 1
    sumar_caracteres_numericos("12") => 3
    sumar_caracteres_numericos("123") => 6
    sumar_caracteres_numericos("o1la293fr") => 1 + 2 + 9 + 3 = 15
'''


def sumar_caracteres_numericos(cadena):
    suma = 0
    for caracter in cadena:
        if caracter.isnumeric():
            suma += int(caracter)
    return suma

sumar_caracteres_numericos("1")
sumar_caracteres_numericos("o1la293fr")
