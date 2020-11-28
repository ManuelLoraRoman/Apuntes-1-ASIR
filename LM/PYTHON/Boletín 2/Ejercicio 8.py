
#Escriba un programa que permita crear dos listas de palabras
#y que, a continuación, elimine de la primera lista
#los nombres de la segunda lista

lista = []
num = int(input("Dime la cantidad de palabras a introducir: "))
for i in range(0,num):
    cad = str(input("Dame una palabra: "))
    lista.append(cad)
print("La lista sería: ",lista)
lista2 = []
num = int(input("Dime la cantidad de palabras a introducir: "))
for i in range(0,num):
    cad = str(input("Dame una palabra: "))
    lista2.append(cad)
print("La lista sería: ",lista2)
for i in lista:
    if i in lista2:
        lista.remove(i)
    lista.remove(i)
print("Lista 1 eliminación: ",lista)
