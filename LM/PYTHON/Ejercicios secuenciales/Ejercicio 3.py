
#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

import math;

cateto1 = int(input("Dime la longitud del cateto nº1: "))
cateto2 = int(input("Dime la longitu del cateto nº2: "))
hipotenusa = math.sqrt(pow(cateto1,2) + pow(cateto2,2))
print("La hipotenusa del triángulo rectángulo es de", round(hipotenusa,2),".")
