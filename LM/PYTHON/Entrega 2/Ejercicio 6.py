
#Realizar un programa que guarde en una lista los nombre y edades de los alumnos de una clase.
#El programa ira pidiendo por teclado el nombre (string) y la edad (int) hasta que se introduzca como nombre un “*”.
# Las posiciones pares (0,2,4,…) de la lista serán cadenas y las impares son enteros.
# Cuando terminemos de meter datos hay que mostrar la siguiente información:
    #Los nombres de los alumnos con más edad.
    #La media de edad de la clase
    #Te pide por teclado un nombre y te dice la edad que tiene. Si hay varios alumnos con el mismo nombre te muestra todos.
    #Genera una nueva lista con los nombres y edades de los mayores de edad.


nombre = ""
lista = []
while nombre != "*":
    print("Dígame un nombre (* para parar): ", end="")
    nombre = input()
    if nombre == "*":
        break;
    print("Y una edad para el mismo:",end="")
    edad = int(input())
    lista += [nombre] + [edad]
print("La lista es:", lista)

print("ALUMNO MAYOR")
n = lista[1]
for i in range(1,len(lista),2):
    if n < lista[i]:
        n = lista[i]
print("Alumno con más edad:",lista[lista.index(n) - 1])

print("MEDIA")
media=0
for i in range(1,len(lista) + 1,2):
    media = media + int(lista[i])
print("La media de todas las edades es: %.2f años."% (media/(len(lista)/2)))

print("APARICIÓN Y EDAD")
nombrenuevo = str(input("Dime un nombre: "))
for i in lista:
    if i == nombrenuevo:
        print(f"La edad de {nombrenuevo} es de",lista[lista.index(i) + 1],"años.")

print("MAYORES DE EDAD")
listanueva = []
for i in range(1,len(lista),2):
    if lista[i] >= 18:
        listanueva.append(lista[i - 1])
        listanueva.append(lista[i])
print("Mayores de edad:",listanueva)
