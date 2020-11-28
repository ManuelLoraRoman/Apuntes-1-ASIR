
#Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y muestre un mensaje cada vez que un número no sea mayor que el primero.

#MAYORES QUE EL PRIMERO
#¿Cuántos valores va a introducir? -1
#¡Imposible!

#MAYORES QUE EL PRIMERO
#¿Cuántos valores va a introducir? 4
#Escriba un número: 6
#Escriba un número más grande que 6: 10
#Escriba un número más grande que 6: 3
#¡3 no es mayor que 6!
#Escriba un número más grande que 6: 9
#Gracias por su colaboración


print("MAYORES QUE EL PRIMERO")
num = int(input("¿Cuántos valores va a introducir?"))
if num < 1:
    print("¡Imposible!")
else:
    num1 = int(input("Escriba un número: "))
    for i in range(num - 1):
        num2 = int(input(f"Escriba un número más grande que {num1}: "))
        if num2 <= num1:
            print("¡",num2,"no es mayor que",num1,"!")
    print("Gracias por su colaboración")
