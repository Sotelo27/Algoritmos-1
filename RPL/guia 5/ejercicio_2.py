# tu codigo
'''
Este ejercicio requiere la construcción de un pequeño programa que sirva para registrar votos correspondientes a una votación y 
determinar cuál fue el partido ganador.

Para esto, deberemos comenzar solicitando al usuario que ingrese votos para los distintos partidos hasta que decida finalizar la carga.
En un diccionario, se tienen que ir contabilizando los votos que llegan para los distintos partidos. Es posible que haya votos que lleguen 
al centro de votación para un partido para el cual se recibieron votos previamente.

Finalmente, se tienen que imprimir ordenadamente una lista con todos los partidos con su correspondiente cantidad de votos, ordenados de mayor a menor. 
(HINT: Usar alguna función para formatear strings, por ejemplo .format())

En el siguiente ejemplo se detallan los mensajes que deben ser mostrados al usuario. Recordar que para que el ejercicio pase las pruebas, 
se tiene que mostrar exactamente el mismo.

Ejemplo:

>> Ingrese el partido a sumarle votos: Blanco
>> Ingrese la cantidad de votos a sumarle: 2
>> Desea seguir ingresando?(s/n): s
>> Ingrese el partido a sumarle votos: Rosa
>> Ingrese la cantidad de votos a sumarle: 3
>> Desea seguir ingresando?(s/n): s
>> Ingrese el partido a sumarle votos: Rosa
>> Ingrese la cantidad de votos a sumarle: 4
>> Desea seguir ingresando?(s/n): s
>> Ingrese el partido a sumarle votos: Blanco
>> Ingrese la cantidad de votos a sumarle: 4
>> Desea seguir ingresando?(s/n): n
El partido Rosa obtuvo 7 votos.
El partido Blanco obtuvo 6 votos.
Notar que se puede asumir que se ingresa al menos un par partido-votos.
Pensar bien la modularización del programa.
'''

def ordenar_tabla(tabla:dict):
    '''
    Recibe una tabla y la ordena de manera descendente respecto a su valor.
    '''
    tabla_ordenada = sorted(tabla.items(),key=lambda c:c[1],reverse=True)
    return tabla_ordenada

def construir_tabla_votos():
    '''
    Construye una tabla de votos, con la clave siendo el partido que el usuario ingrese, y su valor la cantidad de votos
    '''
    tabla_votos = {}
    partido = input("Ingrese el partido a sumarle votos: ")
    validacion = True
    while validacion == True:
        cantidad_votos = int(input("Ingrese la cantidad de votos a sumarle: "))
        if partido not in tabla_votos:
            tabla_votos[partido] = cantidad_votos
        else:
            tabla_votos[partido] += cantidad_votos
        respuesta = input("Desea seguir ingresando?(s/n): ")
        if respuesta == "s":
            partido = input("Ingrese el partido a sumarle votos: ")
        else:
            validacion = False
    return tabla_votos


def main():
    tabla = construir_tabla_votos()
    tabla = ordenar_tabla(tabla)
    for elementos in tabla:
        print("El partido {} obtuvo {} votos.".format(elementos[0],elementos[1]))
main()
    

