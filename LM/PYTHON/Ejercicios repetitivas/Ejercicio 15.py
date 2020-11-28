
#Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €,
#el segundo 20 €, el tercero 40 € y así sucesivamente.
#Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total de
#lo que pagó después de los 20 meses.

precio = 70
for i in range(4,21):
    precio = precio + 20
    print("En el mes nº",i,"tiene que pagar 20 €.")
print("Al final de los 20 meses tiene que pagar",precio,"€.")
