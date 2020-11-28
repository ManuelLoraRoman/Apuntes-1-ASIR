
#Escriba un programa que permita crear una lista de palabras
#y que, a continuación, pida dos palabras
# y sustituya la primera por la segunda en la lista.

lista = []
num = int(input("Dime la cantidad de palabras a introducir: "))
for i in range(0,num):
    cad = str(input("Dame una palabra: "))
    lista.append(cad)
print("La lista sería: ",lista)
sus1 = str(input("Palabra a sustituir: "))
sus2 = str(input("Palabra sustituta: "))
for i in lista:
    if i == sus1:
        lista[lista.index(i)] = sus2
print("Lista sustituida: ",lista)
