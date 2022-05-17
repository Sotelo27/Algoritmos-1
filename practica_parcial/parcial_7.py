"""

Escribi una funcion que devuelva verdadero si un alumno aprobo un curso virtual, o de lo contrario falso.
La funcion recibe dos listas: una de puntajes maximos por cada actividad y otra de 
puntajes otorgados por dicha actividad.

Para aprobar el curso se necesita que en cada actividad haya obtenido, por lo menos, 
un 60% del puntaje maximo o, en su defecto, el 80% del total del puntaje.

Comproba el correcto funcionamiento, mediante los siguientes casos de prueba usando la libreria doctest. 
Además, agrega DOS casos de prueba adicionales, en donde uno sea Falso y el otro Verdadero.

"""
def alumnos_aprobados (listas_porcentajes_max,listas_puntajes):
    aprobar_cursada = True
    contador = 0
    while aprobar_cursada and contador < len(listas_porcentajes_max):
        porcentaje_para_aprobar = (listas_porcentajes_max[contador] * 60) // 100
        if porcentaje_para_aprobar <= listas_puntajes[contador] <= listas_porcentajes_max[contador]:
            contador += 1
        else:
            aprobar_cursada = False
    return aprobar_cursada

print(alumnos_aprobados([10,10,10,10,100],[6,10,8,5,60]))
print(alumnos_aprobados([10,10,10,10,100],[10,10,8,10,100]))
print(alumnos_aprobados([10,10,10,10,100],[6,6,8,8,8]))
print(alumnos_aprobados([10,10,10,10,100],[6,10,8,10,60]))
print(alumnos_aprobados([10,10,10,10,100],[5,4,5,5,50]))