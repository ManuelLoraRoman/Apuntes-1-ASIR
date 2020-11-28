
#Escribir dos funciones que permitan calcular:

    #La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
    #La cantidad de horas, minutos y segundos de un tiempo dado en segundos.

import re

def cantidad_seg(tiempo):

    hh = int(tiempo.split(":")[0])
    mm = int(tiempo.split(":")[1])
    ss = int(tiempo.split(":")[2])
    S = "La cantidad de segundos será de " + str((hh * 3600) + (mm * 60) + ss) + " segundos."
    return S

def cantidad_tiempo(segundos):

    hh = segundos // 3600
    mm = (segundos%3600) // 60
    ss = segundos%60
    tiempo = "Los segundos serán en total " + str(hh) + ":" + str(mm) + ":" + str(ss) + "."
    return tiempo

print("Comprobación 1ª función:")

tiempo = str(input("Dame un tiempo: "))
patron = re.compile('[0-9]{2}:[0-9]{2}:[0-9]{2}')
while True:
    if patron.search(tiempo):
        print(cantidad_seg(tiempo))
        break;
    else:
        tiempo = str(input("El tiempo introducido no es correcto. Debe seguir la estructura HH:MM:SS"))

print("Comprobación 2ª función:")

segundos = int(input("Dame una cantidad de segundos: "))
print(cantidad_tiempo(segundos))
