'''
Escribir un programa que solicite el ingreso de palabras ó frases, y a medida que se ingresan informar si se 
trata de un palíndromo. 
Validar que la palabra ó frase ingresada, sólo este formada por caracteres alfabéticos y por espacios en 
blanco. 
El ingreso de las palabras ó frases, terminará cuando el usuario de enter, sin ingresar nada. 
La solución debe ser estructurada en funciones, que sigan los lineamientos de la programación 
estructurada. Reutilice el código de ejercicios anteriores. 
'''
def definir_palindromo(cadena):
    contador = 0 
    auxiliar = ""
    while contador < len(cadena):
            if cadena[contador] != " ":
                auxiliar += cadena[contador]
            contador += 1
    if auxiliar.upper() == auxiliar.upper()[::-1]:
            print("Es palindromo\n")
    else:
        print("No es palindromo")

def validar_caracteres(cadena):
    validacion = False
    caracteres_validos = "QWERTYUIOPASDFGHJKLÑZXCVBNM "
    if type(cadena) == str and type(caracteres_validos) == str:
        contador = 0
        while contador < len(cadena) and cadena.upper()[contador] in caracteres_validos:
            contador += 1
        if contador == len(cadena) and contador != 0 :
            validacion = True
    return validacion

def main():
    print("A continuacion, ingrese una cadena, solo conformada por caracteres alfabeticos y espacios en blanco, caso contrario sera invalida,para finalizar ingreso presione enter.\n")
    cadena = input("Ingresa la cadena: ")
    validar_cadena = validar_caracteres(cadena)
    if validar_cadena == True:
        print("Ahora se informara si la cadena es un palindromo: ")
        definir_palindromo(cadena)
    else:
        print("A ingresado una palabra no valida")

main()