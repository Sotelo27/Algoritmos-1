print("\n-----Ejercicio 1------\n")
'''
Escribir un programa que solicite el ingreso de un número y luego
calcule e informe el factorial del número ingresado.
'''
print("A continuacion se calculara el factorial del numero que desea ingresar :")
numero = -1
factorial = 1
while numero < 1 :
    numero = int(input("Ingrese un numero a continuacion: "))
    if numero < 1 :
        print("A ingresado un numero menor a uno, ingrese un numero desde 1 a mayor.")

while numero !=0:
    factorial *= numero 
    numero -= 1

print(factorial)

print("\n-----Ejercicio 2------\n")
'''
Escribir un programa que solicite el ingreso de valores numéricos.
El ingreso finalizará cuando el usuario haya ingresado como último
valor, un cero.
Informar el total de los valores acumulados y cuantos valores fueron
ingresados.

'''
print("\nA continuacion ingrese una serie de numero y se calculara el total de los numeros acumulados y cuantos de los mismos\n")
print("\nPara terminar la secuencia inicie 0 \n")
contador = 0 
numero = 1
total = 0
while numero > 0 :
    numero = int(input("Ingrese un numero a continuacion: "))
    if numero > 0 :
        contador += 1
        total += numero
print("El total de los valores ingresados es ",total,"y la cantidad ingresada de valores es ", contador)
print("\n-----Ejercicio 3------\n")
print("\n-----Ejercicio 4------\n")
'''
Mostrar en forma descendente, los número pares entre 100 y 0
inclusive.
'''
numero = 100
while numero != -1:
    if numero % 2 == 0 :
        print(numero)
    numero -= 1
print("\n-----Ejercicio 5------\n")