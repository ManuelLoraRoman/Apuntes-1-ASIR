
#El módulo random incluye la función random() que genera un número seudo-aleatorio entre 0 y 1:

import random
 #>>> random()
 #0.51605767814317494

#Crea un programa que pida al usuario un número n y genere una lista con n elementos con valores aleatorios y muestre como salida:

    #La lista de los n números aleatorios con una precisión de 3 decimales.
    #La suma de todos los elementos con una precisión de 2 decimales.

#Nota: Los valores deben redondearse a la precisión solicitada, no truncarse.

#Ejemplo:

 #Dame un numero: 4
 #La lista de 4 numeros aleatorios es: (0.123, 0.432, 0.335, 0.456)
 #La suma de estos 4 elementos es: 1.3

lista = []
suma = 0
num = int(input("Dame un número: "))
for i in range(0,num):
    lista.append(round(random.random(),3))
print("La lista de",num,"números aleatorios es:",lista)
for i in range(0,num):
    suma = suma + lista[i]
print("La suma de estos",num,"elementos es:",round(suma,3))
