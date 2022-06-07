'''
Escribir una funcion en Python, para validar una nueva clave de acceso.
La función deberá recibir una cadena de caracteres, que contendrá 
la clave candidata, que fue previamente ingresada por el usuario.
Devolverá true o false, dependiendo de si cumple o no con las siguientes condiciones:

- La clave debe estar formada únicamente por, entre 4 y 8 caracteres solamente numéricos
- Los caracteres NO pueden ser todos iguales

La cadena sólo puede ser recorrida a lo sumo una vez.
Evitar ciclos innecesarios.

Ejemplos de resultados a obtener  si se invoca la función:

validar("j2020") devuevle False
validar("20X20") devuevle False
validar("2020a") devuevle False
validar("2220") devuelve True
validar("23445776") devuelve True
validar("089") devuelve False
validar("027845321") devuelve False
validar("02784532") devuelve True
validar("33333") devuelve False
'''

def validar_clave(clave):
    validacion = False
    contador = 0
    if clave.isnumeric() and 4 <= len(clave) <= 8:
        while clave[0] == clave[contador] and contador < len(clave):
            contador += 1
        if contador < len(clave):
            validacion = True
    return validacion

print(validar_clave("23445776"))
