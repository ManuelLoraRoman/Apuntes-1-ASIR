
#Utilizando el fichero notas.csv, realiza un programa en python que lea los datos de ese fichero y construya la siguiente estructura:
#alumnos = [ {"nombre":"Daniel", "apellidos":"Fustero López", "curso": "1A","notas":{"FH":3,"LM":4,"ISO":5,"FOL":6,"PAR":7,"SGBG":6}},
#            {"nombre":"Rafaela", ... },...]
#Crea un programa que muestre un menú y puedas elegir una de estas opciones:
    #Muestra el listado de los alumnos con la nota media que han sacado. Utiliza una función para realizar el cálculo de la nota media.
    #Pide un curso y una asignatura y muestre una lista de los alumnos de ese curso con las notas en esa asignatura.
    #Pide un curso y muestre el porcentaje de aprobados por cada asignatura.
    #Pide un curso, y crea un fichero nombredelcurso.txt con los alumnos y la nota media.

def calcular_media(notas):
    media = (int(notas["FH"]) + int(notas["LM"]) + int(notas["ISO"]) + int(notas["FOL"]) + int(notas["PAR"]) + int(notas["SGBG"])) / 6
    return media

alumnos = []
with open("notas.txt",encoding="utf-8") as fichero:
    i = 0
    for linea in fichero:
        if i > 0:
            nombrealum = linea.split(",")[1]
            apellidos = linea.split(",")[0]
            curso = linea.split(",")[2]
            fh = linea.split(",")[3]
            lm = linea.split(",")[4]
            iso = linea.split(",")[5]
            fol = linea.split(",")[6]
            par = linea.split(",")[7]
            sgbg = linea.split(",")[8]
            dic = {"Nombre":nombrealum,"Apellidos":apellidos,"Curso":curso,"Notas":{"FH":fh,"LM":lm,"ISO":iso,"FOL":fol,"PAR":par,"SGBG":sgbg.strip("\n")}}
            alumnos.append(dic.copy())
            dic.clear()
        i = i + 1
    print(alumnos)
while True:
    opcion = int(input("\nElija una opción:\n1. Listado de notas medias\n2. Notas asignatura concreta\n3. Porcentaje de aprobados del curso\n4. Creación archivo de notas medias\n5. Salir\nRespuesta: "))
    if opcion == 1:
        for i in range(0,len(alumnos)):
            print(alumnos[i]["Apellidos"],",",alumnos[i]["Nombre"],".Media:",calcular_media(alumnos[i]["Notas"]))
    elif opcion == 2:
        cursopedido = str(input("Dime un curso: "))
        asigpedido = str(input("Dime una asignatura: "))
        for i in range(0,len(alumnos)):
            if alumnos[i]["Curso"] == curso:
                print(alumnos[i]["Apellidos"],",",alumnos[i]["Nombre"],". Notas:",alumnos[i]["Notas"][asigpedido])
    elif opcion == 3:
        print("No realizado")
    elif opcion == 4:
        cursopedido = str(input("Dime un curso: "))
        f = open(curso,"w")
        for i in range(0,len(alumnos)):
            if alumnos[i]["Curso"] == curso:
                f.write(alumnos[i]["Apellidos"])
                f.write(",")
                f.write(alumnos[i]["Nombre"])
                f.write(". Nota Media: ")
                f.write(str(calcular_media(alumnos[i]["Notas"])))
                f.write("\n")
        print("Archivo creado")
        f.close()
    elif opcion == 5:
        print("Programa terminado")
        break;
