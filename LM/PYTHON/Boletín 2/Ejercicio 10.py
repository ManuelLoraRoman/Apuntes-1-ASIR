
#Escribir una función que reciba una lista de elementos
#e indique si se encuentran ordenados de menor a mayor o no.

lista = []
num = 0
num = int(input("Dime la cantidad de palabras a introducir: "))
for i in range(0,num):
    cad = str(input("Dame una palabra: "))
    lista.append(cad)
print("La lista sería: ",lista)
lista2 = lista[:]
lista2.sort()
#for i in lista:
#    for n in lista2:
#        if i == n:
#            num = num + 1
if lista == lista2:
    print("La lista SÍ que está ordenada de menor a mayor.")
else:
    print("La lista NO está ordenada de menor a mayor.")
