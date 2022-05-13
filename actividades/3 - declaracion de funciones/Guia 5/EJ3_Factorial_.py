'''
Escribir una función que reciba un valor y calcule el factorial del mismo. Si no se
puede calcular el factorial del valor recibido, la función deberá devolver 0, de lo
contrario deberá devolver el valor calculado.
'''

def factorial(numero:int):
    factorial = 1
    if numero >= 0:
        for i in range(1,numero+1):
            factorial = i * factorial
    else:
        factorial = 0
    return factorial

def main():
    print("\nEl factorial de 6 es " + str(factorial(6)))
    print("\nEl factorial de 1 es " + str(factorial(1)))
    print("\nEl factorial de 0 es " + str(factorial(0)))
    print("\nEl factorial de 20 es " + str(factorial(20)))
    print("\nEl factorial de 5 es " + str(factorial(5)))
    print("\nEl factorial de -5 es " + str(factorial(-5)))


main()
