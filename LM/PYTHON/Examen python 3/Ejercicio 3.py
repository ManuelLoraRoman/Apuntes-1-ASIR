#Realiza un programa que lea el siguiente fichero de texto (el contenido es variable,
# y lo puedes cambiar, este es sólo un ejemplo), con la siguiente información: nombre del artículo, precio, cantidad comprada:
#Fregona Rebajas, 4.5, 3
#Detergente, 2.0, 5
#Escoba, 1.5, 7

import Ejercicio1

lista = []
with open("Ejemplo3.txt","r") as fichero:
    for linea in fichero:
        art = linea.split(",")[0]
        precio = float(linea.split(",")[1])
        cant = int(linea.split(",")[2])
        lista.append(Ejercicio1.CalcularPrecio(art,precio,cant))
for i in range(0,len(lista)):
    print(lista[i])
