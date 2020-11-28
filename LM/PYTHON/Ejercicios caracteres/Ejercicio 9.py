
#Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.

cadena = str(input("Dame una cadena: "))
subcad = str(input("Dame una subcadena: "))

if cadena.find(subcad):
    print("La cadena contiene a la subcadena.")
else:
    print("No contiene a la subcadena.")
