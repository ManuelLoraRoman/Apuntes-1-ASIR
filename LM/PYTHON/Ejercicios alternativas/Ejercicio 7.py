
#Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:
#El exponente sea positivo, sólo tienes que imprimir la potencia.
#El exponente sea 0, el resultado es 1.
#El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

base = int(input("Dime la base de la potencia:"))
exponente = int(input("Dime el exponente ahora:"))

if exponente > 0:
    print("El resultado de la potencia",base,"^",exponente,"=",base ** exponente,".")
else:
    if exponente == 0:
        print("El resultado de la potencia es 1.")
    else:
        print("El resultado de la potencia",base,"^",exponente,"=", 1 / (base ** abs(exponente)),".")
