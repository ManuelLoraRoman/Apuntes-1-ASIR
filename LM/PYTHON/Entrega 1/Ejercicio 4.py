
#Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.

#Notas:

#    Un número es divisible por otro cuando el resto de su división es cero (numero % divisor == 0).
#    Se puede hacer un programa más rápido, teniendo en cuenta que los divisores son siempre menores (o iguales) que la mitad del número.
#    Es decir, no hace falta probar todos los números entre 1 y el propio número, sino únicamente hasta la mitad.
#    Si se hace así, no hay que olvidarse de añadir el propio número a la lista de divisores.

#Ejemplo:

#DIVISORES
#Escriba un número mayor que cero: -5
#¡Le he pedido un número entero mayor que cero!

#DIVISORES
#Escriba un número entero mayor que cero: 200
#Los divisores de 200 son 1 2 4 5 8 10 20 25 40 50 100 200


print("DIVISORES")
num = int(input("Escriba un número mayor que cero: "))
if num < 0:
    print("¡Le he pedido un número entero mayor que cero!")
else:
    cad = ""
    for i in range(1,(num // 2) + 1):
        if num % i == 0:
            s = str(i)
            cad = cad + " " + s
    numcad = str(num)
    print("Los divisores de",num,"son" + cad + " " + numcad)
