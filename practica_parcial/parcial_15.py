def validar(clave):
    mayus = 0
    minus = 0
    espacio_blanco = 0
    especiales = 0
    caracteres_especiales = "#&*$"
    digitos = 0
    contador = 0
    validacion = False
    if 8 <= len(clave) <= 12:
        while contador < len(clave) and validacion == False and espacio_blanco == 0:
            if clave[contador] == " ":
                espacio_blanco += 1
            elif clave[contador].isupper() and clave[contador].isalpha():
                mayus += 1
            elif clave[contador].islower() and clave[contador].isalpha():
                minus += 1
            elif clave[contador] in caracteres_especiales:
                especiales += 1
            elif clave[contador].isnumeric():
                digitos += 1
            contador += 1
            print(mayus,minus,especiales,digitos,espacio_blanco)
            if espacio_blanco == 0 and mayus >= 1 and minus >= 1 and especiales >= 1 and digitos >= 2:
                validacion = True
    return validacion

print(validar("Pepepepe33$")) 