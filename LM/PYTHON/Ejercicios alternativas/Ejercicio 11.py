
#Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:
#Si se cumple Pitágoras entonces es triángulo rectángulo
#Si sólo dos lados del triángulo son iguales entonces es isósceles.
#Si los 3 lados son iguales entonces es equilátero.
#Si no se cumple ninguna de las condiciones anteriores, es escaleno.

A = int(input("Dime la longitud del lado A del triangulo:"))
B = int(input("Dime la longitud del lado B del triangulo:"))
C = int(input("Dime la longitud del lado C del triangulo:"))

if (A ** 2 + B ** 2 == C ** 2) or (A ** 2 + C ** 2 == B ** 2) or (B ** 2 + C ** 2 == A ** 2):
    print("El triángulo es rectángulo.")
else:
    if A == B and A != C or A == C and A != B or B == C and A != B:
        print("El triángulo es isósceles.")

if A == B and A == C:
    print("El triángulo es equilátero.")
else:
    if A != B and A != C and B != C:
        print("El triángulo es escaleno.")
