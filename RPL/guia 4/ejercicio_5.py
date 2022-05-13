'''
La idea de esta sección es completar las distintas funciones de acuerdo a los 
requerimientos especificados para cada una de ellas, tal como se hizo para el resto del módulo de listas.
'''
    
from calendar import c


def es_primo(numero:int,menor_numero:int):
    '''
    Recibe un valor numero y otro valor numerico ingresado por el usuario.La funcion comprueba si el numero es primo y si dicho numero es mayor
    que 2do numero ingresado por el usuario.
    '''
    verificacion = False
    contador = 2
    divisores = 1
    while contador <= numero and divisores <= 2 and numero > menor_numero:
        if numero % contador == 0:
            divisores += 1
        contador += 1
    if divisores == 2:
        verificacion = True
    return verificacion

def filtrar_primos(numeros:list, menor_numero:int):
    '''
    Recibe una lista de números enteros y un número adicional. Retorna una nueva lista filtrada, 
    que contiene aquellos números que sean primos y además sean mayores al segundo número que se recibió 
    como parámetro.

    HINT: Pueden utilizar la función es_primo(), correspondiente al módulo de funciones.

    Ejemplos:

        filtrar_primos([3, 7, 11, 13], 8) => [11, 13]
        filtrar_primos([11, 7, 3, 19], 15) => [19]
    '''
    lista_filtrada = []
    for numero in numeros:
        validacion = es_primo(numero,menor_numero)
        if validacion == True:
            lista_filtrada.append(numero)
    return lista_filtrada

def ordenar_por_longitud_de_tuplas(tuplas:list):
    '''
    Recibe una lista de tuplas. Retorna una nueva lista ordenada de mayor a menor por la longitud de las mismas. 
    Aclaración: No importa el tipo de los elementos que se encuentran contenidos en las tuplas.

    Ejemplo:

    lista_tuplas = [(1,5,6), (1,2), (1,), (6,4,5,6), ("asd", 9, 5.6, "l", "s")]
    ordenar_por_longitud_de_tuplas(lista_tuplas) => [("asd", 9, 5.6, "l", "s"), (6,4,5,6), (1,5,6), (1,2), (1,)]
    '''
    lista_nueva = sorted(tuplas,key= len ,reverse=True)
    return lista_nueva

def concatenar_primeros_elementos(lista):
    '''
    Recibe una lista de lista de listas. Se puede asumir que cada una de las listas internas tiene una longitud mayor a 3. 
    Retorna una única lista, que resulta de la concatenación de los primeros 2 elementos de cada una de las listas internas, 
    en el orden original.

    Ejemplo:

        lista = [[1,4,5,6], [2,3,4,5], [6,4,4,6,7,8], [5,6,7,3,5,6,4]]
        concatenar_primeros_elementos(lista) => [1,4,2,3,6,4,5,6]
    '''
    lista_nueva = [n for x in lista for n in x[0:2] ]
    return lista_nueva

print(filtrar_primos([3, 7, 11, 13], 8))
print(filtrar_primos([11, 7, 3, 19], 19))
print(filtrar_primos([11, 7, 3, 19], 15))
lista_tuplas = [(1,5,6), (1,2), (1,), (6,4,5,6), ("asd", 9, 5.6, "l", "s")]
print(ordenar_por_longitud_de_tuplas(lista_tuplas))
lista = [[1,4,5,6], [2,3,4,5], [6,4,4,6,7,8], [5,6,7,3,5,6,4]]
print(concatenar_primeros_elementos(lista))
print()
print()
print()