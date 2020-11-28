
#Crea un programa que pida al usuario dos números
#y muestre su división si el segundo no es cero,
#o un mensaje de aviso en caso contrario.

num1 = int(input("Dime el primer número:"))
num2 = int(input("Dime el segundo número:"))

if num2 != 0:
    print("La división sería",num1,"/",num2,"=",num1/num2,".")
else:
    print("¡ERROR!")
