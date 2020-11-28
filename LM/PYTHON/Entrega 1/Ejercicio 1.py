
#Escriba un programa que pida dos números enteros y que calcule su división,
#escribiendo si la división es exacta o no. Se puede mejorar el programa haciendo que tenga en cuenta que no se puede dividir por cero.

#DIVISOR DE NÚMEROS
#Escriba el dividendo: 14
#Escriba el divisor: 5
#La división no es exacta. Cociente: 2 Resto: 4

#DIVISOR DE NÚMEROS
#Escriba el dividendo: 20
#Escriba el divisor: 4
#La división es exacta. Cociente: 5

print("DIVISOR DE NÚMEROS")
divi = int(input("Escriba el dividendo: "))
divs = int(input("Escriba el divisor: "))
if divs == 0:
    print("No se puede dividir entre cero")
elif divi % divs != 0:
    print("La división no es exacta. Cociente:", divi // divs," Resto:", divi % divs)
elif divi % divs == 0:
    print("La división es exacta. Cociente:",divi // divs)
