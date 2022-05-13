'''
Escribir una función que reciba una cadena de caracteres a validar, y un segundo parámetro, que 
contenga una cadena con los caracteres válidos. La función debe devolver True, si la cadena a validar, está 
formada sólo por caracteres válidos; en caso contrario, deberá devolver False.
'''

def validar_caracteres(cadena,caracteres_validos):
    validacion = False
    if type(cadena) == str and type(caracteres_validos) == str:
        contador = 0
        while contador < len(cadena) and cadena[contador] in caracteres_validos:
            contador += 1

        if contador == len(cadena) and contador != 0 :
            validacion = True
    return validacion

print(validar_caracteres("hhggghghghhghhghhghhgh","hgt"))
print(validar_caracteres(1,2))
print(validar_caracteres("3",2))
print(validar_caracteres(2,"3"))
print(validar_caracteres("555566778","6578"))
print(validar_caracteres("33","334"))
print(validar_caracteres("1225","3122"))