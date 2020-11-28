
#Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y
#muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.

#Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
#Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: "ERROR: número incorrecto.".

dado = int(input("Introduzca el número de un dado:"))
if dado < 1 and dado > 6:
    print("ERROR: número incorrecto.")
else:
    if dado == 1:
        print("En la cara opuesta está el 6.")
    else:
        if dado == 2:
            print("En la cara opuesta está el 5.")
        else:
            if dado == 3:
                print("En la cara opuesta está el 4.")
            else:
                if dado == 6:
                    print("En la cara opuesta está el 1.")
                else:
                    if dado == 5:
                        print("En la cara opuesta está el 2.")
                    else:
                        if dado == 4:
                            print("En la cara opuesta está el 3.")
