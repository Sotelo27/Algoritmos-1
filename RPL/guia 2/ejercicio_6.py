'''
Completar el cuerpo de la función. La misma recibe un número y 
debe devolver la suma de todos los divisores de este número. 
No deben considerarse el número en cuestión ni el número uno.

Por ejemplo, para el número 8, sus divisores son 4 y 2, por lo tanto la función debe devolver 6.

Ejemplos:

suma_de_divisores(8) => 6
suma_de_divisores(7) => 0
suma_de_divisores(10) => 7
suma_de_divisores(31) => 0
suma_de_divisores(32) => 30
'''
def suma_de_divisores(numero):
    suma_total = 0
    for i in range(2,numero - 1):
        if numero % i == 0:
            suma_total += i
    return suma_total

print(suma_de_divisores(31))
