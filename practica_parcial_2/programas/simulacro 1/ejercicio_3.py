def leer_lineas(archivo,default):
    linea = archivo.readline()
    return linea if linea else default

def merge(saldo_anual,movi,saldo_actual):
    sumatoria_importes = []
    linea = leer_lineas(saldo_anual,',,,,')
    linea_2 = leer_lineas(movi,',,,')
    nro_cuenta,nombre,apellido,saldo = linea.rstrip('\n').split(',')
    nro_cuenta_2,cod_operacion,importe = linea_2.rstrip('\n').split(',')

    while nro_cuenta :
        nro_cuenta_ant_2 = nro_cuenta_2
        total_gastos_cliente = 0
        while nro_cuenta and nro_cuenta_ant_2 == nro_cuenta_2:
            total_gastos_cliente += int(importe)
            nro_cuenta_2,cod_operacion,importe = linea_2.rstrip('\n').split(',')
        total_gastos_cliente += saldo
        sumatoria_importes[nro_cuenta] = total_gastos_cliente
        saldo_actual.write('{} {} {} {} \n'.format(nro_cuenta,nombre,apellido,total_gastos_cliente))
        nro_cuenta,nombre,apellido,saldo = linea.rstrip('\n').split(',')
    importes_ordenados = sorted(sumatoria_importes.items(),key=lambda x:x[1] , reverse=True)
    for elementos in importes_ordenados:
        print('La cuenta {} tiene una sumatoria de importes de {}'.format(importes_ordenados[0],importes_ordenados[1]))
    


saldo_anual = open('saldo_anual.dat','r')
movi = open('movi.dat','r')
saldo_actual = open('saldo_actual','w')
merge(saldo_actual,movi,saldo_actual)
saldo_anual.close()
movi.close()
saldo_actual.close()


