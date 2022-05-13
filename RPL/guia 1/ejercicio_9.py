'''
Escribir un programa que solicite a un usuario el ingreso de notas en forma sucesiva 
y que imprima el promedio de las mismas. Se debe considerar que el usuario ha finalizado 
la carga cuando ingresa la nota "0". Por otro lado, se puede asumir que todos los datos ingresados 
son correctos (la entrada es convertible a un valor entero que va entre 0 y 10).

Ejemplo:

>> Ingrese nota o 0 para terminar: 10
>> Ingrese nota o 0 para terminar: 7
>> Ingrese nota o 0 para terminar: 4
>> Ingrese nota o 0 para terminar: 0
El promedio es: 7.0
'''
nota = int(input("Ingrese nota o 0 para terminar: "))
sumatoria_notas = nota
contador = 0
while nota != 0:
    nota = int(input("Ingrese nota o 0 para terminar: "))
    contador += 1
    sumatoria_notas += nota
promedio = sumatoria_notas / contador
print("El promedio es: "+ str(promedio))
