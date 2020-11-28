
#Escribe un programa que lea una cadena y
#devuelva un diccionario con la cantidad
#de apariciones de cada carácter en la cadena.

cad = str(input("Dame una cadena: "))
diccionario = {}
for i in range(0,len(cad)):
    diccionario[cad[i]] = cad.count(cad[i])
print("El diccionario sería: ", diccionario)
