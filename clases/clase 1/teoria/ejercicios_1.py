print("\n----Ejercicio 1----\n")
'''
Abrí la consola de Python y crea la variable lado_1 con un valor inicial de 10,
y la variable lado_2, con un valor inicial de 5. Las mismas, representan los
lados de un rectángulo.
Ahora, crea las variables superficie y perímetro, asignándole a cada una la
operación que corresponda, utilizando las variables lado_1 y lado_2 creadas,
junto con los operadores aritméticos adecuados.
'''
lado_1 = 10
lado_2 = 5
superficie = lado_1 * lado_2
perimetro = lado_2 * 2 + lado_1 * 2 

print("La superficie es ",superficie,"y el perimetro es",perimetro)

print("\n----Ejercicio 2----\n")
'''
Como en el caso anterior, utiliza la consola y crea la variable kilómetros con
un valor inicial de 455.
Sabiendo que 1 km. equivale a 0,6214 millas; crea la variable millas, y
asígnale como valor inicial, el valor equivalente a 455 km, pero utilizando la
variable kilómetros creada y el valor de 0,6214 millas por km.
Observa que en Python, como separador de la parte decimal, tienes que usar
el "." y no la ",".
'''
kilometros = 455
millas = kilometros * 0.6214 
print("\n455 KILOMETROS equivalen a ", millas , " MILLAS ")

print("\n----Ejercicio 3----\n")
'''
Por último, procede de modo similar al caso anterior, teniendo en cuenta que
32 grados Fahrenheit, equivalen a 0 grados Celsius
'''
celsius = 455
farenheit = ( celsius * 9/5 ) + 32
print("\nLOS GRADOS ",celsius,"celsius equivalen a ",farenheit,"grados farenheit")
print("\n----Ejercicio 4----\n")

'''
Ahora crea la variable apellido, y asígnale tu apellido; y crea la variable
nombre, y asígnale tu nombre.
Crea nuevas variables y asígnales las variables creadas, de modo tal que
formen una nueva variable con:
1) Tu nombre y apellido. Ejemplo: "Juan Perez"
2) Tu apellido, seguido por tu nombre, separado por una coma.
Ejemplo: "Perez, Juan"
3) La cadena "Hola, yo soy: " seguida de tu nombre y apellido.
Ejemplo: "Hola, yo soy: Juan Perez"
'''

apellido = "Sotelo"
nombre = "Martin"
nombre_completo = nombre +" " + apellido
print(nombre_completo)
nombre_compl_inv = apellido + ", " + nombre 
print(nombre_compl_inv)
print ("Hola, yo soy: " + nombre_completo)
