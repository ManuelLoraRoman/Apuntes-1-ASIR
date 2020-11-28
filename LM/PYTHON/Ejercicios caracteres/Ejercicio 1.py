
#Escribir por pantalla cada carácter de una cadena introducida por teclado.

cadena = str(input("Dime una cadena: "))

for i in range(0,len(cadena)):
    if i == len(cadena) - 1:
        print(cadena[i])
    else:
        print(cadena[i],"-",end="")
