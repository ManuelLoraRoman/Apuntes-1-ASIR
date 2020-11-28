
#Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas.
#El programa pedirá el nombre de la fruta y la cantidad que se ha vendido
#y nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario.
# Si la fruta no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.

diccionario = {"Kiwi": 1.80,"Naranja": 1.50,"Mango": 3.20,"Limón": 1.10,"Ciruela": 3.25,"Higo": 4.20,"Plátano": 1.89}
indicador = "s"
while indicador.lower() == "s":
    fruta = str(input("Dime la fruta deseada: "))
    if fruta not in diccionario:
        print("ERROR")
    cantidad = int(input(f"Dime la cantidad de {fruta}: "))
    print("Precio Final: ",diccionario[fruta] * cantidad,"€.")
    indicador = str(input("¿Quieres realizar otra consulta? "))
    if indicador.lower() == "n":
        print("Programa finalizado")
        break;
