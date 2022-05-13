'''
El siguiente ejercicio nos pide extraer estadísticas para un campeonato de fútbol finalizado a partir de ciertos datos que 
se encuentran cargados en un diccionario importado desde un archivo secundario.

El diccionario tiene como clave el nombre del equipo de fútbol y como valor asociado una tupla de largo 5, 
que contiene información sobre el desempeño de los equipos en el campeonato. En la primera posición tiene la cantidad de partidos ganados (vale por 3 puntos); 
en la segunda posición la cantidad de partidos empatados (vale por 1 punto); en la tercera posición la cantidad de partidos perdidos (vale por 0 puntos); 
en la cuarta posición la cantidad de goles realizados; y en la quinta posición la cantidad de goles recibidos.

A partir de importar este diccionario, se pide construir un programa que calcule las siguientes estadísticas:

El equipo que salió campeón, con su respectiva cantidad de puntos.
El equipo que desciende (último), con su respectiva cantidad de puntos.
El partido que más partidos empatados tuvo, con su respectiva cantidad.
El equipo que tiene el ratio goles realizados sobre goles recibidos más alto de todos (goles realizados / goles recibidos).
La salida debe tener el siguiente formato:

El equipo campeon es Boca con 26 puntos.
El equipo que desciende es San Lorenzo con 4 puntos.
El equipo que mas partidos empato es River con 6 partidos.
El equipo con mejor proporcion goleadora es Huracan con 2.6.
Nota importante: Está claro que conociendo el diccionario pueden hacer las cuentas a mano y printear las respuestas. 
El objetivo del ejercicio es que hagan los cálculos. Nuevamente, confiamos en su honestidad y responsabilidad para aprovechar el ejercicio para practicar.
'''

def ordenar_tabla(tabla:dict):
    '''
    Recibe una tabla y la ordena de manera descendente respecto a su valor.
    '''
    tabla_ordenada = sorted(tabla.items(),key=lambda c:c[1],reverse=True)
    return tabla_ordenada

def calcular_puntos(tabla:dict):
    tabla_de_puntos = {}
    for equipos in tabla:
        tabla_de_puntos[equipos] = tabla[equipos][0]* 3 + tabla[equipos][1] 
    tabla_de_puntos = ordenar_tabla(tabla_de_puntos)
    campeon = tabla_de_puntos[0]
    equipo_deciende = tabla_de_puntos[-1]
    return campeon,equipo_deciende
    

def calcular_goleador(tabla:dict):
    tabla_goles = {}
    for equipos in tabla:
        tabla_goles[equipos] = tabla[equipos][3] / (tabla[equipos][4])
    tabla_goles = ordenar_tabla(tabla_goles)
    print(tabla_goles)
    goleador = tabla_goles[0]
    return goleador

def main(campeonato:dict):
    mejor_y_peor_equipo = calcular_puntos(campeonato)
    goleador = calcular_goleador(campeonato)
    tabla_empates = sorted(campeonato.items(),key=lambda c:c[1][1],reverse=True)
    print("El equipo campeon es {} con {} puntos.".format(mejor_y_peor_equipo[0][0],mejor_y_peor_equipo[0][1]))  
    print("El equipo que desciende es {} con {} puntos.".format(mejor_y_peor_equipo[1][0],mejor_y_peor_equipo[1][1]))
    print("El equipo que mas partidos empato es {} con {} partidos.".format(tabla_empates[0][0],tabla_empates[0][1][1]))
    print("El equipo con mejor proporcion goleadora es {} con {:.3f}.".format(goleador[0],goleador[1]))  


primera_division = {
    "Boca": (2, 3, 4, 10, 10),
    "River": (3, 4, 2, 12, 16),
    "Central": (7, 1, 1, 23, 21),
    "Racing": (5, 2, 2, 15, 8),
    "Independiente": (4, 3, 2, 7, 8),
    "San Lorenzo": (1, 8, 0, 5, 9),
    "Godoy Cruz": (3, 3, 1, 3, 3),
    "Estudiantes": (1, 1, 7, 9, 9),
    "Huracan": (3, 2, 4, 4, 6),
    "Gimnasia LP": (0, 2, 7, 1, 26)
}
main(primera_division)