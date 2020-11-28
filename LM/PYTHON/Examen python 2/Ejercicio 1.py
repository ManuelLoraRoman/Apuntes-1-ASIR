
lista = []
media = 0
num = int(input("Nº a introducir: "))
for i in range(0,num):
    number = int(input("Introduzca un número: "))
    lista.append(number)
print("Nº que hay en la lista: ", len(lista))
print("Nº mayor de la lista: ", max(lista))
print("Lista ordenada",sorted(lista))
for i in lista:
    media = media + int(i)
print("La media de todos los números es", media / len(lista))
