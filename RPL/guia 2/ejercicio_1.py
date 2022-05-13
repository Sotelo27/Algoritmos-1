'''
Completar el cuerpo de la función. La misma debe 
devolver True en caso en el que el número recibido como parámetro recibido sea par, y
 False en caso contrario.

Ejemplos:

es_par(2) => True
es_par(3) => False
es_par(32) => True
es_par(33) => False
'''
def es_par(numero):
    verificar = False
    if numero % 2 == 0:
        verificar = True
    return verificar
es_par(2)
es_par(3)
es_par(32)
es_par(33)