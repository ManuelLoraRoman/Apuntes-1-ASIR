
#Una compañía de transporte internacional tiene servicio en algunos países de América del Norte, América Central, América del Sur, Europa y Asia.
#El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido. Lo anterior se muestra en la tabla:
#Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de logística y de seguridad.
#Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.
#Zona
#Ubicación
#Costo/gramo
#1
#América del Norte
#24.00 euros
#2
#América Central
#20.00 euros
#3
#América del Sur
#21.00 euros
#4
#Europa
#10.00 euros
#5
#Asia
#18.00 euros

peso = int(input("Peso del paquete:"))
zona = int(input("Dime la zona a la que vas:"))

if peso > 5 or peso < 0:
    print("Paquete rechazado.")
else:
    if zona == 1:
        print("El precio de la entrega sería de", 24 * peso,"€.")
    else:
        if zona == 2:
            print("El precio de la entrega sería de", 20 * peso,"€.")
        else:
            if zona == 3:
                print("El precio de la entrega sería de", 21 * peso,"€.")
            else:
                if zona == 4:
                    print("El precio de la entrega sería de", 10 * peso,"€.")
                else:
                    print("El precio de la entrega sería de", 18 * peso,"€.")
