
#Realizar un programa que comprueba si una cadena leída por teclado comienza por una subcadena introducida por teclado.

cadena = str(input("Dame una cadena: "))
subcad = str(input("Dame una subcadena: "))

if cadena.startswith(subcad):
    print("Si que comienza.")
else:
    print("No comienza por la subcadena introducida.")
