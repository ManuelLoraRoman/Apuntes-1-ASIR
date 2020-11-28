
#Utilizando el ejercicio anterior, crea una aplicación simple de craqueo de contraseñas utilizando
#los ficheros que puedes encontrar en el repositorio.

from crypt import crypt

usuario = str(input("Usuario: "))
contraseña = str(input("Contraseña: "))
with open("/etc/shadow","r") as fichero:
    lineas = fichero.readlines()
    for linea in lineas:
        if linea.split(":")[0] == usuario:
            sol = crypt(contraseña,linea.split(":")[1][0-11])
            if sol == linea.split(":")[1]:
                print("El usuario es válido.")
            else:
                print("El usuario no es válido.")
