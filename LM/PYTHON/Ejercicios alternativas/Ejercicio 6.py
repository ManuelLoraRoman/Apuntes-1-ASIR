
#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

cad = input("Dime algo para comprobar si es mayúscula:")

if cad == cad.upper():
    print("La cadena que has escrito está en mayúsculas.")
else:
    print("No está en mayúsculas.")
