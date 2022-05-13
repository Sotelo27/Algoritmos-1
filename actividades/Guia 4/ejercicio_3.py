'''
Escribir una función que reciba una dirección de mail, y devuelva True ó False, en función de haber 
evaluado que dicha dirección está bien formada. 
Escribir una función que reciba una cadena de caracteres que representa una dirección de mail. La 
función deberá devolver True ó False, en función de haber evaluado que dicha dirección está bien 
formada. 
Se debe controla que:  
a.  Que no contenga blancos 
b.  Que sólo se utilicen letras y/o números para la parte del nombre, delante de la @ 
c.  Que haya exactamente una arroba 
d.  Que los nombres de dominio sean: fi.uba.ar ó gmail.com 
'''

def validar_email_1(correo):
    validacion = False
    if type(correo) == str and correo != "":
        contador_caracteres = 0
        contador_arrobas = 0
        contador_caracteres_invalidos = 0
        posicion_arroba = 0
        dominio = ""
        while contador_arrobas != 2 and contador_caracteres < len(correo) :
            if correo[contador_caracteres] == "@":
                contador_arrobas += 1
                posicion_arroba = contador_caracteres
                dominio = correo[posicion_arroba:]
            contador_caracteres += 1
        contador_caracteres = 0
        while contador_caracteres_invalidos == 0 and correo[contador_caracteres] != "@":
            if correo[contador_caracteres] not in ("1234567890qwertyuiopasdfghjklñzxcvbnm"):
                contador_caracteres_invalidos +=1
            contador_caracteres += 1
        if contador_arrobas == 1 and contador_caracteres_invalidos == 0 and (dominio == "@gmail.com" or dominio == "@fi.uba.ar") :
            validacion = True
    return validacion

def validar_email_2(correo):
    validacion = False
    if type(correo) == str and correo.count("@") == 1 and correo != "":
        posicion_arroba = correo.find("@")
        dominio = correo[posicion_arroba:]
        contador = 0
        contador_caracteres_invalidos = 0
        while contador_caracteres_invalidos == 0 and correo[contador] != "@":
            if correo[contador] not in ("1234567890qwertyuiopasdfghjklñzxcvbnm"):
                contador_caracteres_invalidos += 1
            contador += 1
        if contador_caracteres_invalidos == 0 and (dominio == "@gmail.com" or dominio == "@fi.uba.ar"):
            validacion = True
    print(validacion)
    return validacion



            
            
      