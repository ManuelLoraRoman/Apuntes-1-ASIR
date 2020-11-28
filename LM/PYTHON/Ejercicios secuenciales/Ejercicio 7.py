
#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
#Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

minutos = int(input("Dime una cantidad de minutos:"))

resto = minutos % 60;

print("Los minutos dados corresponden a", minutos // 60 ,"horas y",resto,"minutos.")
