
#Algoritmo que pida un número y diga si es positivo, negativo o 0.

num = int(input("Dime un número:"))
if num > 0:
    print("El número es positivo.")
else:
    if num == 0:
        print("El número es 0.")
    else:
        print("El número es negativo.")
