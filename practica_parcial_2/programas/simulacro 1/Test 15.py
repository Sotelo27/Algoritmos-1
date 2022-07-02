def leer_linea(archivo,default):
    linea=archivo.readline()
    return linea.rstrip('\n').split(',') if linea else default.split(',')


def procesar_archivo(saldos,movimientos,nuevos_saldos):

    nro_cta,nombre,apellido,saldo = leer_linea(saldos,',,,')
    nrocta,codoper,importe = leer_linea(movimientos,',,')
    estadistica = {}

    while nro_cta !=' ' or nrocta !=' ':
        
        nuevo_saldo=0
        while nro_cta==nrocta and (nro_cta !=' ' or nrocta !=' '):

            nuevo_saldo += int(importe)

            if codoper not in estadistica:
                estadistica[codoper] = int(importe)
            else:
                estadistica[codoper] += int(importe)
            
            nrocta,codoper,importe = leer_linea(movimientos,',,')
        
        saldo_final = nuevo_saldo + int(saldo)
        nuevos_saldos.write(nro_cta + ',' + nombre + ',' + ',' + apellido + ',' + saldo_final + '\n')
        nro_cta,nombre,apellido,saldo = leer_linea(saldos,',,,')

    for item in sorted(estadistica.items(),key = lambda x:x[1]):

        print(f"{item[0]}-------{item[1]} \n")
    
    pass



def main():

    saldos = open("saldo_anual.dat","r")
    movimientos = open("movi.dat","r")
    nuevos_saldos = open("saldo_actual","w")

    procesar_archivo(saldos,movimientos,nuevos_saldos)

    saldos.close()
    movimientos.close()
    nuevos_saldos.close()

    
    
