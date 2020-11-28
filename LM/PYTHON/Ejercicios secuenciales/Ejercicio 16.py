
#Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d.
#El que está detrás viaja a una velocidad mayor.
#Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km)
#y sus respectivas velocidades (km/h) y con esto determinar y
#mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.


v1 = int(input("Dime la velocidad del coche nº1:"))
v2 = int(input("Dime la velocidad del coche nº2:"))
d = int(input("Distancia entre los dos coches:"))

tiempo = d / (v2 -v1)

print("El tiempo en el que alcanzará el vehículo más rápido al otro será de %.2f segundos." % tiempo)
