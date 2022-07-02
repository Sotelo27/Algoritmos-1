import herramientas as tools

def leer_linea(archivo, default):
    linea = archivo.readline()
    return linea if linea else default

def merge(gastos, excedidos, devoluciones, ranking):
    topes = tools.cargar_topes()
    linea = leer_linea(gastos, ",,,,")
    legajo, fecha, id_ticket, cod_reintegro, monto = linea.rstrip("\n").split(",")
    lista_ranking = []

    while legajo:
        legajo_ant = legajo
        total_gastos_emp = 0

        while legajo and legajo == legajo_ant:
            cod_reintegro_ant = cod_reintegro
            total_gastos_cod = 0

            while legajo and legajo == legajo_ant and cod_reintegro == cod_reintegro_ant:
                total_gastos_cod += int(monto)
                linea = leer_linea(gastos, ",,,,")
                legajo, fecha, id_ticket, cod_reintegro, monto = linea.rstrip("\n").split(",")
            
            if total_gastos_cod > topes[cod_reintegro_ant][1]:
                
                excedidos.write("El empleado " + legajo_ant + " se ha excedido del tope de reintegro de " + cod_reintegro_ant + ": "
                + topes[cod_reintegro_ant][0] + " por un monto de " + str(total_gastos_cod - topes[cod_reintegro_ant][1]) + "\n")
                
                devoluciones.write("Se le debe devolver al empleado " + legajo_ant + " por " + cod_reintegro_ant + ": " + topes[cod_reintegro_ant][0]
                + " , un total de " + str(topes[cod_reintegro_ant][1]) + "\n")
            
            else:
                devoluciones.write("Se le debe devolver al empleado " + legajo_ant + " por " + cod_reintegro_ant + ": " + topes[cod_reintegro_ant][0]
                + " , un total de " + str(total_gastos_cod) + "\n")
            
            total_gastos_emp += total_gastos_cod
        
        lista_ranking.append([legajo_ant, total_gastos_emp])
    
    lista_ranking.sort(key= lambda x: x[1], reverse = True)
    for i in lista_ranking:
        ranking.write(str(i[0]) + "," + str(i[1]) + "\n")


gastos = open("rendicion_gastos.csv", "r")
excedidos = open("excedidos.txt", "w")
devoluciones = open("devoluciones.txt", "w")
ranking = open("ranking_devoluciones.csv", "w")
merge(gastos, excedidos, devoluciones, ranking)
gastos.close()
excedidos.close()
devoluciones.close()
ranking.close()
print("Ya esta")