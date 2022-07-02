
# ----------- #
# EJERCICIO 1 #
# ----------- #

# una facultad tiene un archivo secuencial de CSV por c/u de sus 3 sedes.
# dichos archivos estan ordenados en forma ascendente, por padron, y contiene la info de las evaluaciones
# tomadas en c/u de las 2 sedes
# los campos son: padron(numero), cod_materia(nyumero), fecha(AAAAMMDD), calificacion(numero)

# Se tiene tambien un archivo CSV que contiene para cada cod_mateira, el nombre de la materia.
# En este archivo no tiene orden alguno, y SOLO PUEDE SER LEIDO UNA VEZ EN TODO EL PROGRAMA.
# Se pide:

# 1. Procesar los archivos obteniendo como resultado un UNICO ARCHIVO CSV ordenado ascendentemente por PADRON
#    donde c/linea esta compuesta por:
# 	 cod_materia,nombre_materia,fecha,calificaion y SOLO SI LA MATERIA FUE APROBADA POR EL ALUMNO EN EL AÑO 2020
#    En caso que el nombre de la materia NO EXISTA, esa linea debe ser enviada al archivo de errores.txt
#
# 2. Informar las 5 materias con mas aprobadas durante el año 2020,
#    ordenadas descendentemente por cantidad de aprobados.
#
# Aclaraciones:
# * Solo el archivo materias puede ser cargado totalmente en memoria
# * Leer solo los archivos de entrada y solo una vez c/u
# * Un mismo padron puede aparecer en mas de un archivo
# * Un mismo padron puede aparecer mas de una vez en el mismo archivo
# * El programa en Python debe ser estructurado y claro
#
# Archivos a Utilizar:
# sede_1.csv
# sede_2.csv
# materias.csv


def leer_archivo(archivo):
    linea = archivo.readline()
    if linea:
        linea = linea.strip("\n").split(",")
    else:
        linea = None
    return linea

def merge(s1,s2,sG):

    sede1 = leer_archivo(s1)
    sede2 = leer_archivo(s2)

    while sede1 or sede2:
        if sede1:
            padron,cod_mat,fecha,calificacion = sede1
            sede1 = leer_archivo(s1)
        else:
            padron,cod_mat,fecha,calificacion = sede2
            sede2 = leer_archivo(s2)

        sG.write(f"{padron},{cod_mat},{fecha},{calificacion}\n")

    return sG



def dicMaterias(mat):

    dicMat = {}
    materia = leer_archivo(mat)
    while materia:
        dicMat[materia[0]] = materia[1]
        materia = leer_archivo(mat)

    return dicMat

#EJERCICIO 1
def alumnosAprobados(sg,mat,aprobados,errores):

    sedeG = leer_archivo(sg)

    nombreMaterias = dicMaterias(mat)

    while sedeG:
        padron,cod_mat,fecha,calificacion = sedeG

        if cod_mat in nombreMaterias.keys():
            if int(calificacion) >= 4 and fecha[:4] == "2020":
                aprobados.write(f"{padron},{cod_mat},{nombreMaterias[cod_mat]},{fecha},{calificacion}\n")

        else:
            errores.write(f"{padron},{cod_mat},{fecha},{calificacion}\n")

        sedeG = leer_archivo(sg)


    return aprobados,errores

#EJERCICIO 2
def topAprobados(aprobados):

    dicAprobados = {}
    aprob = leer_archivo(aprobados)
    while aprob:
        materia = aprob[2]
        if materia not in dicAprobados:
            dicAprobados[materia] = 1
        else:
            dicAprobados[materia] += 1
        aprob = leer_archivo(aprobados)

    listAprobados = sorted(dicAprobados.items(), key=lambda x:x[1], reverse=True)

    i = 0
    while i in range(len(listAprobados)) and  i < 5:
        print(f"materia: {materia[0]} -- aprobados: {materia[1]}")
        i += 1



#Ejercicio 1
#abrimos y creamos los archivos
s1 = open("sede_1.csv",'rt')
s2 = open("sede_2.csv",'rt')
sG = open("sede_general.csv","w")

sG = merge(s1,s2,sG)
sG = open("sede_general.csv","r")

mat = open("materias.csv",'rt')
aprobados = open("aprobados.csv",'w')
errores = open("errores.txt",'w')


#Ejercicio 1
aprobados,errores = alumnosAprobados(sG,mat,aprobados,errores)

aprobados = open("aprobados.csv",'r')

#Ejercicio 2
topAprobados(aprobados)


#cierro los archivos antes de terminar el programa
s1.close()
s2.close()
sG.close()
mat.close()
errores.close()
aprobados.close()








