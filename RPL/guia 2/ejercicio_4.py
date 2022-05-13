'''
Completar el cuerpo de la función. La misma recibe un número como parámetro 
y debe devolver el valor absoluto del mismo.

Ejemplos:

valor_absoluto(3) => 3
valor_absoluto(-3) => 3
'''
def valor_absoluto(numero):
    valor_absoluto = numero
    if numero < 0 :
        valor_absoluto *= -1
    return valor_absoluto