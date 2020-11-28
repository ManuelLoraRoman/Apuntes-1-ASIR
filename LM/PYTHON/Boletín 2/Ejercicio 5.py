
#Escribe un programa que permita crear una lista de palabras
#y que, a continuación, pida una palabra y diga cuántas veces
#aparece esa palabra en la lista.

lista = []
n = 0
num = int(input("Dime la cantidad de palabras a introducir: "))
for i in range(0,num):
    cad = str(input("Dame una palabra: "))
    lista.append(cad)
print("La lista sería: ",lista)
peti = str(input("Dame una palabra a buscar: "))
for i in lista:
    if peti == i:
        n = n + 1
if n == 1:
    print(f"La palabra {peti} aparece repetida 1 vez.")
else:
    print(f"La palabra {peti} aparece repetida",n,"veces.")
