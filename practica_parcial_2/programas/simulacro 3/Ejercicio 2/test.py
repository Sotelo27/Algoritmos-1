

from datetime import datetime
hoy = datetime.today().strftime('%Y%m%d')

dia = datetime.today().strftime('%d')
print(dia)


fecha = '20220625'

print(fecha[:4])
print(fecha[4:6])
print(fecha[-2:])