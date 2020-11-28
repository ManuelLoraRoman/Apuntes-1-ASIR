
#La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual se clasifica en tipos A y B, y además en tamaños 1 y 2.
#Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño,
#se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo A,
#se le cargan 20 céntimos al precio inicial cuando es de tamaño 1;
#y 30 céntimos si es de tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1,
#y 50 céntimos cuando es de tamaño 2.  Realice  un  algoritmo  para  determinar  la  ganancia  obtenida.

kilo = int(input("Dime los kilos comprados:"))
precio = int(input("Dime el precio por kg:"))
tipo = input("Dime el tipo de uva (A o B):")
tam = int(input("Dime el tamaño de uva (1 o 2):"))

if tipo == "A" and tam == 1:
    ganancia = kilo * 0.2
    ganancia = ganancia * precio
    print("La ganancia por la venta sería de",ganancia,"€.")
else:
    if tipo == "A" and tam == 2:
        ganancia = kilo * 0.3
        ganancia = ganancia * precio
        print("La ganancia por la venta sería de",ganancia,"€.")
if  tipo == "B" and tam == 1:
    ganancia = precio - 0.3
    ganancia = ganancia * kilo
    print("La ganancia por la venta sería de",ganancia,"€.")
else:
    if tipo == "B" and tam == 2:
        ganancia = precio - 0.5
        ganancia = ganancia * kilo
        print("La ganancia por la venta sería de",ganancia,"€.")
