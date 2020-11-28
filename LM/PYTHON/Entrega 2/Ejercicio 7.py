
#Repite el ejercicio 6, pero utilizando la siguiente estructura: una lista,
#en la cual cada elemento es una lista con dos elementos: el nombre y la edad. Por ejemplo:
#[ ["juan",18],["maría",21],["pablo",15] ]

nombre = ""
lista = []
while nombre != "*":
    print("Dígame un nombre (* para parar): ", end="")
    nombre = input()
    if nombre == "*":
        break;
    print("Y una edad para el mismo:",end="")
    edad = int(input())
    lista.append([nombre,edad])
print("La primera lista es:", lista)

print("ALUMNO MAYOR")
n = lista[0][1]
j = 0
for i in range(0,len(lista)):
    if n < lista[i][1]:
        n = lista[i][1]
        j = i
print("Alumno con más edad:",lista[j][lista[j].index(n) - 1])

print("MEDIA")
media=0
for i in range(0,len(lista)):
    media = media + lista[i][1]
print("La media de todas las edades es: %.2f años."% (media/(len(lista))))

print("APARICIÓN Y EDAD")
nombrenuevo = str(input("Dime un nombre: "))
for i in lista:
    if i[0] == nombrenuevo:
        print(f"La edad de {nombrenuevo} es de",i[1],"años.")

print("MAYORES DE EDAD")
listanueva = []
for i in lista:
    if i[1] >= 18:
        listanueva.append(i)
print("Mayores de edad:",listanueva)
