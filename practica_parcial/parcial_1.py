'''
Escribir una funcion en Python, para validar una nueva clave de acceso.
La función deberá recibir una cadena de caracteres, que contendrá la clave candidata, 
que fue previamente ingresada por el usuario.
Devolverá true o false, dependiendo de si cumple o no con las siguientes condiciones:

- La clave debe estar formada únicamente por, entre 4 y 8 caracteres solamente numéricos
- Los caracteres NO pueden ser todos iguales

La cadena sólo puede ser recorrida a lo sumo una vez.
Evitar ciclos innecesarios.

Ejemplos de resultados a obtener  si se invoca la función:


    >>> validar("j2020") 
    False
    >>> validar("20X20") 
    False
    >>> validar("2020a") 
    False
    >>> validar("2220") 
    True
    >>> validar("23445776") 
    True
    >>> validar("089") 
    False
    >>> validar("027845321") 
    False
    >>> validar("02784532") 
    True
    >>> validar("33333") 
    False
    '''
import doctest
def validar(cadena):
    validacion = False
    contador = 0
    while 4 <= len(cadena) <= 8 and cadena.isnumeric() and contador < len(cadena) and validacion == False:
        if cadena[0] == cadena[contador]:
            contador += 1
        else:
            validacion = True   
    return validacion

print(doctest.testmod())
validar("3333")




