
#Pide una cadena y dos caracteres por teclado (valida que sea un carácter),
#sustituye la aparición del primer carácter en la cadena por el segundo carácter.

cadena = str(input("Dame una cadena: "))
c1 = str(input("Dame un carácter: "))
c2 = str(input("Dame otro carácter: "))

while len(c1) != 1 or len(c2) != 1:
    c1 = str(input("Dame un carácter: "))
    c2 = str(input("Dame otro carácter: "))

print(cadena.replace(c1,c2))
