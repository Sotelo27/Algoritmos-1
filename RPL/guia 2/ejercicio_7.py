'''
Completar el cuerpo de la función. La misma recibe como parámetro un
número que será tomado como límite superior del cálculo que debemos realizar.
La función debe retornar la suma de todos los números positivos primos 
existentes entre el 0 y el número ingresado inclusive.
Recordar que el 1 no se considera primo y el 2 por definición sí lo es. 
Se puede asumir que el parámetro de entrada ha sido verificado previamente y siempre es mayor que 0.

Ejemplos:

suma_de_numeros_primos(1) => 0
suma_de_numeros_primos(2) => 2
suma_de_numeros_primos(3) => 5
suma_de_numeros_primos(4) => 5
suma_de_numeros_primos(5) => 10
suma_de_numeros_primos(17) => 2 + 3 + 5 + 7 + 11 + 13 + 17 = 58
Hint: Pueden utilizar la función es_primo(numero) definida en la segunda actividad de la categoría, logrando un mayor grado de modularización.
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

def suma_de_numeros_primos(numero):
    suma_total = 0
    for i in range(0 , numero + 1):
        verificar_primo = es_primo(i)
        if verificar_primo == True:
            suma_total += i
    return suma_total

print(suma_de_numeros_primos(3))