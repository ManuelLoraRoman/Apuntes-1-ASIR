
print("SUMA ENTRE VALORES")
num1 = int(input("Escriba un número entero: "))
num2 = int(input(f"Escriba un número entero mayor que {num1}: "))
s = 0
if num2 < num1:
    print("¡Le he pedido un número entero mayor que",num1,"!")
else:
    for i in range(num1,num2 + 1):
        s = s + i
        if i < num2:
            print(i,"+ ",end="")
        else:
            print(i,end="")
print(" =",s,"\nLa suma desde",num1,"hasta",num2,"es",s)
