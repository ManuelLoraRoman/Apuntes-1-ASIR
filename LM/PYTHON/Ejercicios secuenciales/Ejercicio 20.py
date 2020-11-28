
#Diseñar un algoritmo que nos diga el dinero que tenemos
#(en euros y céntimos) después de pedirnos cuantas monedas
#tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).


eur2 = int(input("¿Cuántas monedas de 2€ tienes? "))
eur1 = int(input("¿Cuántas monedas de 1€ tienes? "))
eur50 = int(input("¿Cuántas monedas de 50 céntimos tienes? "))
eur20 = int(input("¿Cuántas monedas de 20 céntimos tienes? "))
eur10 = int(input("¿Cuántas monedas de 10 céntimos tienes? "))

totaleuros = eur2 * 2 + eur1
totalcentimos = eur50 * 50 + eur20 * 20 + eur10 * 10
totaleuros = totaleuros + (totalcentimos // 100)
totalcentimos = totalcentimos % 100

print("Tienes en total",totaleuros,"euros y",totalcentimos,"céntimos.")
