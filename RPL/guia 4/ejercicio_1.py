
def filtrar_pares(lista):
    '''

    Recibe una lista con variables numéricas enteras. 
    Retorna una nueva lista con todos los números pares que estaban en la lista que se recibió como parámetro. 
    Los elementos de la lista devuelta deben estar en el orden original.

    Ejemplo:
    filtrar_pares([5,6,13,7,11,9,10,11]) => [6,10]

    '''
    lista_nueva = []
    for numero in lista:
        if numero % 2 == 0 :
            lista_nueva.append(numero)
    return lista_nueva

def es_primo(numero):
    verificacion = False
    contador = 2
    divisores = 1
    while contador <= numero and divisores <= 2:
        if numero % contador == 0:
            divisores += 1
        contador += 1
    if divisores == 2:
        verificacion = True
    return verificacion

def filtrar_primos(lista):
    '''

    Recibe una lista con variables numéricas enteras. 
    Retorna una nueva lista con todos los números primos que estaban en la lista que se recibió como parámetro
    Los elementos de la lista devuelta deben estar en el orden original.

    Hint: Utilizar la función programada en otra actividad que determina si un número es primo o no.

    Ejemplo:
    filtrar_primos([5,6,13,7,11,9,10,11]) => [5,13,7,11,11]

    '''
    lista_nueva = []
    for numero in lista:
        validacion = es_primo(numero)
        if validacion == True:
            lista_nueva.append(numero)
    return lista_nueva


def sumar_elementos(lista):
    '''

    Recibe una lista con variables numéricas. Retorna la suma de todos sus elementos.
    No se puede utilizar la función sum(), ya existente en Python.

    Ejemplo:
    sumar_elementos([5,6,13,7,11,9,10,11]) => 72

    '''
    suma = 0
    for numero in lista:
        suma += numero
    return suma


def esta_ordenada(lista):
    '''
    Recibe una lista con variables numericas. 
    Retorna True en caso de que la lista este ordenada ascendentemente (es decir, los mas chicos en las primeras posiciones), 
    False en caso contrario.

    Ejemplos:
    esta_ordenada([5,6,13,7,11,9,10,11]) => False
    esta_ordenada([5,6,7,11]) => True

    '''
    validacion = True
    auxiliar = 0
    contador = 0
    while validacion and contador < len(lista):
        for numero in lista:
            if numero < auxiliar:
                validacion = False
            auxiliar = numero
            contador += 1
    return validacion
    

def producto_escalar(vector_1, vector_2):
    '''

    Recibe dos listas de variables numéricas con la misma longitud. Interpretarlas como vectores. 
    Retorna el producto escalar entre ambos vectores.

    Ejemplos:
    producto_escalar([2,5,3], [4,6,7]) => 59

    '''
    multiplicacion = 0
    for i in range(len(vector_1)):
        multiplicacion += vector_1[i] * vector_2[i]
    return multiplicacion
    

def letras_en_palabra(letras, frase):
    '''

    Recibe una lista de letras y una cadena. 
    La lista contiene en cada índice de la misma una letra (string de longitud 1). 
    Retorna True en caso de que todas las letras se encuentren en la palabra, False en caso contrario.

    Ejemplos:
    letras_en_palabras(["a","h","e"], "hola como estas") => True
    letras_en_palabras(["a","h","e"], "ola como estas") => False 

    '''
    validacion = True
    contador = 0
    while validacion and contador < len(letras):
        if letras[contador] not in frase:
            validacion = False
        contador += 1
    return validacion


print(filtrar_pares([5,6,13,7,11,9,10,11]))
print(filtrar_primos([5,6,13,7,11,9,10,11]))
print(sumar_elementos([5,6,13,7,11,9,10,11]))
print(esta_ordenada([5,6,13,7,11,9,10,11]))
print(esta_ordenada([5,6,7,11]))
print(producto_escalar([2,5,3], [4,6,7]))
print(letras_en_palabra(["a","h","e"], "hola como estas"))
print(letras_en_palabra(["a","h","e"], "ola como estas"))