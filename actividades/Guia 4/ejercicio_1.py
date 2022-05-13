'''
Escribir una función que reciba una cadena de caracteres. La función deberá evaluar si la cadena recibida
representa un número binario, y en ese caso devolver True, de lo contrario, deberá devolver False
'''
def buscar_binarario(cadena):
    contador = 0
    if type(cadena) == str:
        validacion = True
        while contador < len(cadena) and (cadena[contador] == "0" or cadena[contador] == "1"):
            contador += 1
    if contador == 0 or contador > len(cadena) or contador < len(cadena) :
        validacion = False
    print(validacion)
    return validacion
        


buscar_binarario("010111")
buscar_binarario("030111")
buscar_binarario("3010111")
buscar_binarario("0101113")
buscar_binarario("algoritmosalgoritmos")
buscar_binarario("0 0 0 0 0 0 1 1 ")
buscar_binarario("")
buscar_binarario("1")
buscar_binarario(1)
