'''
El siguiente ejercicio es un poco más largo que el resto del módulo y está tomado de un parcial tomado en el año 2018.

Se pide construir un programa que nos permita obtener estadísticas del mercado laboral por localidad con el fin de poder realizar comparaciones.

Para comenzar, se deben comenzar cargando en un diccionario pares de datos localidad-personas, donde el valor de las personas hace 
referencia a la cantidad de personas que se encuentra en edad de trabajar.
Debe tenerse en cuenta que, como los datos se obtienen de distintas planillas, es posible que se ingrese más de un par clave-valor asociada a una localidad.

Una vez que el usuario terminar de realizar la carga, se deben imprimir:

a) El total de personas en edad laboral y el total de empleados para cada localidad.

b) Un listado ordenado de mayor a menor por porcentaje de desocupación. Debe tenerse en cuenta que para determinar el porcentaje 
de desocupación se puede utilizar la fórmula:

% desocupacion = (1 - empleados / personas en edad de trabajar) * 100

En el siguiente ejemplo se detallan los mensajes que deben ser mostrados al usuario. Recordar que para que el ejercicio pase las pruebas,
 se tiene que mostrar exactamente el mismo.

Ejemplo:

>> Ingrese localidad: CABA
>> Ingrese la cantidad de personas que pueden trabajar: 10
>> Ingrese la cantidad de empleados: 9
>> Desea seguir ingresando?(s/n): s
>> Ingrese localidad: Lanus
>> Ingrese la cantidad de personas que pueden trabajar: 10
>> Ingrese la cantidad de empleados: 7
>> Desea seguir ingresando?(s/n): s
>> Ingrese localidad: CABA
>> Ingrese la cantidad de personas que pueden trabajar: 10
>> Ingrese la cantidad de empleados: 6
>> Desea seguir ingresando?(s/n): s
>> Ingrese localidad: Lanus
>> Ingrese la cantidad de personas que pueden trabajar: 10
>> Ingrese la cantidad de empleados: 6
>> Desea seguir ingresando?(s/n): s
>> Ingrese localidad: Chascomus
>> Ingrese la cantidad de personas que pueden trabajar: 10
>> Ingrese la cantidad de empleados: 6
>> Desea seguir ingresando?(s/n): n
En la localidad de CABA hay 20 personas en edad laboral y 17 trabajando.
En la localidad de Lanus hay 20 personas en edad laboral y 15 trabajando.
En la localidad de Chascomus hay 10 personas en edad laboral y 6 trabajando.
La tasa de desocupacion en Chascomus es 40.0%.
La tasa de desocupacion en Lanus es 35.0%.
La tasa de desocupacion en CABA es 25.0%.
'''