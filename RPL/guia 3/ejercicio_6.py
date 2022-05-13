'''
Completar el cuerpo de la función. La misma recibe una cadena y debe retornar la 
misma habiendo filtrado todas las vocales que contenía.

Ejemplos:

    filtrador_de_vocales("hola") => "hl"
    filtrador_de_vocales("facultad") => "fcltd"
    filtrador_de_vocales("algoritmos") => "lgrtms" 
'''

def filtrador_de_vocales(cadena):
    cadena_final = ""
    for caracter in cadena:
        if caracter not in ("aeiou"):
            cadena_final += caracter
    return cadena_final

filtrador_de_vocales("hola")