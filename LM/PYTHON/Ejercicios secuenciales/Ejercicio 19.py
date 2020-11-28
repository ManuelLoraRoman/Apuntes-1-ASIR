
#Escribir un algoritmo para calcular la nota final de un estudiante, considerando que:
#por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0.
#Imprime el resultado obtenido por el estudiante.

preguntas = int(input("Dime el nº de preguntas del examen:"))
rescor = int(input("Dime el nº de preguntas correctas:"))
resinc = int(input("Dime el nº de preguntas incorrectas:"))
resbla = int(input("Dime el nº de preguntas en blanco:"))

print("El resultado del examen sería",(rescor * 5) + (resinc * (-1)) + (resbla * 0),".")
