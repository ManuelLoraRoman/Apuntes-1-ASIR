
#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
#El tiempo de viaje hasta llegar a otra ciudad B es de T segundos.
#Escribir un algoritmo que determine la hora de llegada a la ciudad B.

HH = int(input("Dime la hora de partida:"))
MM = int(input("Dime los minutos de partida:"))
SS = int(input("Dime los segundos de partida:"))
T = int(input("Dime los segundos en llegar a la ciudad B:"))

print("La hora de partida de la ciudad A es:",HH,":",MM,":",SS,".")

seginicial = HH * 3600 + MM * 60 + SS
total = seginicial + T

horallegada = total // 3600
minllegada = (total % 3600) // 60
segllegada = (total % 3600) % 60

print("La hora de llegada a la ciudad B será:",horallegada,":",minllegada,":",segllegada,".")
