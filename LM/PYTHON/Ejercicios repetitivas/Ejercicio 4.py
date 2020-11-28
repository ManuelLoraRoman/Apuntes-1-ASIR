
#Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir).
#El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

cant = int(input("Dime la cantidad de números a introducir: "))
may = 0
men = 0
igu = 0

for i in range(0,cant):
    num = int(input("Dime un número: "))
    if num > 0:
        may = may + 1
    elif num < 0:
        men = men + 1
    if num == 0:
        igu = igu + 1
print("Nº mayores que 0:",may,".\n Nº menores que 0:",men,".\n Nº iguales que 0:",igu,".")
