
#El Código Cuenta Cliente (CCC) es el código que identifica en España las cuentas corrientes de los clientes de bancos.
#El CCC tiene 20 dígitos en formato AAA-BBBB-CCC-DDDDDDDDDD.
    #AAAA son cuatro dígitos que identifican la entidad bancaria.
    #BBBB son cuatro dígitos que identifican la oficina.
    #CC se denomina dígito de control (DC).
    #DDDDDDDDDD son 10 dígitos de la cuenta del cliente en el banco.
#Según la Wikipedia: Los dígitos situados en las posiciones novena y décima se generan a partir de los demás dígitos del CCC,
#permitiendo comprobar la validez del mismo y reducir la posibilidad de errores de manipulación.
#El primero de ellos valida conjuntamente los códigos de entidad y de oficina; el segundo, valida el número de cuenta.
#Cada uno de los dígitos del DC se calcula utilizando el mismo algoritmo, para lo que se complementa con dos ceros a la izquierda la entidad y oficina.
#La siguiente función en Python calcula el DC correspondiente para una lista de 10 número enteros:
    #def calcula_dc(lista):
    #"""Calcula el dígito de control de una CCC.
    #Recibe una lista con 10 numeros enteros y devuelve el DC
    #correspondiente"""
    #pesos = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6]
    #aux = []
    #for i in range(10):
    #	aux.append(lista[i]*pesos[i])
    #resto = 11 - sum(aux) %11
    #if resto == 10:
    #	return 1
    #elif resto == 11:
    #	return 0
    #else:
    #	return resto
    #
    #Por ejemplo:
    #
    #>>> lista = [1, 6, 7, 0, 0, 0, 0, 3, 3, 2]
    #>>> calcula_dc(lista)
    #5
#Escribe un programa que pida al usuario un CCC en el formato arriba indicado y compruebe su validez.
#Mejora: Además de decirte si el número de cuenta es válido, te tiene que mostrar el nombre de la identidad bancaria que leerá del fichero bancos.txt.

import re

def calcula_dc(lista):
    pesos = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6]
    aux = []
    for i in range(10):
        aux.append(lista[i]*pesos[i])
    resto = 11 - sum(aux) %11
    if resto == 10:
	    return 1
    elif resto == 11:
        return 0
    else:
        return resto

lista1 = []
lista2 = []
print("CÓDIGO CUENTA CLIENTE")

CCC = str(input("Introduzca un CCC para comprobar su validez: "))
patron = re.compile('[0-9]{4}-[0-9]{4}-[0-9]{2}-[0-9]{10}')

while True:
    if patron.search(CCC):

        A = str(CCC.split("-")[0])

        with open("bancos.txt",encoding="utf-8") as fichero:
            for linea in fichero:
                if linea.split(",")[0] == A:
                    print("La entidad bancaria introducida sería",linea.split(",")[1])
        B = str(CCC.split("-")[1])
        AyB = A + B + "00"
        for i in range(0,len(AyB)):
            lista1.append(int(AyB[i]))
        DC1 = calcula_dc(lista1)

        D = str(CCC.split("-")[3])
        for i in range(0,len(D)):
            lista2.append(int(D[i]))
        DC2 = calcula_dc(lista2)

        DC = str(CCC.split("-")[2])
        if int(DC[0]) == DC1 and int(DC[1]) == DC2:
            print("El CCC introducido es válido")
        else:
            print("El CCC introducido no es válido")
        break;
    else:
        CCC = str(input("El patrón del CCC es incorrecto.\nDebe tener la estructura AA-BBBB-CC-DDDDDDDDDD.\nIntroduzca otra: "))
