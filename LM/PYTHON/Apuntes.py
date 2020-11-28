#ENTEROS
#abs(x): Devuelve al valor absoluto de un número.
#divmod(x,y): Toma como parámetro dos números, y devuelve una tubla con dos valores, la división entera, y el módulo o resto de la división.
#hex(x): Devuelve una cadena con la representación hexadecimal del número que recibe como parámetro.
#bin(x): Devuelve una cadena con la representación binaria del número que recibe como parámetro.
#pow(x,y): Devuelve la potencia de la base x elevado al exponente y. Es similar al operador**`.
#round(x,[y]): Devuelve un número real (float) que es el redondeo del número recibido como parámetro,
#podemos indicar un parámetro opcional que indica el número de decimales en el redondeo.
#int(x): Convierte el valor a entero.
#float(x): Convierte el valor a float.


#continue --> Deja de ejecutar las restantes instrucciones del bucle y vuelve a iterar.
#Para ir de 10 a 1
#for var in range(10,0,-1):
    #print(var," ",end="")
#in, not in en cadenas
#Como resumen de las distintas posibilidades podemos indicar:
#cadena[start:end] 	  # Elementos desde la posición start hasta end-1
#cadena[start:]    	  # Elementos desde la posición start hasta el final
#cadena[:end]      	  # Elementos desde el principio hasta la posición end-1
#cadena[:] 	 	  # Todos Los elementos
#cadena[start:end:step] # Igual que el anterior pero dando step saltos.
#capitalize() nos permite devolver la cadena con el primer carácter en mayúsculas.
#lower() y upper() convierte la cadena de caracteres en minúsculas y mayúsculas respectivamente.
#swapcase(): devuelve una cadena nueva con las minúsculas convertidas a mayúsculas y viceversa.
#title(): Devuelve una cadena con los primeros caracteres en mayúsculas de cada palabra.
#count(): Es un método al que indicamos como parámetro una subcadena y cuenta cuantas apariciones hay de esa subcadena en la cadena.
#Además podemos indicar otro parámetro para indicar la posición desde la que queremos iniciar la búsqueda.
#Y otro parámetro optativo para indicar la posición final de búsqueda.
#find() nos devuelve la posición de la subcadena que hemos indicado como parámetro. Sino se encuentra se devuelve -1.
#startswith() nos indica con un valor lógico si la cadena empieza por la subcadena que hemos indicado como parámetro.
#Podemos indicar también con otro parámetro la posición donde tiene que buscar.
#endswith() igual que la anterior pero indica si la cadena termina con la subcadena indicada.
#En este caso, se puede indicar la posición de inicio y final de búsqueda.
#Otras funciones de validación: isdigit(), islower(), isupper(), isspace(), istitle(),...
#replace(): Devuelve una cadena donde se ha sustituido las apariciones de la primera subcadena indicada por la segunda subcadena indicada como parámetro.
#strip(): Devuelve una cadena donde se han quitado los espacios del principio y del final.
#Si indicamos una subcadena como parámetro quitará dicha subcadena del principio y del final
#aunque todavía no lo hemos estudiado, el método split() nos permite convertir una cadena en una lista. Lo usaremos más adelante.
#   >>> hora = "12:23:12"
#   >>> print(hora.split(":"))
#   ['12', '23', '12']
#splitlines(): Nos permite separar las líneas que hay en una cadena (indicada con el carácter \n) en una lista.
#   >>> texto = "Linea 1\nLinea 2\nLinea 3"
#   >>> print(texto.splitlines())
#   ['Linea 1', 'Linea 2', 'Linea 3']
#>>> lista1 = [20,40,10,40,50]
#>>> len(lista1)
#     5
#>>> max(lista1)
#     50
#>>> min(lista1)
#     10
#>>> sum(lista1)
#     150
#>>> sorted(lista1)
#     [10, 20, 30, 40, 50]
#>>> sorted(lista1,reverse=True)
#     [50, 40, 30, 20, 10]
#
#>>> tabla = [[1,2,3],[4,5,6],[7,8,9]]
#>>> tabla[1][1]
#5
#
#>>> for fila in tabla:
#...   for elem in fila:
#...      print(elem,end="")
#...   print()
#
#123
#456
#789

#append() para añadir un elemento a la lista
#El operador de asignación no crea una nueva lista, sino que nombra con dos nombres distintos a la misma lista, por lo tanto la forma más fácil de copiar una lista en otra es:
#   >>> lista1 = [1,2,3]
#   >>> lista2=lista1[:]
#   >>> lista1[1] = 10
#   >>> lista2
#   [1, 2, 3]

#extend(): Une dos listas
#insert(): Añade un elemento en un posición indicada de la lista
#pop(): elimina un elemento de la lista y lo devuelve. Se puede indicar el índice del elemento que queremos obtener como parámetro,
#sino se indica se devuelve y elimina el último:
#remove(): Elimina el elemento de la lista indicado por la posición
#reverse(): Modifica la lista invirtiendo los elementos
#sort(): Modifica la lista ordenando los elementos, se puede indicar el sentido de la ordenación
#count(): devuelve el número de apariciones de un elemento en la lista
#index(): Nos devuelve la posición de la primera aparición del elemento indicado. Se puede indicar la posición inicial y final de búsqueda

#f = open("fichero.txt","r")
#type(f)
#f.tell() #--> donde está el puntero
#f.read()
#f.seek(0) #--> mueve el puntero, es decir, si has leido antes, se queda en el final, y por lo tanto tienes que indicar desde donde quieres leer
#f.readlines()
#f.readline()
#f.close()
#with open("/etc/passwd", "r") as archivo:
#>>> f = open("ejemplo.txt","w")
#>>> type(f)
#<class '_io.TextIOWrapper'>
#>>> f.close()
#Añadido en modo binario. Crea si éste no existe
#Modo 	Comportamiento 	Puntero
#r	-->Solo lectura	Al inicio del archivo
#rb	-->Solo lectura en modo binario
#r+	-->Lectura y escritura 	Al inicio del archivo
#rb+	-->Lectura y escritura binario	Al inicio del archivo
#w	-->Solo escritura. Sobrescribe si existe. Crea el archivo si no existe.	Al inicio del archivo
#wb	-->Solo escritura en modo binario. Sobrescribe si existe. Crea el archivo si no existe.	Al inicio del archivo
#w+	-->Escritura y lectura. Sobrescribe si existe. Crea el archivo si no existe.	Al inicio del archivo
#wb+	-->Escritura y lectura binaria. Sobrescribe si existe. Crea el archivo si no existe.	Al inicio del archivo
#a	-->Añadido (agregar contenido). Crea el archivo si no existe.	Si el archivo existe, al final de éste. Si el archivo no existe, al comienzo.
#ab	-->	Si el archivo existe, al final de éste. Si el archivo no existe, al comienzo.
#a+	-->Añadido y lectura. Crea el archivo si no existe.	Si el archivo existe, al final de éste. Si el archivo no existe, al comienzo.
#ab+	-->Añadido y lectura en binario. Crea el archivo si no existe	Si el archivo existe, al final de éste. Si el archivo no existe, al comienzo.

    #closed: retorna True si el archivo se ha cerrado. De lo contrario, False.
    #mode: retorna el modo de apertura.
    #name: retorna el nombre del archivo
    #encoding: retorna la codificación de caracteres de un archivo de texto
#>>> with open("ejemplo3.txt","r") as fichero:
#...    for linea in fichero:
#...        print(linea)
