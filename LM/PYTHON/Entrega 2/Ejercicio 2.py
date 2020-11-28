
#Escribe una programa que pida una cadena de caracteres y diga si no tiene caracteres repetidos.

print("Repetición de caracteres:")

se_repite = False
cadena = input("\nDame una cadena: ")
for i in range(0,len(cadena)):
    if cadena.count(cadena[i]) > 1:
        se_repite = True
if se_repite:
    print("Se repite algún caracter.")
else:
    print("No se repite ningún caracter.")
