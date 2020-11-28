
#Amplíe el programa anterior haciendo que el programa lleve la cuenta de las respuestas correctas
#e incorrectas e indique la nota correspondiente. Si la nota es igual o mayor que 9,
#el programa felicitará al usuario por el resultado. Ayuda: La nota se calcula con la fórmula Nota=Correctas / Total * 10.

#Número de preguntas: 2

#¿Cuánto es 7 x 8? 56
#¡Respuesta correcta!
#¿Cuánto es 4 x 9? 35
#¡Respuesta incorrecta!

#Ha contestado correctamente 1 pregunta
#Le corresponde una nota de 5.0


#Número de preguntas: 3

#¿Cuánto es 7 x 8? 56
#¡Respuesta correcta!
#¿Cuánto es 4 x 9? 35
#¡Respuesta incorrecta!
#¿Cuánto es 2 x 3? 6
#¡Respuesta correcta!

#Ha contestado correctamente 2 preguntas
#Le corresponde una nota de 6.7

#Número de preguntas: 1
#¿Cuánto es 7 x 8? 56
#¡Respuesta correcta!

#Ha contestado correctamente 1 pregunta
#Le corresponde una nota de 10.0
#¡Enhorabuena!

import random

print("EXAMEN")
num = int(input("Número de preguntas: "))
n = 0
if num < 1:
    print("¡Imposible!")
else:
    for i in range(num):
        num1 = random.randint(0,10)
        num2 = random.randint(0,10)
        respuesta = int(input(f"¿Cuánto es {num1} x {num2}? "))
        if respuesta == num1 * num2:
            print("¡Respuesta correcta!")
            n = n + 1
        elif respuesta != num1 * num2:
            print("¡Respuesta incorrecta!")
if n == 1:
    print("Ha contestado correctamente 1 pregunta\nLe correspone una nota de", (n * 10)/num)
else:
    print("Ha contestado correctamente",n,"preguntas\nLe correspone una nota de", (n * 10)/num)

if n == num:
    print("¡Enhorabuena!")
