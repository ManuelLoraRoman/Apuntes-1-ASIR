
#Dada una lista de números enteros
#(guarda la lista en una variable)
# y un entero k, escribir un programa que:
    #Cree tres listas, una con los menores,
    #otra con los mayores y otra con los iguales a k.
    #Crea otra lista lista con aquellos que son múltiplos de k.
import random

lista = []
listaup = []
listadown = []
listaigual = []
listamult = []
k = int(input("Dime el nº k: "))
num = int(input("Dime la cantidad de nº de la lista: "))
for i in range(0,num):
    lista.append(random.randint(0,100))
print("Lista principal:\n",lista)
for i in lista:
    if int(i) < k:
        listadown.append(i)
    elif int(i) == k:
        listaigual.append(i)
    else:
        listaup.append(i)
print(f"Lista menores que {k}:",listadown)
print(f"Lista mayores que {k}:",listaup)
print(f"Lista iguales que {k}:",listaigual)
for i in lista:
    if int(i) % k  == 0:
        listamult.append(i)
print(f"Lista múltiplos de {k}",listamult)
