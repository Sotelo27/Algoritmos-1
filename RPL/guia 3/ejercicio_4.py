'''
Completar el cuerpo de la función. La misma debe tomar la cadena que se pasa como parámetro e insertar 
el separador cada tantos caracteres como indique el parámetro "espaciado".

Ejemplos:

   insertar_separadores("255255255255", ".", 3) => "255.255.255.255"
   insertar_separadores("holacomoestas", "|", 4) => "hola|como|esta|s"  
'''
def insertar_separadores(cadena, separador, espaciado):
    cadena_auxiliar = ""
    contador = 0
    contador_total = 0
    for caracter in range(len(cadena)):
        contador += 1
        cadena_auxiliar += cadena[caracter]
        contador_total += 1
        if contador == espaciado and contador_total < len(cadena) :
            contador = 0
            cadena_auxiliar += separador
    return cadena_auxiliar

#insertar_separadores("255255255255", ".", 3)
cadena = "hola"
print(cadena[::3])