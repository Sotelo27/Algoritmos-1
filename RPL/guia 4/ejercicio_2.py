'''
Los distintos ejercicios propuestos en este apartado fueron pensados para ser resueltos utilizando listas por compresión. 
Correr un test para probar una función solamente implica testear el resultado; esto significa que un test puede pasar sin que 
los ejercicios sean resueltos utilizando listas por comprensión y realizando simples iteraciones sobre las listas. 
Esta claro que no deben hacer esto último, recuerden que los docentes pueden ver el código que envían. 
Confiamos en su honestidad y responsabilidad.
'''
def numeros_positivos(numero):
    '''

    Recibe un entero positivo. Retorna una lista que contiene todos los números positivos hasta llegar al número que recibió como parámetro.

    Ejemplo:
    numeros_positivos(5) => [1,2,3,4,5]

    '''
    lista_nueva = [n for n in range(1 , numero + 1)]
    return lista_nueva
    
def numeros_positivos_pares(numero):
    '''
    Recibe un entero positivo. Retorna una lista que contiene todos los números positivos pares hasta llegar al número que recibió como parámetro.

    Ejemplo:
    numeros_positivos_pares(7) => [2,4,6]
    '''
    lista_nueva = [n for n in range (1, numero + 1) if n % 2 == 0 ]
    return lista_nueva
    
def numeros_positivos_pares_cuadrado(numero):
    '''
    Recibe un entero positivo. Retorna una lista que contiene todos los números positivos PARES elevados al cuadrado hasta llegar 
    al número que recibió como parámetro.

    Ejemplo:

    numeros_positivos_pares(7) => [4,16,36]
    '''
    lista_nueva = [n**2 for n in range(1,numero + 1) if n % 2 == 0 ]
    return lista_nueva

def impares_al_cuadrado(lista):
    '''
    Recibe una lista de enteros positivos. Retorna una nueva lista donde los números impares están elevados al cuadrado,
    mientras que los pares se conservan sin sufrir ninguna modificación.

    Ejemplo:
    impares_al_cuadrado([1,2,3,4,5,6,7]) => [1,2,9,4,25,6,49]

    '''
    lista_nueva = [n**2 if n % 2 != 0 else n for n in lista ]
    return lista_nueva

def filtrar_tuplas_por_suma(lista_de_tuplas):
    '''
    Recibe una lista de tuplas de longitud 2 que contiene un número entero en cada índice. 
    Retorna una nueva lista que contiene únicamente a aquellas tuplas que, al sumar sus dos elementos, el resultado sea positivo (mayor o igual a 0). 
    Se debe conservar el orden original.

    Ejemplo:
    filtrar_tuplas_por_suma([(7, -5), (4, -5), (1, 2), (1, -2)]) => [(7, -5),(1, 2)]
    '''
    lista_nueva = [n for n in lista_de_tuplas if n[0] + n[1] >= 0 ]
    return lista_nueva
    
def filtrar_tupla_elemento_par(lista_de_tuplas):
    '''
    Recibe una lista de tuplas de longitud 2 que contiene un número entero en cada índice. Retorna una nueva lista que contiene ínicamente 
    aquellas tuplas que contengan al menos un numero par, conservando el orden original.

    Ejemplo:
    filtrar_tupla_elemento_par([(7, -5), (4, 5), (1, 2), (1, -3), (4, 2)]) => [(4, 5),(1, 2), (4,2)]

    '''
    lista_nueva = [n for n in lista_de_tuplas if n[0] % 2 == 0 or n[1] % 2 == 0]
    return lista_nueva

print(numeros_positivos(5))
print(numeros_positivos_pares(7))
print(numeros_positivos_pares_cuadrado(7))
print(impares_al_cuadrado([1,2,3,4,5,6,7]))
print(filtrar_tuplas_por_suma([(7, -5), (4, -5), (1, 2), (1, -2)]))
print(filtrar_tupla_elemento_par([(7, -5), (4, 5), (1, 2), (1, -3), (4, 2)]))
print()
print()
