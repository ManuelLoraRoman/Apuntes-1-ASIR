
#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

dia = int(input("Dime un día:"))
mes = int(input("Dime un mes:"))
anyo = int(input("Dime un año:"))
print("Fecha:",dia,"/",mes,"/",anyo,".")


if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia > 31 or dia < 0:
        print("La fecha introducida es incorrecta.")
    else:
        print("Fecha correcta.")
if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia > 30 or dia < 0:
        print("La fecha introducida es incorrecta.")
    else:
        print("Fecha correcta.")
if mes == 2:
    if (dia > 28 and ((anyo % 4 != 0 and anyo % 100 != 0) or (anyo % 4 != 0 and anyo % 100 != 0 and anyo % 400 != 0))) or dia < 0:
        print("La fecha introducida es incorrecta.")
    else:
        print("Fecha correcta.")
