
#Realiza un programa que pida un cadena. A continuación debe pedir otra cadena.
#El programa debe buscar la segunda cadena en la primera (ignorando mayúsculas o minúsculas)
#y podrá responder una de las siguientes opciones:
    #La segunda cadena es una subcadena de la primera
    #La segunda cadena no es una subcadena de la primera
#Ejemplo:
#Cadena 1: Java es un lenguaje de programación
#Cadena 2: LENGUAJE
#Respuesta:
#La segunda cadena es una subcadena de la primera

cadena1 = input("Cadena 1: ")
cadena2 = input("Cadena 2: ")
print("Respuesta:")
if cadena1.find(cadena2):
    print("La segunda cadena es una subcadena de la primera.")
else:
    print("La segunda cadena no es una subcadena de la primera.")
