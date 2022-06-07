def registro_campeonato(campeonato):
    diccionario_campeonato = {}
    for equipos in campeonato:
        diccionario_campeonato[equipos[0]] = equipos[1] * 3 + equipos[2]
    return diccionario_campeonato
   
def ordenar_registro(regis_campeonato):
    tabla_ordenada = sorted(regis_campeonato.items(),key= lambda x:x[1],reverse= True)
    return tabla_ordenada

def main():
    campeonato = [["Boca",19,0,0],["River",0,1,18],["San Lorenzo",12,2,5],["Racing",6,10,3]]
    tabla_campeonato_puntajes = registro_campeonato(campeonato)
    print(tabla_campeonato_puntajes) #para que verifiques los puntos
    tabla_ordenada = ordenar_registro(tabla_campeonato_puntajes)
    print(tabla_ordenada)# para que veas la tabla ordenada por puntos

main()
