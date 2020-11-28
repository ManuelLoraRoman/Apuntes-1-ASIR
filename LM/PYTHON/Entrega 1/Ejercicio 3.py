
#Escriba un programa que pida tres números y que escriba si son los tres iguales, si hay dos iguales o si son los tres distintos.

#COMPARADOR DE TRES NÚMEROS
#Escriba un número: 6
#Escriba otro número: 6
#Escriba otro número más: 6
#Ha escrito tres veces el mismo número.

#COMPARADOR DE TRES NÚMEROS
#Escriba un número: 6
#Escriba otro número: 6.5
#Escriba otro número más: 6
#Ha escrito uno de los números dos veces.

#COMPARADOR DE TRES NÚMEROS
#Escriba un número: 4
#Escriba otro número: 5
#Escriba otro número más: 6
#Los tres números que ha escrito son distintos.



print("COMPARADOR DE TRES NÚMEROS")
num1 = int(input("Escriba un número: "))
num2 = int(input("Escriba otro número: "))
num3 = int(input("Escriba otro número más: "))
if num1 == num2 and num1 == num3:
    print("Ha escrito tres veces el mismo número.")
elif num1 == num2 or num2 == num3 or num1 == num3:
    print("Ha escrito uno de los números dos veces.")
elif num1 != num2 and num1 != num3 and num2 != num3:
    print("Los tres números que ha escrito son distintos.")
