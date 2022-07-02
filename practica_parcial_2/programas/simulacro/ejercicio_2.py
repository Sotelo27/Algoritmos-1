import herramientas as tools
def leer_lineas(archivo,default):
    linea = archivo.readline()
    return linea if linea else default

def mergue(gastos,devoluciones,excedidos,ranking):
    lista_ranking = []
    topes = tools.cargar_topes()
    linea = leer_lineas(gastos,',,,,')
    legajo,fecha,id_ticket,cod_reintegro,monto = linea.rstrip('\n').split(',')
    while legajo:
        legajo_ant = legajo
        total_gastos_emp = 0
        while legajo_ant == legajo and legajo:
            cod_reintegro_ant = cod_reintegro 
            total_gastos_cod = 0
            while legajo_ant == legajo and cod_reintegro_ant == cod_reintegro:
                total_gastos_cod += int(monto)
                linea = leer_lineas(gastos,',,,,')
                legajo,fecha,id_ticket,cod_reintegro,monto = linea.rstrip('\n').split(',')
            if total_gastos_cod > topes[cod_reintegro_ant][1] :
                importe = total_gastos_cod - topes[cod_reintegro_ant][1]
                excedidos.write("El empleado {} a excedido del tope de reintegro de {} de {} por un importe de {} \n".format(legajo_ant,cod_reintegro_ant,str(topes[cod_reintegro_ant][0]),str(importe)))
            else:
                importe = topes[cod_reintegro_ant][1]
                devoluciones.write("El empleado {} se bede devolver el reintegro de {} de {} por un importe de {} \n".format(legajo_ant,cod_reintegro_ant,str(topes[cod_reintegro_ant][0]),str(importe)))
            total_gastos_emp += total_gastos_cod
        lista_ranking.append([legajo_ant, total_gastos_emp])
    
    lista_ranking.sort(key= lambda x: x[1], reverse = True)
    for i in lista_ranking:
        ranking.write(str(i[0]) + "," + str(i[1]) + "\n")

gastos = open('rendicion_gastos.csv','r')
devoluciones = open('devoluciones.txt','w')
excedidos = open('excedidos.txt','w')
ranking_devolciones = open('ranking_devoluciones.csv','w')
mergue(gastos,devoluciones,excedidos,ranking_devolciones)
gastos.close()
devoluciones.close()
excedidos.close()
ranking_devolciones.close()
