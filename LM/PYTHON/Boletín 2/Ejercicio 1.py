
#Lee por teclado números y guardalo en una lista,
#el proceso finaliza cuando metamos un número negativo.
#Muestra el máximo de los números guardado en la lista,
#muestra los números pares.

lista = []
num = 0
while num >= 0:
    num = int(input("Dame un número: "))
    if num < 0:
        break;
    else:
        lista.append(num)
print(lista)
print("El número máximo guardado en la lista es",max(lista))
print("Números Pares:")
for i in lista:
    if int(i) % 2 == 0:
        print(i," ", end="")
