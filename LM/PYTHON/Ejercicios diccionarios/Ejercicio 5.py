
#Escribir un programa que implemente una agenda.
#En la agenda se podrán guardar nombres y números de teléfono. El programa nos dará el siguiente menú:
#Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda,
# debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
# Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
#Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
#Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
#Listar: Nos muestra todos los contactos de la agenda.
#Implementar el programa con un diccionario.

diccionario = {"Manuel Lora Román":661152395,"Fran Madueño":651127833,"Fernando Pérez": 644444444}
repite = True
print("AGENDA")
while repite:
    opcion = str(input("\n|Añadir / Modificar|\n|Buscar|\n|Borrar|\n|Listar|\n\nOpción: "))
    if opcion.capitalize() == "Añadir" or opcion.capitalize() == "Modificar":
        nombre = str(input("Dame un nombre: "))
        if nombre in diccionario:
            print("Su número de teléfono es:",diccionario[nombre],"¿Es correcto?")
            corr = str(input("(S/N): "))
            if corr.upper() == "N":
                nummod = int(input("Dame un nº nuevo para sustituirlo: "))
                diccionario[nombre] = nummod
            elif corr.upper() == "S":
                print("Número no modificado.")
        else:
            numnuevo = int(input("Dame un nº nuevo para añadir: "))
            diccionario[nombre] = numnuevo
    if opcion.capitalize() == "Buscar":
        busqueda = str(input("Dime un nombre a buscar: "))
        print("CONTACTOS")
        for i in diccionario.keys():
            if i == busqueda:
                print("-",i,". Nº de contactos: ",diccionario[i])
    if opcion.capitalize() == "Borrar":
        borrador = str(input("Dame un nombre para borrar: "))
        del(diccionario[borrador])
    if opcion.capitalize() == "Listar":
        print("El listado de contactos:")
        for i in diccionario.keys():
            print("Nombre: ",i,".")
    bool = str(input("¿Quieres hacer otra operación?(S/N)"))
    if bool.upper() == "N":
        repite == False
        print("Programa Finalizado.")
        break;
