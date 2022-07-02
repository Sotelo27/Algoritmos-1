def leer_linea(archivo,campos):
    linea = archivo.readline()
    if not linea:
        if campos == 3:
            linea = ',,'
        else:
            linea = ',,,'

    return linea.rstrip("\n").split(",")

def actualizacion(saldoAnual,movi,actualizado):

    dicCodoper = {}

    nro_sal,nombre,apellido,saldo  = leer_linea(saldoAnual,4)

    nro_imp,codoper,importe = leer_linea(movi,3)

    while nro_sal: #corte principal

        nro_imp_ant = nro_imp # MUCHOS IMPORTES -> MUCHOS NRO_CTA
        importe_total = 0

        while nro_sal and nro_imp and nro_imp_ant == nro_imp: #primer corte (siguiendo en una linea)
            importe_total += int(importe)

            nro_imp, codoper, importe = leer_linea(movi,3)


        importe_total +=   int(saldo)
        dicCodoper[nro_sal] = importe_total

        actualizado.write(f"{nro_sal},{nombre},{apellido},{importe_total}\n")

        nro_sal, nombre, apellido, saldo = leer_linea(saldoAnual,4)

    estadisticas = sorted(dicCodoper.items(),key=lambda x:x[1],reverse=True)

    for cuenta in estadisticas:
        print(f"cuenta: {cuenta[0]} -- importe total: {cuenta[1]}")


saldoAnual = open("saldo_anual.csv","r")
movi = open("movi.csv","r")
actualiado = open("actualizacion.csv","w")

actualizacion(saldoAnual,movi,actualiado)

saldoAnual.close()
movi.close()
actualiado.close()