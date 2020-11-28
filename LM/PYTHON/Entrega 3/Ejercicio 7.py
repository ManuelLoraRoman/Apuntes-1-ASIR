#Realizar una aplicación que recoja por teclado la cantidad total a pagar y la cantidad que se ha entregado.
#La aplicación debe calcular el cambio correspondiente con el menor número de monedas y/o billetes posibles.
#Por ejemplo:
	#Cantidad total: 7,17 €
	#Cantidad entregada: 100 €
	#Cantidad a devolver: 92,83 €
	#1 billete de 50 €
	#2 billete de 20 €
	#1 monedas de 2 €
	#1 monda de 50 c
	#1 moneda de 20 c
	#1 moneda de 10 c
	#1 moneda de 2 c
	#1 moneda 1 c



print("PAGOS Y CAMBIOS")

valores = [500,200,100,50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]

canttotal = float(input("Cantidad total a pagar: "))
cantentr = float(input("Cantidad entregada: "))
cantdev = cantentr - canttotal
print("Cantidad total:",canttotal,"€\nCantidad entregada:",cantentr,"€\nCantidad a devolver:",cantdev,"€")

for valor in valores:
    if valor > 2:
        if int(cantdev / valor) == 1:
            print("1 Billete de %d €"% valor)
        elif cantdev / valor > 1:
            print("%d Billetes de %d €"%((cantdev / valor),valor))
    elif valor <= 2 and valor >=1:
        if int(cantdev / valor) == 1:
            print("1 moneda de %d €"% valor)
        elif cantdev / valor > 1:
            print("%d monedas de %d €"%((cantdev / valor),valor))
    elif valor < 1:
        if int(cantdev / valor) == 1:
            print("1 moneda de %.2f c"% valor)
        elif cantdev / valor > 1:
            print("%d monedas de %.2f c"%((cantdev / valor),valor))
    cantdev = cantdev % valor
