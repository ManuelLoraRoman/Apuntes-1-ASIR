
#Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. Si introducimos otro número nos da un error.

dia = int(input("Dime el día de la semana:"))

if dia > 7 or dia < 0:
    print("ERROR")
else:
    if dia == 1:
        print("El día es Lunes.")
    else:
        if dia == 2:
            print("El día es Martes.")
        else:
            if dia == 3:
                print("El día es Miércoles.")
            else:
                if dia == 4:
                    print("El día es Jueves.")
                else:
                    if dia == 5:
                        print("El día es Viernes.")
                    else:
                        if dia == 6:
                            print("El día es Sábado.")
                        else:
                            if dia == 7:
                                print("El día es Domingo.")
