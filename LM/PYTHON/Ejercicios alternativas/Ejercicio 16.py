
#La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el tiempo que ésta dura,
#de tal forma que los primeros cinco minutos cuestan 1 euro, los siguientes tres,
#80 céntimos,  los  siguientes  dos  minutos,  70 céntimos,  y  a  partir  del  décimo  minuto, 50 céntimos.
#Además,  se  carga  un  impuesto  de  3  %  cuando  es  domingo,
#y  si  es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %.
#Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona  que  realiza  una  llamada.

min = int(input("Minutos consumidos en la llamada:"))
dia = input("Dime el dia que llamastes:")
turno = input("Dime si era turno de mañana(m) o de tarde(t):")

if min == 5:
    precio = 1
if min == 8:
    precio = 1.8
else:
    if min == 10:
        precio = 2.5
    else:
        precio = 3

if dia == "domingo" or dia == "Domingo":
    print("Tienes que pagar",precio + ((precio * 3)/100),"€.")
else:
    if turno =="m":
        print("Tienes que pagar",precio + ((precio * 15)/100),"€.")
    else:
        print("Tienes que pagar",precio + ((precio * 10)/100),"€.")
