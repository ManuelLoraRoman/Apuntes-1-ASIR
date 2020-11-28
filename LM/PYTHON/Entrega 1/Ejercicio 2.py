
#Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año
#o cuántos años faltan para llegar a ese año.
#Se puede mejorar el programa haciendo que cuando la diferencia sea exactamente un año y escriba la frase en singular.

#COMPARADOR DE AÑOS
#¿En qué año estamos?: 2015
#Escriba un año cualquiera: 2020
#Para llegar al año 2020 faltan 5 años.

#COMPARADOR DE AÑOS
#¿En qué año estamos?: 2015
#Escriba un año cualquiera: 1997
#Desde el año 1997 han pasado 18 años.

#COMPARADOR DE AÑOS
#¿En qué año estamos?: 2015
#Escriba un año cualquiera: 2015
#¡Son el mismo año!


print("COMPARADOR DE AÑOS")
anyoac = int(input("¿En qué año estamos?: "))
anyo = int(input("Escriba un año cualquiera: "))
if anyoac < anyo and anyo - anyoac == 1:
    print("Para llegar al año",anyo,"falta 1 año exactamente.")
elif anyoac > anyo and anyoac - anyo == 1:
    print("Desde el año",anyo,"ha pasado exactamente 1 año.")
elif anyoac < anyo:
    print("Para llegar al año",anyo,"faltan",anyo - anyoac,"años.")
elif anyo < anyoac:
    print("Desde el año",anyo,"han pasado",anyoac - anyo,"años.")
elif anyo == anyoac:
    print("¡Son el mismo año!")
