'''

Completar el cuerpo de la función. La misma debe retornar valor un valor booleano: True en caso de que la contraseña sea válida, False en caso contrario.
Se considera válida una contraseña si:

Tiene al menos un número.
Tiene al menos una mayúscula.
Tiene al menos un caracter no alfanumérico
(Hint: Se puede evaluar utilizando la conjunción de la negación entre .isalpha() y
la negación de .isnumeric())
Tiene una longitud mayor a 7 caracteres pero menor a 15.
Ejemplo:

   validar_contraseña("!Algoritmos123") => True
   validar_contraseña("!Algoritmos123!Algoritmos123") => False
   validar_contraseña("algoritmos") => False
   validar_contraseña("algoritmos123") => False
   validar_contraseña("Algoritmos123") => False
   validar_contraseña("!Alg123") => False
'''

def contar_caracteres(cadena:str):
    #funcion que recorre una cadena y cuenta sus caracteres
    suma = 0
    for suma in range(len(cadena)):
        suma += 1
    return suma

def comprobar_mayus(cadena):
    validacion = False
    for posicion in range(len(cadena)):
        caracter = cadena[posicion]
        if caracter.isupper():
            validacion = True
    return validacion

def validar_contrasenia(cadena):
    #funcion que analizando ciertas condiciones, valida o no una contraseña
    caracteres_totales = contar_caracteres(cadena)
    validacion = False
    validar_mayus = comprobar_mayus(cadena)
    if (caracteres_totales > 7 and caracteres_totales < 15) and cadena.isalnum() == False and validar_mayus == True:
        validacion = True
    return validacion

hola = "hola"
#print(hola.isalnum())
#print(validar_contraseña("Algoritmos123"))
validar_contrasenia("!Algoritmos123") 
validar_contrasenia("!Algoritmos123!Algoritmos123") 
validar_contrasenia("algoritmos") 
validar_contrasenia("algoritmos123") 
validar_contrasenia("Algoritmos123") 
validar_contrasenia("!Alg123") 
