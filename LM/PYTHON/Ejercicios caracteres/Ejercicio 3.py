
#Pide una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuantas veces aparece el carácter en la cadena.

cadena = str(input("Dame una cadena: "))
carac = input("Dame un carácter: ")

while len(carac) != 1:
    carac = input("Dame otro carácter")

print("Aparece",cadena.count(carac),"veces el carácter",carac,".")
