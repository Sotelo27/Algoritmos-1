#Para este apartado, se propone la utilización de la funcionalidad de slices de indexación aplicada a listas

def ultimos_tres_elementos(lista):
    '''

    Recibe una lista previamente inicializada, de longitud mayor o igual a 3. 
    Retorna una lista con los últimos tres elementos de la que se recibi.

    Ejemplo:

    ultimos_tres_elementos([5,3,6,2,5,32,6,4,7]) => [6,4,7]

    '''
    lista_nueva = lista[-3:]
    return lista_nueva
    
def ultimos_tres_elementos_concatenados(lista):
    '''
    Recibe una lista de listas. 
    Retorna una única lista que tiene concatenados los últimos tres elementos de cada una de las listas individuales en el orden original.

    Ejemplo:

    ultimos_tres_elementos_concatenados([[1,2,3,4], [5,6,7,8], [9,10,11,12]]) => [2,3,4, 6,7,8,10,11,12]
    '''
    lista_nueva = [numeros for listas in lista for numeros in listas[-3:] ]
    return lista_nueva
    
def indices_pares(lista):
    '''
    Recibe una lista previamente inicializada. Retorna una lista que tiene únicamente los elementos correspondientes a 
    los índices pares de la lista que recibió como parámetro.

    Hint: Recordar que los índices comienzan en 0.

    Ejemplo:
    indices_pares(["a","b","c","d","e"]) -> ["a","c","e"]
    '''
    lista_pares = lista[::2]
    return lista_pares

    
def indices_impares(lista):
    '''
    Recibe una lista previamente inicializada. 
    Retorna una lista que tiene únicamente los elementos correspondientes a los índices impares de la lista que recibió como parámetro.

    Ejemplo:

    indices_impares(["a","b","c","d","e", "f"]) -> ["b","d","f"]
    '''
    lista_impares = lista[1::2]
    return lista_impares

def invertir(lista):
    '''
    Recibe una lista previamente inicializada. Retorna dicha lista invertida.

    Ejemplo:

    invertir([1,2,3,4,5]) => [5,4,3,2,1]
    '''
    lista_invertida = lista[::-1]
    return lista_invertida

print(ultimos_tres_elementos([5,3,6,2,5,32,6,4,7]))
print(ultimos_tres_elementos_concatenados([[1,2,3,4], [5,6,7,8], [9,10,11,12]]))
print(indices_pares(["a","b","c","d","e"]))
print(indices_impares(["a","b","c","d","e", "f"]))
print(invertir([1,2,3,4,5]))
print()
print()
print()