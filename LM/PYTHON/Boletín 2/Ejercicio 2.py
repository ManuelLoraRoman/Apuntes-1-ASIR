
#Escribe un programa que permita crear una lista de palabras.
#Para ello, el programa tiene que pedir un número y luego
#solicitar ese número de palabras para crear la lista.
#Por último, el programa tiene que escribir la lista.

lista = []
num = int(input("Dime la cantidad de palabras a introducir: "))
for i in range(0,num):
    cad = str(input("Dime una palabra: "))
    lista.append(cad)
print("La lista es:\n",lista)
