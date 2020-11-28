
#Realizar un programa que, dada una lista,
#devuelva una nueva lista cuyo contenido sea igual a la original
#pero invertida. Así, dada la lista
#[‘Di’, ‘buen’, ‘día’, ‘a’, ‘papa’],
#deberá devolver [‘papa’, ‘a’, ‘día’, ‘buen’, ‘Di’].

lista = []
num = int(input("Dime la cantidad de palabras a introducir: "))
for i in range(0,num):
    cad = str(input("Dame una palabra: "))
    lista.append(cad)
print("La lista sería: ",lista)
lista1 = lista[::-1]
print("La lista invertida sería: ",lista1)
