#Realiza un programa que vaya pidiendo artículos (nombre y precio) y la cantidad que el cliente ha comprado
#y te vaya mostrando el precio final (utilizando las funciones anteriores).
#El programa termina cuando introducimos un * como nombre de artículo.

import Ejercicio1
nombre = ""
lista = []
while True:
    if nombre != "*":
        nombre = str(input("Dime el nombre del artículo: "))
        if nombre == "*":
            break;
        precio = int(input(f"Dime el precio individual de {nombre}: "))
        cant = int(input(f"Dime la cantidad de {nombre}: "))
        lista.append(Ejercicio1.CalcularPrecio(nombre,precio,cant))
for i in range(0,len(lista)):
    print(lista[i])
