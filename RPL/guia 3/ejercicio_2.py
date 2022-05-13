'''
Completar el cuerpo de la función. La misma recibe una cadena de caracteres y 
dos caracteres individuales. Debe retornar la suma de la cantidad de veces que aparecen cada uno de los caracteres en la cadena.

Hint: No utilizar la función .count() de las cadenas. Cada vez que la invocamos, 
Python realiza un recorrido por la cadena buscando la subcadena que la función recibe como parámetro. 
Resolver el ejercicio realizando una única iteración en toda la cadena.

Ejemplo:

    contar_caracteres("casa", "c", "a") => 3
    contar_caracteres("cosa", "c", "a") => 2
    contar_caracteres("algoritmos", "a", "o") => 3
    contar_caracteres("algoritmos", "w", "x") => 0
'''

def contar_caracteres(cadena:str,caracter_1:str,caracter_2:str):
    #funcion que recorre una cadena y devuelve la cantidad de caracteres total que el usuario busca
    suma = 0
    for caracter in cadena:
        if caracter == caracter_1 or caracter == caracter_2:
            suma += 1
    return suma

print(contar_caracteres("cosa","c","a"))
