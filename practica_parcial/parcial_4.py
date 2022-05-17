"""
Escribir una función que reciba una cadena de caracteres y devuelva una tupla con la cantidad de letras mayúsculas y minúsculas. La primer posición en la tupla, corresponde a las letras mayúsculas; y la segunda posición, a las letras minúsculas. Debe tener en cuenta las vocales acentuadas.
NO PUEDE UTILIZAR para esta solución el método count.
Deberá comprobar el correcto funcionamiento, mediante los siguientes casos de prueba usando la librería doctest.

Para ("Hola, ¿qué tal?") debe devolver (1, 9)
Para ("HoLaChAu") debe devolver (4, 4)
Para ("") debe devolver (0, 0)
Para ("42910%(@!") debe devolver (0, 0)
Para ("429A10É%(@!") debe devolver (2, 0)
Para ("90em28ú") debe devolver (0,3)
Para ("A MÍ MI MAMÁ ME MIMA") debe devolver (15, 0)
Para ("hola q tal?!") debe devolver (0, 8)
"""
def contar_mayus_minus(cadena):
    mayusculas = 0
    minusculas = 0
    palabras_mayusculas = "ÁÉÍÓÚQWERTYUIOPASDFGHJKLÑZXCVBNM"
    palabras_minusculas = "áéíóúqwertyuiopasdfghjklñzxcvbnm"
    for caracteres in cadena:
        if caracteres in palabras_minusculas:
            minusculas += 1
        elif caracteres in palabras_mayusculas:
            mayusculas += 1
    return mayusculas,minusculas

print(contar_mayus_minus("Hola, ¿qué tal?"))
print(contar_mayus_minus("HoLaChAu"))
print(contar_mayus_minus(""))
print(contar_mayus_minus("42910%(@!"))
print(contar_mayus_minus("429A10É%(@!"))
print(contar_mayus_minus("90em28ú"))
print(contar_mayus_minus("A MÍ MI MAMÁ ME MIMA"))
print(contar_mayus_minus("hola q tal?!"))

