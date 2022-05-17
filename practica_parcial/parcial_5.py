"""Escribi una funcion que devuelva verdadero si elegis una pelicula que te proponen, o de lo contrario falso.
La funcion recibe dos listas: una de actores/actrices que actuan en esa pelicula y otra de puntajes.
La lista actores/actrices puede tener desde 1 a n actores/actrices.
La lista puntajes puede tener desde 1 a m puntajes (del 1 al 10).

Se elige la pelicula cuando:

- En la lista actores/actrices están "Leonardo Di Caprio" o "Emma Stone" o "Jazmin Stuart" 
Y
- en la lista de puntajes, hay mayor cantidad de notas mayores o iguales a 6 que las que son menores a 6

Comproba el correcto funcionamiento, mediante los siguientes casos de prueba usando la librería doctest.
Ademas, agrega DOS casos de prueba adicionales,en donde uno sea Falso y el otro Verdadero."""

def pelicula_elegida(lista_actores,lista_puntajes):
    validar_pelicula = False
    validar_actores = False
    cantidad_notas_mayores = 0
    cantidad_notas_menos = 0
    contador = 0
    while validar_actores == False and contador < len(lista_actores) :
        if lista_actores[contador] == "Leonardo Di Caprio" or lista_actores[contador] == "Emma Stone" or lista_actores[contador] == "Jazmin Stuart":
            validar_actores = True
        else:
            contador += 1
    for notas in lista_puntajes:
        if notas >= 6:
            cantidad_notas_mayores += 1
        else:
            cantidad_notas_menos += 1
    if validar_actores == True and cantidad_notas_mayores > cantidad_notas_menos:
        validar_pelicula = True
    return validar_pelicula
lista_actores = ["Leonardo Di Caprio","Josecito","Pepito"]
lista_actores_1 = ["Emma Stone" , "Leonardo Di Caprio" , "Rambo"]
lista_actores_2 = ["PEPE","Rambo","Yondu"]
lista = [1,2,3,4,1,2,4,6,6,6,6,6,6,6,6,6]
lista_2 = [2,3,3,3,3,2,2,3,2,2,1]
lista_3 = [5,6,6,10]
print(pelicula_elegida(lista_actores,lista))
print(pelicula_elegida(lista_actores_1,lista_2))
print(pelicula_elegida(lista_actores_2,lista_3))