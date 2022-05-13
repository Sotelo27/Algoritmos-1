'''
Escribir un programa que solicite el ingreso de un número y que luego calcule e imprima su factorial.

    >>> Ingrese un numero: 5
    120
'''
numero = int(input("Ingrese un numero: "))
factorial = 1
for i in range (1,numero + 1):
    factorial *= i
print(factorial)