
#Introducir una cadena de caracteres e indicar si es un palíndromo.
#Una palabra palíndroma es aquella que se lee igual adelante que atrás.

cadena = str(input("Dame una cadena: "))
print("Cadena al revés:",cadena[::-1])
if cadena[::-1] == cadena:
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
