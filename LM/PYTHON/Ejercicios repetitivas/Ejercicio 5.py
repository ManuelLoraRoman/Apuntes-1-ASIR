
#Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' en caso contrario, el programa termina cuando se introduce un espacio.

n = ""
while n != " ":
    n = input("Dime un carácter: ")
    if n == "a" or n == "e" or n == "i" or n == "o" or n == "u":
        print("VOCAL")
    else:
        print("N0 V0CAL")
print("Programa terminado")
