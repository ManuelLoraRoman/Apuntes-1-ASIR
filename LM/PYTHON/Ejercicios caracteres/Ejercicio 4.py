
#Suponiendo que hemos introducido una cadena por teclado que representa una frase
#(palabras separadas por espacios), realiza un programa que cuente cuantas palabras tiene.

cadena = str(input("Dame un frase: "))
print("Hay",cadena.count(" ") + 1,"palabras.")
