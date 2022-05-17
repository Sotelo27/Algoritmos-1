'''
El diccionario sistema_previsional tiene cargados para cada país (clave) dos enteros: cantidad de personas trabajando y cantidad de personas jubiladas (ambos dados en miles).
Se pide que armes un programa en Python (compuesto por funciones) que:

Permita la carga de nuevos datos. Si el país ya existe en el diccionario, deberá actualizar los datos con los nuevos ingresados.
Calcule el promedio mundial de personas que están trabajando y personas jubiladas.
Liste, de mayor a menor, los países con los porcentajes de relación jubilados / trabajadores.
Indicando:
                  País – porcentaje
'''

def cargar_datos():
    sistema_previsional = {}
    respuesta = input("Desea ingresar paises? si/no: ")
    while respuesta.lower() == "si":
        pais = input("Ingrese a continuacion el pais: ")
        personas_trabajando = int(input("Ingrese la cantidad de personas trabajando: "))
        jubilados = int(input("Ingrese a continuacion la cantidad de jubilados: "))
        if pais not in sistema_previsional:
            sistema_previsional[pais] = [personas_trabajando,jubilados]
        else:
            sistema_previsional[pais][0] = personas_trabajando
            sistema_previsional[pais][1] = jubilados
        respuesta = input("Desea ingresar paises? si/no: ")
    return sistema_previsional

def calcular_promedio_mundial(sist_previsional):
    total_jubilados = 0
    total_personas = 0
    total_trabajando = 0
    for paises in sist_previsional:
        total_jubilados += sist_previsional[paises][1]
        total_trabajando += sist_previsional[paises][0]
    promedio_mundial = total_jubilados / total_trabajando
    return promedio_mundial

def calcular_promedio_pais(sistema_previsional):
    pais_porcentaje = []
    for paises in sistema_previsional:
        porcentaje = sistema_previsional[paises][1] / sistema_previsional[paises][0]
        pais_porcentaje.append([paises,porcentaje])
    pais_porcentaje = sorted(pais_porcentaje ,key=lambda x:x[1] ,reverse=True)
    return pais_porcentaje

def main():
    sistema_previsional = cargar_datos()
    print(sistema_previsional)
    promedios_mundiales = calcular_promedio_mundial(sistema_previsional)
    print("")
    print(promedios_mundiales)
    pais_porcentaje = calcular_promedio_pais(sistema_previsional)
    print("")
    print(pais_porcentaje)

main()