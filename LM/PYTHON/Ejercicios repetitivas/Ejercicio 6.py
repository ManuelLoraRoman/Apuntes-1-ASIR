
#Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

num1 = int(input("Dime un número: "))
num2 = int(input("Dime otro número: "))
print("Los números pares entre esos dos números son: ",end= "")
for i in range(num1,num2):
    if i % 2 == 0:
        print(i," ",end = "")
