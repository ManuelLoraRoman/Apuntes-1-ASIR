
#Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente),
#saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.

base = int(input("Dime la base: "))
exponente = int(input("Dime el exponente: "))
resultado = 1

for i in range(0,exponente):
    resultado = resultado * base
print("El resultado de la potencia es",resultado,".")
