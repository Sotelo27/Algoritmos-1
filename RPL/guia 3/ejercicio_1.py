'''
Completar el cuerpo de la función. La misma recibe tres cadenas previamente inicializadas y 
debe retornar la suma de la longitud de la concatenación de las tres cadenas.

Ejemplo:

    longitud_cadenas("hola", "como", "estas") => 13
    longitud_cadenas("a", "b", "c") => 3
'''

def longitud_cadenas(cadena_1,cadena_2,cadena_3):
    longitud_cadenas = len(cadena_1) + len(cadena_2) + len(cadena_3)
    return longitud_cadenas


print(longitud_cadenas("hola","como","estas"))