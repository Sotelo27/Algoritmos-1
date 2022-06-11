"""
Solicitar al usuario el ingreso de un texto a continuacion: 
mostrar el teto ordenado por palabra y todo en mayusculas
informar cuantos caracteres tiene la palabra mas larga
generar una lista sin palabras repetidas
armar un ranking de palabras informando palabra y cantidad de ocurrencias ordenado
por la cantidad de ocurrencias
"""

from cgitb import text


def registrar_palabras(palabra,diccionario):
    if palabra not in diccionario.keys():
        diccionario[palabra] = 1
    else:
        diccionario[palabra] += 1

def ordenar_texto(texto):
    lista = texto.split()
    texto_mayus = texto.upper()
    lista_mayus = texto_mayus.split()
    lista_sin_repetidos = []
    registro_palabras = {}
    palabra_larga = ""
    for palabra in lista:
        if len(palabra) > len(palabra_larga):
            palabra_larga = palabra
        if palabra not in lista_sin_repetidos:
            lista_sin_repetidos.append(palabra)
        registrar_palabras(palabra,registro_palabras)
    longitud_palabra_larga = len(palabra_larga)
    lista_mayus = sorted(lista_mayus)
    for elementos in lista_mayus:
        print(elementos)
    print("La palabra mas larga es {} y su longitud es de {} ".format(palabra_larga,longitud_palabra_larga))
    print(registro_palabras)

ordenar_texto("Hola como arbol esdrujula como")
