
#Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos.

import math

x1 = int(input("Defina la x de un punto 1:"))
y1 = int(input("Defina la y de un punto 1:"))
x2 = int(input("Defina la x de un punto 2:"))
y2 = int(input("Defina la y de un punto 2:"))

distancia = math.sqrt(pow((x2 - x1),2) + pow((y2 - y1),2))

print("La distancia entre los dos puntos sería %.2f."%(distancia))
