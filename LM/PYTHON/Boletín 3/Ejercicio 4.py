
#Escribe un programa que pida al usuario su fecha de nacimiento y le responda el día de la semana correspondiente
#(para ello debes utilizar la función adecuada del módulo calendar). Ejemplo:

#Ejemplo:

 #Introduce tu fecha de nacimiento (DD-MM-YYYY): 29-02-1992
 #Naciste en sabado

import calendar

cadena = str(input("Introduzca tu fecha de nacimiento (DD-MM-YYYY): "))
lista1 = cadena.split("-")
fecha = calendar.weekday(int(lista1[2]),int(lista1[1]),int(lista1[0]))
if fecha == 0:
    print("Naciste en Lunes")
elif fecha == 1:
    print("Naciste en Martes")
elif fecha == 2:
    print("Naciste en Miércoles")
elif fecha == 3:
    print("Naciste en Jueves")
elif fecha == 4:
    print("Naciste en Viernes")
elif fecha == 5:
    print("Naciste en Sábado")
else:
    print("Naciste en Domingo")
