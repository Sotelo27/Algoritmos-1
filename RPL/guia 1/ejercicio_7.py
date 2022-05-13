'''
Escribir un programa que solicite el ingreso de un valor correspondiente a una base 
y un valor correspondiente a una potencia e imprima por pantalla el 
resultado de elevar la base ingresada a la potencia ingresada.
El cálculo de la potencia debe ser realizado a través de la realización 
de multiplicaciones sucesivas. No se puede utilizar el operador "**".

    >>> Ingrese la base: 2
    >>> Ingrese la potencia: 4
    16
'''
base = int(input("Ingrese la base: "))
potencia = int(input("Ingrese la potencia: "))
resultado = 1

for i in range(0,potencia):
    resultado *= base
print(resultado)

