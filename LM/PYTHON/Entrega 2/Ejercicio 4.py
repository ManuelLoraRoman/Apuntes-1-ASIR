
#Escriba un programa que permita crear una lista de palabras y que, a continuación de tres opciones:
#    Contar: Me pide una cadena, y me dice cuantas veces aparece en la lista
#    Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas las apariciones de la primera por la segunda en la lista.
#    Eliminar: Me pide una cadena, y la elimina de la lista.
#El programa te muestra el menú, hasta que introduzcamos la opción 0 de salir.
#Dígame cuántas palabras tiene la lista: 4
#Dígame la palabra 1: Carmen
#Dígame la palabra 2: Alberto
#Dígame la palabra 3: Benito
#Dígame la palabra 4: Carmen
#La lista creada es: ['Carmen', 'Alberto', 'Benito', 'Carmen']
#Elige opción:
#1. Contar
#2. Modificar
#3. Eliminar
#0. Salir
#1
#Dígame la palabra a buscar: Carmen
#La palabra 'Carmen' aparece 2 veces en la lista.
#2
#Sustituir la palabra: Carmen
#por la palabra: David
#La lista es ahora: ['Alberto', 'David', 'Benito', 'David']
#3
#Palabra a eliminar: David
#La lista es ahora: ['Alberto', 'Benito']
#0
#Adiós!!!

lista = []
opcion = 1
palabras = int(input("Dígame cuántas palabras tiene la lista: "))
for i in range (palabras):
    print("Dígame la palabra", str(i + 1) + ": ", end="")
    palabra = input()
    lista += [palabra]
print("La lista creada es:", lista)
while opcion != 0:
    opcion = int(input("Elige opción:\n1.Contar\n2.Modificar\n3.Eliminar\n0.Salir\nOpción: "))
    if opcion == 1:
        contar = input("Dígame la palabra a buscar: ")
        if lista.count(contar) == 1:
            print(f"La palabra {contar} aparece",lista.count(contar),"vez en la lista.")
        else:
            print(f"La palabra {contar} aparece",lista.count(contar),"veces en la lista.")
    elif opcion == 2:
        sustituir = input("Sustituir la palabra: ")
        sustituir2 = input("por la palabra: ")
        for i in range(len(lista)):
            if lista[i] == sustituir:
                lista[i] = sustituir2
                print("La lista es ahora:", lista)
    elif opcion == 3:
        eliminar = input("Palabra a eliminar: ")
        lista.pop(lista.index(eliminar))
        print("La lista es ahora:",lista)
    elif opcion == 0:
        print("Adiós!!!")
    else:
        print("¡ERROR! Número introducido no válido.")
