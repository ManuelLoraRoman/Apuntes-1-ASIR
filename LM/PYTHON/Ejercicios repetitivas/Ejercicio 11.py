
#Escribe un programa que diga si un número introducido por teclado es o no primo.
#Un número primo es aquel que sólo es divisible entre él mismo y la unidad.
# Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número.

primo = False
n = int(input("Introduzca un número: "))
for i in range(1,n):
    if  i != 1 and n % i == 0:
        primo = False
    else:
        primo = True
if primo:
    print("Es primo")
else:
    print("No es primo")
print("Programa terminado")
