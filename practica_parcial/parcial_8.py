def validar_palabras(texto):
    lista_ordenada = []
    while len(texto.split()) < 5:
        texto = int(input("Su texto no contiene 100 palabras, reingrese a continuacion: "))
    for palabras in texto.split():
        if palabras[:2] != "ab" and palabras[:6] != "pseudo":
            lista_ordenada.append(palabras)
    lista_ordenada = sorted(lista_ordenada,key=lambda x:x)
    print(lista_ordenada)
validar_palabras("ab jose wilian papa dedo")
            