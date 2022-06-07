def ejercicio_16(texto):
    listaNoRepetidas = []
    for palabra in texto.split():
        if len(palabra) in range(4,10) and palabra not in listaNoRepetidas:
            listaNoRepetidas.append(palabra)

    listaNoRepetidas = sorted(listaNoRepetidas,key=len)
    return sorted(listaNoRepetidas)

print(ejercicio_16("Hola holasa me llamasa santi santiago sipi santi"))