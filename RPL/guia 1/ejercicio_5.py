lado_1 = int(input("Ingrese la longitud del primer lado del triangulo: "))
lado_2 = int(input("Ingrese la longitud del segundo lado del triangulo: "))
lado_3 = int(input("Ingrese la longitud del tercer lado del triangulo: "))
if (lado_1 == lado_2 and lado_1 == lado_3):
    print("Es equilatero")
elif(lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3):
    print("Es isosceles")
else:
    print("Es escaleno")