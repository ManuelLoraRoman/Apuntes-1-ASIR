
#Realizar un algoritmo para determinar cuánto ahorrará una persona en un año,
#si al final de cada mes deposita cantidades variables de dinero; además, se quiere saber cuánto lleva ahorrado cada mes.

din = 0
total = 0
for i in range(1,13):
    din = int(input(f"Dinero en el mes {i}: "))
    total = total + din
    print("Llevas ahorrado con el mes",i,"un total de:",total,".")
print("El dinero ahorrado en el año será de",total,"€.")
