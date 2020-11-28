
#Tenemos la siguiente variable definida en nuestro programa:
#temperaturas='''
#	Utrera,29,12
#	Dos Hermanas,32,14
#	Sevilla,30,15
#	Alcalá de Guadaíra,31,14
#'''
#En esa cadena se definen nombres de poblaciones y las temperaturas máximas y mínimas de dichas poblaciones durante un día.
#Realiza un programa que muestre el nombre de las poblaciones y la temperatura media.
#Además el programa te debe pedir el nombre de una población y
#nos debe dar la temperatura máxima y mínima (si la población no existe se debe dar une error.)

cadena1 = '''
Utrera,29,12
Dos Hermanas,32,14
Sevilla,30,15
Alcalá de Guadaíra,31,14
'''
lista = cadena1.splitlines()
for i in range(0,len(lista)):
    if i > 0:
        print("Población:",lista[i].split(",")[0],". Temperatura media:",(int(lista[i].split(",")[1]) + int(lista[i].split(",")[2]))/2)

pob = str(input("Introduzca una población a su elección: ")).capitalize()
if pob not in cadena1:
    print("¡ERROR! La población escogida no está recogida.")
else:
    for i in range(0,len(lista)):
        if pob == lista[i].split(",")[0]:
            print("Población:",pob,". Temperatura máxima:",lista[i].split(",")[1],". Temperatura mínima:",lista[i].split(",")[2])
