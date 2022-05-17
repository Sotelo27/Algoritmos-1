'''

Los ejercicios de esta sección tienen como objetivo empezar a jugar con
diccionarios resolviendo una serie de problemas que implican completar funciones a partir de ciertos requerimientos.

'''
def numeros_al_cuadrado(numero):
    '''

    Recibe un numero entero positivo. Retorna un diccionario cuya claves comprenden 
    el rango de números positivos tomando como límite superior el número que se recibió como parámetro,
    y donde para cada clave su valor asociado será el número de la clave al cuadrado.

    Ejemplo:
    numeros_al_cuadrado(4) => {1: 1, 2: 4, 3: 9, 4: 16}

    '''
    diccionario = {}
    for numeros in range(1,numero + 1):
        if numeros not in diccionario:
            diccionario[numeros] = numeros**2
    return diccionario

def mezclar_diccionarios(dicc_uno, dicc_dos):
    '''
    Recibe dos diccionarios. Retorna un único diccionario, que resultad de realizar la mezcla entre los dos. 
    Las claves del nuevo diccionario deben ser las claves de ambos (asumir que no tienen claves iguales), con sus respectivos valores.

    Ejemplo:
        dicc_1 = {'clave1': 1, 'clave3': 3}
        dicc_2 = {'clave2': 2, 'clave4': valor4}

        mezclar_diccionarios(dicc_1, dicc_2) => 

            {'clave1': 1, 'clave3': 3, 'clave2': 2, 'clave4': 4}
    Aclaración: El orden de los pares asociados clave-valor puede ser cualquiera.
    '''
    diccionario_mezclado = {}
    for llaves in dicc_1.keys(),dicc_2.keys():
        for claves in llaves:
            if claves not in diccionario_mezclado:
                if claves in dicc_1.keys():
                    diccionario_mezclado[claves] = dicc_1[claves] 
                else:
                    diccionario_mezclado[claves] = dicc_2[claves]
    return diccionario_mezclado
    
    
def filtrar_por_sumar_diez(diccionario):
    '''
    Recibe un diccionario cuyas claves son enteros, y también su valor asociado. 
    Retorna un diccionario que contiene únicamente los pares clave-valor del 
    diccionario que se recibió por parámetro que al sumarlos sean mayores o iguales a 10.

    Ejemplo:

    filtrar_por_sumar_diez({8: 11, 3: 6, 9: 2, 1: 4}) => {8: 11, 9: 2}
   '''
    dic_suma_pares = {}
    for claves in diccionario:
        if diccionario[claves] + claves >= 10:
            dic_suma_pares[claves] = diccionario[claves]
    return dic_suma_pares
 
def ordenar_valores_por_longitud(diccionario):
    '''
    Recibe un diccionario con claves de tipo string y valores asociados de tipo string. Retorna una lista ordenada que contiene únicamente los valores del diccionario. Esta lista debe estar ordenada descendentemente (mayor a menor) según la longitud que tienen las cadenas de caracteres que son valor.

    Ejemplo:

    dicc = {'boca':'river', 'pablo':'guarna', 'hola':'algoritmos'}
    ordenar_valores_por_longitud(dicc) => ['algoritmos','guarna','river']
    '''
    lista = sorted(diccionario.values(),key= len,reverse=True)
    return lista   

#print(numeros_al_cuadrado(4))
dicc_1 = {'jose':1,'ramon':3}
dicc_2 = {'maria':2,'almendra':4}
print()
print(mezclar_diccionarios(dicc_1, dicc_2))
print()
print(filtrar_por_sumar_diez({8: 11, 3: 6, 9: 2, 1: 4}))
dicc = {'boca':'river', 'pablo':'guarna', 'hola':'algoritmos'}
print()
print(ordenar_valores_por_longitud(dicc))