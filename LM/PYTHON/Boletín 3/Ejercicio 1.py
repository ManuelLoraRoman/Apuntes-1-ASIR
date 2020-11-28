#Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol. Para ello vamos a utilizar dos listas:

    #Equipos: Que es una lista cuyos elementos son una lista con el nombre de los equipos que juegan el partido.
    #En la quiniela se indican 15 partidos. Ejemplo: equipos = [["Sevilla","Betis"],["Madrid","Barcelona"],...]
    #Resultados: Es una lista de enteros donde se indica el resultado. También tiene dos columnas (cada elemento es una lista),
    #en la primera se guarda el número de goles del equipo que está guardado en la primera columna de la tabla anterior,
    #y en la segunda los goles del otro equipo. Ejemplo: resultados=[[3,0],[0,0],...]

#El programa ira pidiendo los nombres de los equipos de cada partido y el resultado del partido, a continuación se imprimirá la quiniela de esa jornada.

equipos = []
resultados = []
n = int(input("Dime la cantidad de partidos de la quiniela:"))
for i in range(0,n):
    equipo1 = str(input("Primer equipo: "))
    equipo2 = str(input("Segundo equipo: "))
    goles1 = int(input("Goles marcados por el primer equipo: "))
    goles2 = int(input("Goles marcados por el segundo equipo: "))
    equipo = [equipo1,equipo2]
    equipos.append(equipo)
    goles = [goles1,goles2]
    resultados.append(goles)
print(equipos)
print(resultados)
print("BÚSQUEDA DE JORNADA:")
print("--------------------")
equip1 = str(input("Dame el nombre del primer equipo: "))
equip2 = str(input("Dame el nombre del segundo equipo: "))
for i in equipos:
    if i == [equip1,equip2]:
        print("JORNADA -->",resultados[int(equipos.index([equip1,equip2]))])
