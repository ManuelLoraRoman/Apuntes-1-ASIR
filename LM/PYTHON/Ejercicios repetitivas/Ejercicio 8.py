
#Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
#A continuación se van introduciendo números hasta que introduzcamos el 0.
#Cuando termine el programa dará las siguientes informaciones:

#La suma de los números que están dentro del intervalo (intervalo abierto).
#Cuantos números están fuera del intervalo.
#He informa si hemos introducido algún número igual a los límites del intervalo.

liminf = int(input("Dime el límite inferior: "))
limsup = int(input("Dime el límite superior: "))

while liminf > limsup:
    liminf = int(input("El limite inferior debe ser menor que el limite superior. Escribalo de nuevo: "))
n = 1
s = 0
f = 0
es_igual = False
while n != 0:
    n = int(input("Escriba un número: "))
    if n > liminf and n < limsup:
        s = s + n
    elif n == liminf or n == limsup:
        es_igual = True
    elif n < liminf or n > limsup:
        f = f + 1
print("La suma de los números dentro del intervalo es:",s,".\nNº fuera del intervalo:",f,".")
if es_igual:
    print("Ha introducido un número igual a alguno de los límites del intervalo.")
