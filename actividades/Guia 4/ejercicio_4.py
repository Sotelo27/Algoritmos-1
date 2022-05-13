'''
Escribir una función que reciba una palabra ó frase, y devuelva True, si es un palíndromo, ó False en caso 
contrario. Asumir que la cadena a recibir, sólo estará formada por caracteres alfabéticos y espacios en 
blanco. 
Un palíndromo es una palabra o frase que es igual si se lee de izquierda a derecha que de derecha a 
izquierda.  
Ejemplos:   Ana, ala, Neuquén, Oro, seres, radar 
  Arriba la birra 
   Amar da drama 
   Luz azul 
   La ruta natural
'''

def definir_palindromo(cadena):
  contador = 0 
  auxiliar = ""
  while contador < len(cadena):
        if cadena[contador] != " ":
              auxiliar += cadena[contador]
        contador += 1
  if auxiliar.upper() == auxiliar.upper()[::-1]:
        print("Es palindromo\n")

definir_palindromo("Luz azul")
definir_palindromo("Arriba la birra")
definir_palindromo("Amar da drama")
definir_palindromo("La ruta natural")
definir_palindromo("Ana")
