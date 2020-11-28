
lista = []
listaaux = []
cad = ""
while cad != "*":
    cad = str(input("Introduzca una cadena: "))
    if cad == "*":
        break;
    lista.append(cad)
print("Lista ordenada alfabéticamente:", sorted(lista))
print("Cadenas con más de 5 caracteres:")
for i in lista:
    if len(i) > 5:
        print(i)
if lista.count(" ") >= 1:
    print("Si se ha introducido un espacio.")
else:
    print("No se ha introducido un espacio.")
ultcad = str(input("Dime una cadena a buscar: "))
print("Todas las búsquedas iguales:")
for i in lista:
    if i.startswith(ultcad):
        print(i)
