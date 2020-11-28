
#Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.

num = int(input("Dime un número: "))
print("TABLA DE MULTIPLICAR DEL",num,":")
for i in range(0,11):
    print(num,"x",i,"=",num * i)
