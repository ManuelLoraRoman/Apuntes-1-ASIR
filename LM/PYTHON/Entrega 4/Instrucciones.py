#Necesitamos que se facture el uso de un teléfono.
#Nos informarán de la tarifa por segundo (en céntimos), cuántas comunicaciones se realizaron,
#la duración de cada comunicación expresada en horas, minutos y segundos.
#Como resultado deberemos informar la duración en segundos de cada comunicación y su costo.

#Vamos a dividir este problemas en problemas más pequeños:

    #Cada comunicación se expresa en horas, minutos y segundos, la tarifa es € por segundos,
    #por lo tanto lo primero que vamos a solucionar es convertir las horas, minutos y segundos en segundos.
    #Para ello vamos a crear una función llamada pasar_a_segundos.
    #Piensa los parámetros de entrada que tiene esta función yel valor que devuelve. ¿De qué tipo son?
    #Una vez que sabemos los segundos que ha tardado una comunicación y la tarifa por segundo
    #vamos a crear una función llamada calcular_coste que nos calcule cuanto cuesta, en céntimos, la llamada.
    #Piensa los parámetros y el valor devuelto de la función.
    #Por último vamos a crear una función para convertir el coste en céntimos, en una cantidad de dinero expresada en euros y céntimos.
    #Para ello creamos la función convertir_a_euros. Piensa los parámetros de entrada y los valores devueltos.
