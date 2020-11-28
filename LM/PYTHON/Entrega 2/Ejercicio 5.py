
#Escriba un programa que permita crear dos listas de palabras y que, a continuación, escriba las siguientes listas (en las que no debe haber repeticiones):
#    Lista de palabras que aparecen en las dos listas.
#    Lista de palabras que aparecen en la primera lista, pero no en la segunda.
#    Lista de palabras que aparecen en la segunda lista, pero no en la primera.
#    Lista de palabras que aparecen en ambas listas.
#Nota: Para evitar las repeticiones, el programa deberá empezar eliminando los elementos repetidos en cada lista.
#Dígame cuántas palabras tiene la primera lista: 4
#Dígame la palabra 1: Carmen
#Dígame la palabra 2: Alberto
#Dígame la palabra 3: Benito
#Dígame la palabra 4: Carmen
#La primera lista es: ['Carmen', 'Alberto', 'Benito', 'Carmen']
#Dígame cuántas palabras tiene la segunda lista: 3
#Dígame la palabra 1: Benito
#Dígame la palabra 2: Juan
#Dígame la palabra 3: Carmen
#La segunda lista es: ['Benito', 'Juan', 'Carmen']
#Palabras que aparecen en las dos listas: ['Carmen', 'Benito']
#Palabras que sólo aparecen en la primera lista: ['Alberto']
#Palabras que sólo aparecen en la segunda lista: ['Juan']
#Todas las palabras: ['Carmen', 'Benito', 'Alberto', 'Juan']

num1 = int(input("Dígame cuántas palabras tiene la primera lista: "))
lista1 = []
for i in range(num1):
    print("Dígame la palabra", str(i + 1) + ": ", end="")
    palabra1 = input()
    lista1 += [palabra1]
print("La primera lista es:", lista1)
num2 = int(input("Dígame cuántas palabras tiene la segunda lista: "))
lista2 = []
for i in range(num2):
    print("Dígame la palabra", str(i + 1) + ": ", end="")
    palabra2 = input()
    lista2 += [palabra2]
print("La segunda lista es:", lista2)
iguales = []
for i in lista1:
    if i in lista2:
        iguales += [i]
if iguales == []:
    print("No hay palabras que aparecen en ambas listas.")
else:
    print("Palabras que aparecen en las dos listas:", set(iguales))
sololista1 = []
for i in lista1:
    if i not in lista2:
        sololista1 += [i]
if sololista1 == []:
    print("No hay palabras que solo aparezcan en la primera lista.")
else:
    print("Palabras que sólo aparecen en la primera lista:", set(sololista1))
sololista2 = []
for i in lista2:
    if i not in lista1:
        sololista2 += [i]
if sololista2 == []:
    print("No hay palabras que sólo aparecen en la segunda lista.")
else:
    print("Palabras que sólo aparecen en la segunda lista:", set(sololista2))
todas = lista1 + lista2
print("Todas las palabras:", set(todas))
