#Necesitamos que se facture el uso de un teléfono.
#Nos informarán de la tarifa por segundo (en céntimos), cuántas comunicaciones se realizaron,
#la duración de cada comunicación expresada en horas, minutos y segundos.
#Como resultado deberemos informar la duración en segundos de cada comunicación y su costo.

#Vamos a dividir este problemas en problemas más pequeños:

    #Cada comunicación se expresa en horas, minutos y segundos, la tarifa es € por segundos,
    #por lo tanto lo primero que vamos a solucionar es convertir las horas, minutos y segundos en segundos.
    #Para ello vamos a crear una función llamada pasar_a_segundos.
    #Piensa los parámetros de entrada que tiene esta función y el valor que devuelve. ¿De qué tipo son?
    #Una vez que sabemos los segundos que ha tardado una comunicación y la tarifa por segundo
    #vamos a crear una función llamada calcular_coste que nos calcule cuanto cuesta, en céntimos, la llamada.
    #Piensa los parámetros y el valor devuelto de la función.
    #Por último vamos a crear una función para convertir el coste en céntimos, en una cantidad de dinero expresada en euros y céntimos.
    #Para ello creamos la función convertir_a_euros. Piensa los parámetros de entrada y los valores devueltos.

    #Crea un programa que te pregunte por teclado la tarifa por segundos en céntimos,
    #el número de comunicaciones que se han realizado, y te vaya pidiendo horas, minutos y segundo
    #que han durado cada una de las comunicaciones.
    #Finalmente te mostrará cuanto ha costado cada una de las comunicaciones
    #y el total de dinero de todas las comunicaciones.

import re

def pasar_a_segundos(duracion):

    hh = int(duracion.split(":")[0])
    mm = int(duracion.split(":")[1])
    ss = int(duracion.split(":")[2])
    S = 0
    S = hh * 3600 + mm * 60 + ss
    return S

def calcular_coste(segundos,tarifa):

    coste = segundos * (tarifa * 0.1)
    return round(coste,2)

def convertir_a_euros(coste):

    euros = coste // 100
    return euros

lista = []
tarifa = float(input("Dime la tarifa por segundos de las comunicaciones: "))
numero = int(input("Nº de comunicaciones realizadas: "))
for i in range(1,numero + 1):
    duracion = str(input(f"Dime la duración de la {i}º comunicación: "))
    patron = re.compile('[0-9]{2}:[0-9]{2}:[0-9]{2}')
    while True:
        if patron.search(duracion):
            segundos = pasar_a_segundos(duracion)
            coste = calcular_coste(segundos,tarifa)
            euros = convertir_a_euros(coste)
            lista.append(euros)
            print(f"El coste en euros de la {i}º comunicación es de",euros,"€ y",int(euros%100),"cent.")
            break;
        else:
            duracion = str(input("¡ERROR! La duración no tiene la estructura correcta de HH:MM:SS. Introduzca otra: "))

total = 0
for i in range(0,len(lista)):
    total = total + lista[i]
print("El coste total de todas las comunicaciones sería de",total,"€ y",int(total%100),"cent.")
