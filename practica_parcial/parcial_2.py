'''
Escribi una función que reciba 3 listas con mediciones diarias de
valores para distintas personas. 
La primer lista es de temperaturas corporales, la segunda lista es de 
presencia de tos seca, y la tercera es del nivel de cansancio (medido del 1 al 10).

La función tiene que devolver una lista con los índices (posiciones), 
de quienes son sospechosos de COVID-19, cuando la temperatura sea mayor o igual a 37 grados, 
haya presencia de tos y el nivel de cansancio sea mayor a 6.

Por ejemplo, si ejecutaramos la función con los siguientes casos, obtendrías:


Casos de Prueba:

    >>> prueba_covid19([35.6, 36.4, 35.2, 37.1],[True, False, True, True],[7, 2, 6, 8])
    [3]
    >>> prueba_covid19([38],[False],[9])
    []
    >>> prueba_covid19([40.2, 35.7, 38.4, 37.0],[True, False, True, True],[10, 2, 7, 8])
    [0, 2, 3]
'''
import doctest
def prueba_covid19(lista_fiebre,lista_tos,lista_cansancio):
    pacientes_sospechosos = []
    for posicion in range(len(lista_fiebre)):
        if lista_fiebre[posicion] >= 37 and lista_tos[posicion] == True and lista_cansancio[posicion] > 6:
            pacientes_sospechosos.append(posicion)
    return pacientes_sospechosos
print(doctest.testmod())