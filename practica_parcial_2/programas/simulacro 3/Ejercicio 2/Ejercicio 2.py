
# ----------- #
# EJERCICIO 2 #
# ----------- #

# La empresa lactea "Tres Leches", posee 3 centros de distribucion, desde los cuales distribuye
# diariamente la leche producida y envasada en su tambo central.
# Al final de c/dia, se deben procesar los archivos
# SUR.csv,NORTE.csv,CENTRO.csv, ordenados por codigo de lote
# * LOTE: codigo alfanumerico, por ejemplo, LES20210801
# * TIPO: posibles valores -> entera, descremada, sin lactosa
# * VENCIMIENTO: cadena de caracteres con formato AAAAMMDD
# * ENVASE: posibles valores -> sachet, tetrabrik
#
# Cada linea en el archivo representa un sachet o tetrabrik de 1 litro de leche
# el numero de lote aglutina varios litros de leche
#
# Se pide escribir un programa compuesto por funciones en Python que porcese los archivos y que cumpla con lo siguiente:
#
# 1. Genere un archivo unico DISTRIBUCION.csv unificando los datos de los 3 archivos, ordenado por lote, pero solo con aquellas
#  leches cuyo vencimiento suceda al menos 2 dias despues de la fehca actual
# de ejecucion del programa. Las leches que no cumplan con ello, deben ser ascentadas en el archivo VENCIDAS.csv
#
# 2. Calcular e imprimir la cantidad de litros de leche distribuidos por c/u de los 3 centros de distribucion.
#
# 3. Generar e imprimir los datos de produccion total de leche, ordenado por mayor a menor cantidad de litros, para 
# c/tipo de leche y por tipo de envase
#
# NOTAS:
# 1. Los archivos solo pueden ser leidos UNA VEZ en todo el proceso.
# 2. Ninguno de los archivos csv caben en memoria. A lo sumo, puede haber una lidea de c/u de ellos en memoria al mismo tiempo


from datetime import datetime

def leer_archivo(archivo):
    linea = archivo.readline()
    if linea:
        linea = linea.strip("\n").split(",")
    else:
        linea = None
    return linea

def lecheAlDia(VENCIMIENTO):

    dia = int(datetime.today().strftime('%d'))
    mes = int(datetime.today().strftime('%m'))
    anio = int(datetime.today().strftime('%Y'))
    estado = False

    if int(VENCIMIENTO[:4]) >= anio and int(VENCIMIENTO[4:6]) >= mes and int(VENCIMIENTO[-2:]) >= int(dia) + 2:
        estado = True

    return estado

def ordenarListaPorValor(lista,i):
    return sorted(lista,key=lambda x:x[i],reverse=True)

def imprimirLista(lista):
    for item in lista:
        print(item)



def distribucion(NOR,CEN,SUR,DIST,VENC):

    lecheNorte = leer_archivo(NOR)
    lecheSur = leer_archivo(SUR)
    lecheCentro = leer_archivo(CEN)

    cantDistribuidos = {"NORTE": 0, "SUR": 0, "CENTRO": 0}
    listaDistribuidos = []

    while lecheNorte or lecheCentro or lecheSur:
        if lecheNorte:
            datos = lecheNorte
            sede = "NORTE"
            lecheNorte = leer_archivo(NOR)
        elif lecheSur:
            datos = lecheSur
            sede = "SUR"
            lecheSur = leer_archivo(SUR)
        else:
            datos = lecheCentro
            sede = "CENTRO"
            lecheCentro = leer_archivo(CEN)

        LOTE,TIPO,VENCIMIENTO,ENVASE = datos

        if lecheAlDia(VENCIMIENTO):
            DIST.write(f"{LOTE},{TIPO},{VENCIMIENTO},{ENVASE}\n")
            cantDistribuidos[sede] += 1
            listaDistribuidos.append(datos)
        else:
            VENC.write(f"{LOTE},{TIPO},{VENCIMIENTO},{ENVASE}\n")


    #Ordena por mayor a menor la cantidad de leche producido x sede
    numeroDistribuidos = sorted(cantDistribuidos.items(),key=lambda x:x[1],reverse=True)
    for sede in numeroDistribuidos:
        print(f"sede: {sede[0]} --> cantidad: {sede[1]}")


    lecheOrdenadoPorTipo = ordenarListaPorValor(listaDistribuidos,1)
    lecheOrdenadoPorEnvase = ordenarListaPorValor(listaDistribuidos,3)

    print("Ordenado por Tipo de leche:")
    imprimirLista(lecheOrdenadoPorTipo)

    print("Ordenado por Tipo de Envase:")
    imprimirLista(lecheOrdenadoPorEnvase)

    return DIST,VENC






NOR = open("NORTE.csv","rt")
CEN = open("CENTRO.csv","rt")
SUR = open("SUR.csv","rt")

DIST = open("DISTRIBUCION.csv","w")
VENC = open("VENCIDAS.csv","w")

#Ejercicio 1
DIST,VENC = distribucion(NOR,CEN,SUR,DIST,VENC)





NOR.close()
CEN.close()
SUR.close()

DIST.close()
VENC.close()
