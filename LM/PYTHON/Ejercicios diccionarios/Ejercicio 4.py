
#Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase
#y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas.
#Guarda la información en un diccionario cuya claves serán los nombres de los alumnos
#y los valores serán listas con las notas de cada alumno.
#El programa pedirá el número de alumnos que vamos a introducir,
# pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo.
# Al final el programa nos mostrará la lista de alumnos
#y la nota media obtenida por cada uno de ellos.
#Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.

diccionario = {}
lista = []
total = 0
num = int(input("Dime la cantidad de alumnos: "))
for i in range(0,num):
    nombre = str(input("Dime el nombre del alumno: "))
    if nombre in diccionario.keys():
        print("ERROR. Programa finalizado.")
        break;
    nota = 0
    while nota >= 0:
        nota = int(input(f"Dime la nota de {nombre}: "))
        if nota < 0:
            break;
        lista.append(nota)
    diccionario[nombre] = lista
    lista = []
print(diccionario)
for i in diccionario.keys():
    print(i,"tiene una nota media de ",end="")
    for media in diccionario[i]:
        total = total + media
    print(total / len(diccionario[i]))
    total = 0
