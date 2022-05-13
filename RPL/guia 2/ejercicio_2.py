'''
Completar el cuerpo de la función. La misma debe devolver 
True en caso de que el número que se recibe como parámetro sea primo, y False en caso contrario.

Ejemplos:

es_primo(3) => True
es_primo(4) => False
es_primo(11) => True
es_primo(15) => False
'''
def es_primo(numero):
    verificacion = False
    contador = 2
    divisores = 1
    while contador <= numero and divisores < 3 :
        if numero % contador == 0:
            divisores += 1
        contador += 1
    if divisores == 2 :
        verificacion = True
    return verificacion
