
#Escriba un programa que permita crear una lista de palabras
# y que, a continuación, pida una palabra
# y elimine esa palabra de la lista.

lista = []
num = int(input("Dime la cantidad de palabras a introducir: "))
for i in range(0,num):
    cad = str(input("Dame una palabra: "))
    lista.append(cad)
print("La lista sería: ",lista)
eli = str(input("Dame una palabra a eliminar: "))
for i in lista:
    if eli == i:
        lista.remove(i)
lista.remove(i)
print("Lista con elementos eliminados: ",lista)
