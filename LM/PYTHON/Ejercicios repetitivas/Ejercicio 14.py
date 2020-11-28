
#Una persona se encuentra en el kilómetro 70 de una carretera, otra se encuentra en el km 150,
#los coches tienen sentido opuesto y tienen la misma velocidad.
#Realizar un programa para determinar en qué kilómetro de esa carretera se encontrarán.


p1 = 70
print("La persona nº1 está en el",p1,"km.")
p2 = 150
print("La persona nº2 está en el",p2,"km.")

while p1 != p2:
    p1 = p1 + 1
    p2 = p2 - 1
print("Los dos vehículos se encontrarán en el km",p1,".")
