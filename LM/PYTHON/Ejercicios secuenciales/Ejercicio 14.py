
#Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.
#Ejemplo, si se introduce 23 que muestre 32.

num2 = int(input("Dime un número de dos cifras:"))

inv = str(num2)[::-1]

print("Tu número:",num2,". Tu número invertido:",inv,".")
