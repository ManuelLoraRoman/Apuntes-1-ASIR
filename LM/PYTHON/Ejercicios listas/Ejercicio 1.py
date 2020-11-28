
#Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente
#muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.
import random

lista = [random.randint(1,10)]
print("Lista:",lista[0]," ",end="")
for i in range (1,10):
    lista.append(random.randint(1,10))
    if i == 9:
        print(lista[i])
    else:
        print(lista[i]," ",end="")

for i in range(0,10):
    print(lista[i],lista[i] ** 2, lista[i] ** 3)
