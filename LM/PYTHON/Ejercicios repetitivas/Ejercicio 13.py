
#Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la semana (seis días)
#y requiere determinar el total de éstas, así como el sueldo que recibirá por las horas trabajadas.

horas = 0
din = int(input("Euros por hora trabajada: "))
for i in range(1,7):
    h = int(input(f"Nº de horas trabajadas en el día {i}: "))
    horas = horas + h
print("Total de horas trabajadas:",horas,".\nSueldo:",horas * din,".")
