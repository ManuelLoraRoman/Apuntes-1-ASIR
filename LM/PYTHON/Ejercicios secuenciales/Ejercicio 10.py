
#Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:

#55% del promedio de sus tres calificaciones parciales.
#30% de la calificación del examen final.
#15% de la calificación de un trabajo final.

cal1 = int(input("Nota primera calificación:"))
cal2 = int(input("Nota segunda calificación:"))
cal3 = int(input("Nota tercera calificación:"))

calexam = int(input("Nota examen final:"))

caltrab = int(input("Nota trabajo final:"))

calfinal = (((cal1 + cal2 + cal3) / 3) * 0.55) + (calexam * 0.3) + (caltrab * 0.15)

print("Tu nota media será %.2f."%(calfinal))
