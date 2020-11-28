
#Una dirección 6to4 es una dirección IPv6 reservada para equipos que tienen actualmente una dirección IPv4 pública. Un ejemplo de dirección 6to4 sería:

 #2002:503b:198:0:219:66ff:fea8:db3

#El campo 2002: es fijo y el bloque importante para esta discusión es el que determina la parte de red de la dirección
#es decir, los campos 503b:198 que son la representación hexadecimal de la dirección IPv4 correspondiente:

 #80.59.1.152 = 0x50.0x3b.0x1.0x98 = 503b:198  --> pasar a Hexadecimal

#el resto de campos se corresponden con la dirección de subred y la dirección de host, y no son relevantes para este ejercicio.

#Escribe un programa que pida una dirección IPv4 pública y nos dé la parte de red correspondiente de la dirección 6to4 asociada:

#Ejemplo:

 #Dame una dirección IPv4 publica: 85.135.34.12
 #La parte de red 6to4 correspondiente es: 2002:5587:220

cadena = ""
ipv4 = str(input("Dame una dirección IPv4 publica: "))
lista = ipv4.split(".")
print("Tu dirección IPv4 sería ",lista)
for i in lista:
    if int(i) // 16 != 0:
        cociente = str(int(i) // 16)
        resto = str(int(i) % 16)
    if int(cad) < 16 :
        if cad == "10":
            cad = "a"
        elif cad == "11":
            cad = "b"
        elif cad == "12":
            cad = "c"
        elif cad == "13":
            cad = "d"
        elif cad == "14":
            cad = "e"
        elif cad == "15":
            cad = "f"
    if int(i) % 16 < 16:
        if i == "10":
            cad = cad + "a"
        elif i == "11":
            cad = cad + "b"
        elif i == "12":
            cad = cad + "c"
        elif i == "13":
            cad = cad + "d"
        elif i == "14":
            cad = cad + "e"
        elif i == "15":
            cad = cad + "f"
        cadena = cadena + cad
    if lista[1] == i:
        cadena = cadena + ":"
print(cadena)
