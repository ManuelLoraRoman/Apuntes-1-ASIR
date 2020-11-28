
#Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.

numsum = 0
n = 0
while True:
    num = int(input("Escriba un número: "))
    if num != 0:
        numsum = numsum + num
        n = n + 1
    if num == 0:
        break;
print("La suma de todos los números introducidos es",numsum,"\n La media es",numsum / n,".")
