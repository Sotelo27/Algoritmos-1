'''
Este ejercicio nos permitirá conocer e implementar un concepto muy útil en las finanzas personales.

A menudo, las personas que poseen capital para invertir (inversores) 
buscan una herramienta de inversión que les permita obtener una rentabilidad fija tomando 
un bajo riesgo. Para esto, pueden prestar su dinero a una empresa o estado a cambio de que 
la entidad que toma la deuda devuelva la misma con intereses llegada una fecha acordada.

Por ejemplo, un inversor puede obtener un 3% de rentabilidad por prestarle su dinero a 
una empresa por un año. Es decir que si el inversor le presta 100 dólares a la empresa, 
esta deberá devolverle 103 dólares al inversor al terminar el año que dura el préstamo.
A su vez, el inversor puede volver a invertir estos 103 dólares, obteniendo nuevamente un 
3% de rentabilidad. Sin embargo, al terminar el préstamo, la empresa debe devolver 
3,09 dólares adicionales de intereses (y no 3 como antes), ya que el capital de inversión pasó 
de ser 100 dólares el primer año a 103 el segundo.

De esta forma, los inversores pueden proyectar sus ganancias utilizando el interés compuesto,
 en donde cada vez que finaliza un préstamo vuelven a invertir el capital inicial más las ganancias de la inversión, 
 logrando así retornos nominales mayores a medida que pasa el tiempo.

La función a completar recibe un capital inicial, un tiempo de inversión en años y un porcentaje de rentabilidad. 
Debe retornar cuál será el valor del capital luego de invertirlo año a año obteniendo la rentabilidad indicada.

Por ejemplo, si el capital inicial es 100, el tiempo de inversión es 3 años, y el porcentaje de rentabilidad es 3%, tenemos:

Primer año de inversión:

Inicio: 100; Intereses: 3; Final: 103;

Segundo año de inversión:

Inicio: 103; Intereses: 3,09; Final: 106,09;

Tercer año de inversión:

Inicio: 106,09; Intereses: 3,1827; Final: 109,2727;

El valor que retorna nuestra función es 109,2727.
'''
def interes_compuesto(capital_inicial, tiempo_de_inversion, porcentaje_de_rentabilidad):
    capital_final = 0
    for i in range(0 , tiempo_de_inversion):
        capital_final = (capital_inicial * porcentaje_de_rentabilidad)/ 100 + capital_inicial
        capital_inicial = capital_final
    return capital_final

print(interes_compuesto(100,3,3))
