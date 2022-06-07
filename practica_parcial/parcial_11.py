'''
Escribir en python una funcion validar que recibe un string por parametro y valida una clave de acceso 
a un sitio web
la clave debe cumplir lo siguiente:
Debe tener entre 6 y 10 caracteres
debe tener por lo menos un caracter alfabetico en mayusculas
debe tener por lo menos un caracter alfabetico en minusculas
debe tener por lo menos un digito numero entre 0 y 9 
no puede tener ningun espacio en wblanco
la funcion debe devolver true y cunple las condiciones , false de lo contrario
'''

def validar_clave(clave):
    validacion = False
    contador = 0
    mayus = 0
    minus = 0
    numero = 0
    if clave.isalnum() and 6 <= len(clave) <= 10:
        while contador < len(clave)  and validacion == False:
            print(clave[contador])
            if clave[contador].isnumeric():
                numero += 1 #esta comprobacion se debe a que isnum devuelve true siempre que sean todas letras o numeros o juntos, por lo tanto isalnum no comprueba al 100%
            elif clave[contador] == clave[contador].upper():
                mayus += 1
            elif clave[contador] == clave[contador].lower():
                minus += 1
            contador += 1
            print(mayus,minus,numero)
            if mayus >= 1 and minus >= 1 and numero >= 1:
                validacion = True
    return validacion

print(validar_clave("Pep7epee7"))

        


