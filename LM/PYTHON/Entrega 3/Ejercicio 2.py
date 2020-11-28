
#Implementa un sistema completo de validación de usuarios en una máquina con Debian, que tiene las siguientes características:
    #El nombre de usuario y las contraseñas se almacenan en el fichero /etc/shadow, al que tiene acceso sólo el usuario root.
    #Las contraseñas se almacenan como un hash AES512 con sal
#Supongamos que tenemos en nuestro sistema el usuario prueba con contraseña asdasd, una línea correspondiente
#a este usuario en el fichero /etc/shadow sería:
#prueba:$6$/nNkCgcv$r.FooJSMDwP2gd4MAsoRTTLoOVpsIF2EyxW59ryWW7bpKUxulWX9CpEWknaDBzHWYJ2q9gqxEyfQl93u7okPa.:15059:0:99999:7::::
    #La sal de una contraseña cifrada se indica en linux por los 12 primeros caracteres del hash de la contraseña,
    #en el caso anterior la sal sería $6$/nNkCgcv$.
    #La función crypt del módulo crypt permite formar los hashes con sal utilizados por linux, de la siguiente manera:
      #>>> from crypt import crypt
      #>>> crypt('asdasd','$6$/nNkCgcv$')
      #'$6$/nNkCgcv$r.FooJSMDwP2gd4MAsoRTTLoOVpsIF2EyxW59ryWW7bpKUxul\WX9CpEWknaDBzHWYJ2q9gqxEyfQl93u7okPa.'
#donde asdasd es la contraseña en claro.
#Escribe un programa que lea un usuario y una contraseña, y te informe si el usuario es válido o no.

from crypt import crypt

usuario = str(input("Usuario: "))
contraseña = str(input("Contraseña: "))
with open("shadow",encoding="utf-8") as fichero:
    lineas = fichero.readlines()
    for linea in lineas:
        if linea.split(":")[0] == usuario:
            sol = crypt.crypt(contraseña,linea.split(":")[1][0-11])
            if sol == linea.split(":")[1]:
                print("El usuario es válido.")
            else:
                print("El usuario no es válido.")
