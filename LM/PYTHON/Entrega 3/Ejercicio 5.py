
#Descarga el fichero zips.json del sitio de mongodb. Se trata de un listado de los códigos postales de EEUU en formato JSON
#(lo que Python denomina diccionarios y listas). Realiza los siguientes ejercicios:
    #Cuenta el número de códigos postales que aparecen
    #Cuenta el número de códigos postales de cada estado
    #Obtén la URL del mapa de OpenStreetMap de la ciudad de “Akaska” en el estado de Dakota del Sur (SD).
    #Nota: Las coordenadas que aparecen en el fichero zips.json vienen en formato [longitud,latitud] y la url genérica que utiliza OpenStreetMap es:
    #http://www.openstreetmap.org/#map=zoom/latitud/longitud
#Por ejemplo:
#http://www.openstreetmap.org/#map=19/37.27058/-5.91958 para ver con un zoom de nivel 19 la ubicación con latitud 37.27058 y longitud -5.91958
#Modifica el programa anterior para que ahora se pida por teclado la ciudad y el estado que se quiere localizar en OpenStreetMap.
#El programa te pide una ciudad, si existe te devuelve la URL.

datoscodigos = []
with open("zips.json",encoding="utf-8") as fichero:
    print("Hay un total de",len(fichero.readlines()),"códigos postales.")
    fichero.seek(0)
    for linea in fichero:

        id = linea.split(",")[0]
        id1 = id.split(":")[1]

        ciudad = linea.split(",")[1]
        ciudad1 = ciudad.split(":")[1]
        ciudad1 = ciudad1.replace('"',"").replace(" ","")

        loc = linea.split(",")[2]
        loc1 = loc.split(":")[1]
        loc2 = linea.split(",")[3]
        loc3 = loc2.split(":")[0]
        locf = loc1 + "," + loc3

        pop = linea.split(",")[4]
        pop1 = pop.split(":")[1]

        estado = linea.split(",")[5]
        estado1 = estado.split(":")[1]

        dic = {"ID":id1,"Ciudad":ciudad1,"Localización":locf,"Pop":pop1,"Estado":estado1.replace(" }\n","")}
        datoscodigos.append(dic.copy())
        dic.clear()

    contador = {}
    for i in range(0,len(datoscodigos)):
        if datoscodigos[i]["Estado"] in contador:
            contador[datoscodigos[i]["Estado"]] += 1
        else:
            contador[datoscodigos[i]["Estado"]] = 1

    for clave,valor in contador.items():
        print("El nº de Códigos Postales en el estado",clave.replace(" ","").replace('"',""),"es de",valor)

    print("-----------------------------------------------------------------")

    opcion = str(input("¿Desea hacer una búsqueda de alguna ciudad?(SI/NO) "))
    while True:
        if opcion.upper() == "SI":
            ciu = str(input("Dime una ciudad: "))
            est = str(input("Dime un estado: "))
            for i in range(0,len(datoscodigos)):
                if datoscodigos[i]["Ciudad"] == ciu.upper() and datoscodigos[i]["Estado"].replace(" ","").replace('"',"") == est.upper():
                    part1 = "http://www.openstreetmap.org/#map=19/"
                    part2 = datoscodigos[i]["Localización"]
                    partall = part1 + part2.split(",")[0].replace(" ","").replace("[","") + "/" + part2.split(",")[1].replace(" ","").replace("]","")
                    print("La URL sería",partall,".")
            opcion = str(input("¿Desea hacer otra búsqueda? "))
        elif opcion.upper() == "NO":
            print("Programa terminado")
            break;
        else:
            print("Introducido valor incorrecto")
            opcion = str(input("¿Desea hacer otra búsqueda? "))
