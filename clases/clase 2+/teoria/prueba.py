'''
Solicitar el ingreso de un mes y un año e 
informar la cantidad de días del mes, considerando los años bisiestos.
Tenga en cuenta que un año bisiesto es aquel dividible por 4, 
salvo que sea divisible por 100, en cuyo caso también debe ser divisible por 400.
'''

print("Algoritmo Calendario")
print("A continuacion se ingrese anio y mes , del cual se mostrara los dias de dicho mes.")
anio = int(input('Ingrese el anio: '))
Esbiciesto = 2
if (anio % 4 == 0 and anio % 100 !=0) or (anio % 4 == 0 and anio % 400 == 0):
    Esbiciesto = 1
mes = int(input('Ingrese el numero del Mes: '))
while mes <= 0 or mes >12 :
    print('valor ingresado incorrecto,reingrese correctamente')
    mes = int(input('Ingrese el mes: '))
if Esbiciesto == 1 and mes == 2:
    print("El mes elegido tiene un total de 29 dias")
elif Esbiciesto ==2 and mes ==2:
    print("El mes elegido tiene un total de 28 dias")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("El mes elegido tiene un total de 30 dias")
else:
    print("El mes tiene un total de 31 dias") 