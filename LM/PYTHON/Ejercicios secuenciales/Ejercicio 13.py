
#Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
#Python3 no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿Cómo se puede calcular?

import math

num = int(input("Dime un número:"))

raizcua = math.sqrt(num)

raizcub = num ** 1/3

print("La raíz cuadrada del número",num,"es",raizcua,"y la raíz cúbica es",raizcub,".")
