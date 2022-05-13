'''
Se pide que ingresen por teclado pares de Equipo-Puntos ganados, el mismo par se puede ingresar varias veces. 
Se pide generar una Tabla de Puntos Acumulados para cada equipo, ordenando la tabla por puntos en forma decreciente
'''

from operator import truediv


def tabla_de_puntos():
    tabla = {}
    parar = True
    while parar:
        equipo = input("\nIngrese a continuacion el equipo: ")
        puntos = int(input("\nIngrese a continuacion los puntos ganados por el equipo: "))
        if equipo in tabla.keys():
            tabla[equipo] += puntos
        else:
            tabla[equipo] = puntos
        seguir = input("Ingrese a continuacion 1 si quiere seguir ingresando equipos y sus puntos, caso contrario se cortara el ingreso: ")
        if seguir != "1":
            parar = False
    tabla_ordenada = sorted(tabla.items(), key=lambda x: x[1],reverse=True)
    print(tabla_ordenada)

    
tabla_de_puntos()

