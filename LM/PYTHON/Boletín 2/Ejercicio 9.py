
#Escriba un programa que permita crear una lista de palabras y
#que, a continuación, elimine los elementos repetidos
#(dejando únicamente el primero de los elementos repetidos).

lista = []
num = int(input("Dime la cantidad de palabras a introducir: "))
for i in range(0,num):
    cad = str(input("Dame una palabra: "))
    lista.append(cad)
print("La lista sería: ",lista)
for i in lista:
    if lista.count(i) > 1:
        lista.remove(i)
print("Lista eliminación repetidos: ",lista)
