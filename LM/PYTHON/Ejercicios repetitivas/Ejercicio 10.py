
#Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.

for n in range(1,6):
    print("Tabla de multiplicar del",n,":")
    for i in range(0,11):
        print(n,"x",i,"=",n * i)
    print("------------------------------")
