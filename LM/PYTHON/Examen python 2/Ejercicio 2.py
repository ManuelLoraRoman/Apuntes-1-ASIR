
import math

a = int(input("Introduzca el coeficiente a: "))
b = int(input("Introduzca el coeficiente b: "))
c = int(input("Introduzca el coeficiente c: "))

if a == 0:
    sol = -c / b
    print("La solución es", sol,".")
elif b ** 2 - (4 * a * c) < 0:
    print("Raíces complejas.")
else:
    sol1 = (-b + math.sqrt(b ** 2 - (4 * a * c)))/ (2 * a)
    sol2 = (-b - math.sqrt(b ** 2 - (4 * a * c)))/ (2 * a)
    print("La primera solución es", sol1,"y la segunda es",sol2,".")
