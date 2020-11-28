# Función centrar: Recibe una cadena y la imprime centrada en la pantalla.
# Suponemos que tenemos una pantalla de 80 caracteres de ancho.
# Para centrar usamos la formula 40 - (Longitud(cad)/2)
# Parámetros de entrada: cadena a imprimir centrada


def centrar(cad):
	print(" " * int(40 - (len(cad)/2)),cad)
	print(" " * int(40 - (len(cad)/2)),"=" * len(cad))


# Crea un función EscribirCentrado, que reciba como parámetro un texto y lo
# escriba centrado en pantalla (suponiendo una anchura de 80 columnas; pista:
# deberás escribir 40 - longitud/2 espacios antes del texto).
# Además subraya el mensaje utilizando el carácter =.

mensaje1 = "Un mensaje centrado"
centrar(mensaje1)
mensaje2 = "Otro mensaje"
centrar(mensaje2)


# Función EsMultiplo: Recibe dos número e indica si el primero el múltiplo del
# segundo. Para ello calculo el resto de la división, si es 0 es múltiplo.
# Parámetros de entrada: dos números
# Dato devuelto: múltiplo: Valor lógico verdadero si el primero es múltiplo
# del segundo, Falso en caso contrario.

def esmultiplo(num1,num2):
	if num1 % num2 == 0:
		return True
	else:
		return False

# Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos
# es múltiplo del otro. Crea una función EsMultiplo que reciba los dos números,
# y devuelve si el primero es múltiplo del segundo.

numero1 = int(input("Número 1:"))
numero2 = int(input("Número 2:"))
if esmultiplo(numero1,numero2):
	print(numero1,"es múltiplo de",numero2)
else:
	print(numero1,"no es múltiplo de",numero2)


# Función calcularTemperaturaMedia: Recibe dos números reales que representan
# dos temperaturas y devuelve la temperatura media.
# Parámetros de entrada: dos temperaturas (real)
# Dato devuelto: La temperatura media (real)

def calcularTemperaturaMedia(temp1,temp2):
	return (temp1 + temp2)/2

# Crear una función que calcule la temperatura media de un día a partir de la
# temperatura máxima y mínima. Crear un programa principal, que utilizando la
# función anterior, vaya pidiendo la temperatura máxima y mínima de cada día
# y vaya mostrando la media. El programa pedirá el número de días que se van
# a introducir.

cantidad=int(input("¿Cuántas temperaturas vas a calcular?:"))
for indice in range(cantidad):
	tmin = float(input("Introduce temperatura mínima:"))
	tmax = float(input("Introduce temperatura máxima:"))
	print("Temperatura media:",calcularTemperaturaMedia(tmin,tmax))


# Función ConvetirEspaciado: Recibe una cadena de caracteres, y devuelve otra
# con los mismos caracteres separados con espacio.
# Parámetros de entrada: Cadena de caracteres
# Dato devuelto: Cadena igual a la anterior pero con espacios entre los
# caracteres

def ConvertirEspaciado(cad):
	cad_con_espacio = cad.replace(""," ")
	cad_con_espacio.strip()
	return cad_con_espacio

# Crea un función "ConvertirEspaciado", que reciba como parámetro un texto y
# devuelve una cadena con un espacio adicional tras cada letra. Por ejemplo,
# "Hola, tú" devolverá "H o l a , t ú ". Crea un programa principal donde se
# use dicha función.

mensaje = input("Introduce una cadena:")
print("La cadena con espacio:",ConvertirEspaciado(mensaje))


# Procedimiento CalcularMaxMin: recibe una lista de enteros  y devuelve
#  el máximo y el mínimo de los números guardados en el vector.
# Parámetros de entrada: lista de enteros
# Valores de salida: valor máximo y mínimo
import random
def CalcularMaxMin(lista):
	return (max(lista),min(lista))

# Crea una función "calcularMaxMin" que recibe una lista con valores numéricos y
# devuelve el valor máximo y el mínimo. Crea un programa que pida números por
# teclado y muestre el máximo y el mínimo, utilizando la función anterior.

numeros = []
# Incializo la lista con valores aleatorios
for i in range(10):
	numeros.append(random.randint(1,100))
vmax,vmin = CalcularMaxMin(numeros)
print("El valor máximo es ",vmax)
print("El valor mínimo es ",vmin)


# Función CalcularAreaPerimetro: recibe el radio de una circunferencia y
# devuelve el área y el perímetro.
# Parámetros de entrada: radio (real)
# Valores de salida: área y perímetro (real)
import math
def CalcularAreaPerimetro(radio):
	area = math.pi * radio ** 2;
	perimetro = 2 * math.pi * radio;
	return area,perimetro

# Diseñar una función que calcule el área y el perímetro de una circunferencia.
# Utiliza dicha función en un programa principal que lea el radio de una
# circunferencia y muestre su área y perímetro.

radio = float(input("Introduce el radio:"))
area,perimetro = CalcularAreaPerimetro(radio)
print("Área:",area)
print("Perímetro:",perimetro)


# Función Login: Recibe un nombre de usuario y una contraseña, y devuelve un
# valor lógico: verdadero si se ha introducido el nombre y la contraseña adecuadas.
# Además devuelve el numero de internos
# Parámetros de entrada: nombre y contraseña, y el número de intentos actual
# Datos devueltos: Valor lógico indicando si ha hecho login, e intentos

def Login(nombre,password,intentos):
	intentos += 1
	if nombre == "usuario1" and password == "asdasd":
		return(True,intentos)
	else:
		return(False,intentos)

# Crear una subrutina llamada "Login", que recibe un nombre de usuario y una
# contraseña y te devuelve Verdadero si el nombre de usuario es "usuario1" y la
# contraseña es "asdasd". Además recibe el número de intentos que se ha intentado
# hacer login y si no se ha podido hacer login incremente este valor.
# Crear un programa principal donde se pida un nombre de usuario y una contraseña
# y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.


cuantasveces = 0
while True:
	usuario = input("Usuario:")
	clave = input("Password:")
	entrar,cuantasveces = Login(usuario,clave,cuantasveces)
	if not entrar:
		print("Error. Nombre de usuario o contraseña incorrecta.")
	if entrar or cuantasveces == 3:
		break
	# Sale si he hecho login o llego a los tres intentos
	# Puedo llegar a esta instrucción por dos razones
	# Si he hecho login muestro mensaje de bienvenida
if entrar:
	print("Bienvenidos al sistema")
else: # He llegado a los tres intentos
	print("No has entrado en el sistema")


# Función CalcularFactorial: Recibe un número si el número=1 devuelve que el
# factorial es 1, sino acumula el producto del número con el cálculo del factorial
# del numero-1. Es una función recursiva.
# Parámetros de entrada: número
# Dato devuelto: Factorial del número

def CalcularFactorial(num):
	if num == 1:
		return 1
	else:
		return num*CalcularFactorial(num-1)

# Crear una función recursiva que permita calcular el factorial de un número.
# Realiza un programa principal donde se lea un entero y se muestre el resultado
# del factorial.

numero1 = int(input("Número:"))
print("El factorial es:",CalcularFactorial(numero1))


# Función Intercambiar: Recibe dos números como parámetros de entrada y
#  devuelve los números ordenador de mayor a menor
# Parámetros de entrada: dos números
# Datos de salida: dos números

def Intercambiar(mayor,menor):
	if mayor<menor:
		return menor,mayor
	else:
		return mayor,menor

# Función CalcularMCD: Recibe dos números y devuelve el MCD utilizando el método
# de Euclides. El método de Euclides es el siguiente:
#  * Se divide el número mayor entre el menor.
#  * Si la división es exacta, el divisor es el MCD.
#  * Si la división no es exacta, dividimos el divisor entre el resto obtenido y
# se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.
# Parámetros de entrada: dos números
# Dato devuelto: El MCD

def CalcularMCD(num1,num2):
	# Se divide el número mayor entre el menor.
	num1, num2 = Intercambiar(num1,num2)
	resto = num1 % num2
	if resto == 0: # Si la división es exacta, el divisor es el MCD.
		return num2
	else:
		# Si la división no es exacta, dividimos el divisor entre el resto obtenido y
		# se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.
		return CalcularMCD(num2,resto)

# Crea un programa principal que lea dos números enteros y muestre el MCD.

numero1 = int(input("Número 1:"))
numero2 = int(input("Número 2:"))
print("MCD: ", CalcularMCD(numero1,numero2))


# Función Convertir_A_Segundos: Recibe una cantidad de horas, minutos y segundos
# y calcula a cuantos segundos corresponde.
# Parámetros de entrada: hora, minutos y segundos
# Dato devuelto: Segundos totales

def Convertir_A_Segundos(h,m,s):
	return h * 3600 + m * 60 + s

# Función Convertir_A_HMS: Recibe una cantidad de segundos y debe calcular a
# que hora, minutos y segundos corresponde
# Parámetros de entrada: segundos
# Valores de salida: hora,minutos y segundos

def Convertir_A_HMS(seg):
	# Horas = Divisíón entera de los segundos entre 3600
	h = seg//3600
	# Decremento los segundos que me quedan por convertir
	seg = seg - h*3600
	# Minutos = División entera de los segundos entre 60
	m = seg//60
	# Decremento los segundos que me quedan por convertir
	seg = seg - m*60
	# Lo que me quedan corresponden a los segundos
	s = seg
	return h,m,s

# Escribe un programa principal con un menú donde se pueda elegir la opción de
# convertir a segundos, convertir a horas,minutos y segundos o salir del programa.

while True:
	print("1.- Convertir a segundos")
	print("2.- Convertir a horas, minutos y segundos")
	print("3.- Salir")
	opcion = int(input())
	if opcion == 1:
		hor = int(input("Horas:"))
		minu = int(input("Minutos:"))
		seg = int(input("Segundos:"))
		print("Corresponde a",Convertir_A_Segundos(hor,minu,seg),"segundos.")
	elif opcion == 2:
		segund=int(input("Segundos:"))
		hor,minu,seg = Convertir_A_HMS(segund)
		print("Corresponde a ",hor,":",minu,":",seg)
	elif opcion == 3:
		break
	else:
		print("Opción incorrecta")


# Función EsBisiesto: Recibe un año y devuelve si es o no bisiesto
# Parámetros de entrada: año
# Dato devuelto: Valor lógico indicando si es bisiesto (Verdadero) o no (Falso)

def EsBisiesto(year):
	return (year % 4 == 0 and not (year % 100 == 0)) or year % 400 == 0

# Función DiasDelMes: Recibe un mes y un año y devuelve el número de días que tiene
# ese mes en ese año. Necesita la función EsBisiesto
# Parámetros de entrada: mes y año
# Dato devuelto: Días del mes en ese año

def DiasDelMes(month,year):
	if month in [1,3,5,7,8,10,12]:
		return 31
	elif month in [4,6,9,11]:
		return 30
	elif month == 2:
		if EsBisiesto(year):
			return 29
		else:
			return 28

# Función Calcular_Dia_Juliano: Recibe un día, mes y año y devuelve el día juliano
# correspondiente a esa fecha. El día juliano correspondiente a una fecha es un
# número entero que indica los días que han transcurrido desde el 1 de enero del
# año indicado. Depende de la función DiasDelMes
# Parámetros de entrada: día, mes y año
# Dato devuelto: Día juliano

def Calcular_Dia_Juliano(day,month,year):
	diaj = 0
	for mes in range(1,month):
		diaj = diaj + DiasDelMes(mes,year)
	diaj = diaj + day
	return diaj

# Función LeerFecha: Lee por teclado el día, mes y el año y lo devuelve
# como parámetro de entrada / salida.
# Datos devueltos: día, mes y año

def LeerFecha():
	day = int(input("Día:"))
	month = int(input("Mes:"))
	year = int(input("Año:"))
	return day,month,year

#  Queremos crear un programa principal que al introducir una fecha nos diga el
# día juliano que corresponde.

d,m,a = LeerFecha()
print("Día Juliano: ",Calcular_Dia_Juliano(d,m,a))


# Función ValidarFecha: Recibe un día, mes y año correspondiente a una fecha y
# devuelve si la fecha es correcta o no.
# Simplemente miramos si el día indicado es mayor que 1 y menor que los días del mes
# Si introducimos un mes incorrecto, la función DiasDelMes devuelve 0 por lo tanto
# la fecha va a ser incorrecta.
# Parámetros de entrada: día, mes y año
# Dato devuelto: Valor lógico indicando si es correcta (Verdadero) o no (Falso)

def ValidarFecha(day,month,year):
	if day<1 or day>DiasDelMes(month,year):
		return False
	else:
		return True

# Función EsBisiesto: Recibe un año y devuelve si es o no bisiesto
# Parámetros de entrada: año
# Dato devuelto: Valor lógico indicando si es bisiesto (Verdadero) o no (Falso)

def EsBisiesto(year):
	return (year % 4 == 0 and not (year % 100 == 0)) or year % 400 == 0

# Función DiasDelMes: Recibe un mes y un año y devuelve el número de días que tiene
# ese mes en ese año. Necesita la función EsBisiesto
# Añadimos la opción "else" para devolver 0 si introducimos un mes incorrecto.
# Parámetros de entrada: mes y año
# Dato devuelto: Días del mes en ese año

def DiasDelMes(month,year):
	if month in [1,3,5,7,8,10,12]:
		return 31
	elif month in [4,6,9,11]:
		return 30
	elif month == 2:
		if EsBisiesto(year):
			return 29
		else:
			return 28
	else:
		return 0

# Función Calcular_Dia_Juliano: Recibe un día, mes y año y devuelve el día juliano
# correspondiente a esa fecha. El día juliano correspondiente a una fecha es un
# número entero que indica los días que han transcurrido desde el 1 de enero del
# año indicado. Depende de la función DiasDelMes
# Parámetros de entrada: día, mes y año
# Dato devuelto: Día juliano

def Calcular_Dia_Juliano(day,month,year):
	diaj = 0
	for mes in range(1,month):
		diaj = diaj + DiasDelMes(mes,year)
	diaj = diaj + day
	return diaj

# Función LeerFecha: Lee por teclado el día, mes y el año y lo devuelve
# como parámetro de entrada / salida.Se utiliza la función validarFecha para
# asegurar que la fecha es correcta.
# Datos devueltos: día, mes y año

def LeerFecha():
	while True:
		day = int(input("Día:"))
		month = int(input("Mes:"))
		year = int(input("Año:"))
		if not ValidarFecha(day,month,year):
			print("Fecha no válida")
		else:
			break
	return day,month,year


# Vamos a mejorar el ejercicio anterior haciendo una función para validar la fecha.
# De tal forma que al leer una fecha se asegura que es válida.
d,m,a = LeerFecha()
print("Día Juliano: ",Calcular_Dia_Juliano(d,m,a))


# Función Intercambiar: Recibe dos números como parámetros de entrada y
#  devuelve los números ordenador de mayor a menor
# Parámetros de entrada: dos números
# Datos de salida: dos números

def Intercambiar(mayor,menor):
	if mayor<menor:
		return menor,mayor
	else:
		return mayor,menor

# Función CalcularMCD: Recibe dos números y devuelve el MCD utilizando el método
# de Euclides. El método de Euclides es el siguiente:
#  * Se divide el número mayor entre el menor.
#  * Si la división es exacta, el divisor es el MCD.
#  * Si la división no es exacta, dividimos el divisor entre el resto obtenido y
# se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.
# Parámetros de entrada: dos números
# Dato devuelto: El MCD

def CalcularMCD(num1,num2):
	# Se divide el número mayor entre el menor.
	num1, num2 = Intercambiar(num1,num2)
	resto = num1 % num2
	if resto == 0: # Si la división es exacta, el divisor es el MCD.
		return num2
	else:
		# Si la división no es exacta, dividimos el divisor entre el resto obtenido y
		# se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.
		return CalcularMCD(num2,resto)

# Función LeerFracion: Lee por teclado una fracción (numerador y denominador)
#  y lo devuelve como parámetro de entrada y salida.
# Esta función usa SimplificarFraccion para simplificar la fracción leída.
# Datos devueltos: numerador y denominador

def LeerFraccion():
	num = int(input("Numerador:"))
	den = int(input("Denominador:"))
	num,den = SimplificarFraccion(num,den)
	return num,den

# Función SimplificarFracion: Recibe una fracción (numerador y denominador)
#  y lo devuelve la fracción simplificada como parámetro ed entrada y salida.
# Para simplificar hay que dividir numerador y dominador por el MCD del numerador
# y denominador.
# Datos devueltos: numerador y denominador

def SimplificarFraccion(num,den):
	mcd = CalcularMCD(num,den)
	num = num / mcd
	den = den / mcd
	return num,den

# Función EscribirFracion: Recibe una fracción (numerador y denominador)
#  y lo muestra por pantalla. Muestra numerador partido por denominador. Si el
# denominador es 1 sólo muestra el numerador.
# Parámetros de entrada: numerador y denominador

def EscribirFraccion(num,den):
	if den!= 1:
		print(num)
		print("---")
		print(den)
	else:
		print("")
		print(num)
		print("")

# Función SumarFracciones: Recibe dos fracciones (numerador y denominador)
#  y devuelve otra fracción que es la suma de la primera y la segunda.
# La suma de dos fracciones es otra fracción cuyo `numerador=n1*d2+d1*n2`
# y `denominador=d1*d2`.
# Este Función usa SimplificarFraccion para simplificar la fracción calculada.
# Parámetros de entrada: numerador1 y denominador1, numerador2 y denominador2
# Datos devueltos: numerador y denominador de la fracción resultado

def SumarFracciones(n1,d1,n2,d2):
	nr = n1*d2 + d1*n2
	dr = d1 * d2
	nr,dr = SimplificarFraccion(nr,dr)
	return nr,dr

# Función RestarFracciones: Recibe dos fracciones (numerador y denominador)
#  y devuelve otra fracción que es la resta de la primera y la segunda.
# La resta de dos fracciones es otra fracción cuyo `numerador=n1*d2-d1*n2`
# y `denominador=d1*d2`.
# Este Función usa SimplificarFraccion para simplificar la fracción calculada.
# Parámetros de entrada: numerador1 y denominador1, numerador2 y denominador2
# Datos devueltos: numerador y denominador de la fracción resultado

def RestarFracciones(n1,d1,n2,d2):
	nr = n1*d2 - d1*n2
	dr = d1 * d2
	nr,dr = SimplificarFraccion(nr,dr)
	return nr,dr

# Función MultiplicarFracciones: Recibe dos fracciones (numerador y denominador)
#  y devuelve otra fracción que es el producto de la primera y la segunda.
# La resta de dos fracciones es otra fracción cuyo `numerador=n1*n2`
# y `denominador=d1*d2`
# Este Función usa SimplificarFraccion para simplificar la fracción calculada.
# Parámetros de entrada: numerador1 y denominador1, numerador2 y denominador2
# Datos devueltos: numerador y denominador de la fracción resultado

def MultiplicarFracciones(n1,d1,n2,d2):
	nr = n1 * n2
	dr = d1 * d2
	nr,dr = SimplificarFraccion(nr,dr)
	return nr,dr

# Función DividirFracciones: Recibe dos fracciones (numerador y denominador)
#  y devuelve otra fracción que es la división de la primera y la segunda.
# La resta de dos fracciones es otra fracción cuyo `numerador=n1*d2`
# y `denominador=d1*n2`
# Este Función usa SimplificarFraccion para simplificar la fracción calculada.
# Parámetros de entrada: numerador1 y denominador1, numerador2 y denominador2
# Datos devueltos: numerador y denominador de la fracción resultado

def DividirFracciones(n1,d1,n2,d2):
	nr = n1 * d2
	dr = d1 * n2
	nr,dr = SimplificarFraccion(nr,dr)
	return nr,dr

# Crear un programa que utilizando las funciones anteriores muestre un menú para
# operar con fracciones.

while True:
	print("1.- Sumar dos fracciones")
	print("2.- Restar dos fracciones")
	print("3.- Multiplicar dos fracciones")
	print("4.- Dividir dos fracciones")
	print("5.- Salir")
	opcion = int(input())
	if opcion>=1 and opcion <=4:
		print("Fracción 1:")
		num1,den1= LeerFraccion()
		print("Fracción 2:")
		num2,den2= LeerFraccion()
	if opcion == 1:
		print("Sumar fracciones")
		numr,denr = SumarFracciones(num1,den1,num2,den2)
		EscribirFraccion(numr,denr)
	elif opcion == 2:
		print("Restar fracciones")
		numr,denr = RestarFracciones(num1,den1,num2,den2)
		EscribirFraccion(numr,denr)
	elif opcion == 3:
		print("Multiplicar fracciones")
		numr,denr = MultiplicarFracciones(num1,den1,num2,den2)
		EscribirFraccion(numr,denr)
	elif opcion == 4:
		print("Dicidir fracciones")
		numr,denr = DividirFracciones(num1,den1,num2,den2)
		EscribirFraccion(numr,denr)
	elif opcion == 5:
		break
	else:
		print("Opción incorrecta")


# Función LongitudPila: Recibe una lista (pila).
# Devuelve un contador con los elementos de la pila.

def LongitudPila(pila):
	return len(pila)

# Función EstaVaciaPila: Recibe una lista (pila).
# Devuelve un valor lógico indicando si la pila está vacía.

def EstaVaciaPila(pila):
	return len(pila) == 0

#Procedimiento AddPila: Recibe una lista (pila) y un elemento (cadena)
# Parámetro de entrada:La pila y el elemento.
# Valor devuelto: La pila
def AddPila(cad, pila):
	pila.append(cad)

#Función SacarPila: Recibe una lista (pila) y devuelve
# el elemento que se ha introducido en último lugar, si no está vacía.
# El índice de ese elemento será la longitud de la pila - 1
# Si está vacía, escribe un mensaje de error.
# Parámetro de entrada:La pila y el elemento.
# Dato devuelto: El elemento
def SacarDeLaPila(pila):
	if not EstaVaciaPila(pila):
		return pila.pop(len(pila)-1)
	else:
		print("No se puede sacar elemento. La pila está vacia")
		return ""


# Función EscribirPila: Recibe una lista (pila).
# Muestra los elementos de la pila.
# Parámetros de entrada: La pila
def EscribirPila(pila):
	for elem in pila:
		print(elem,end=" ")
	print()


# Realiza un programa principal que nos permita usar funciones para manipular pilas.
mipila = []
while True:
	print("1.- Añadir elemento a la pila")
	print("2.- Sacar elemento de la pila")
	print("3.- Longitud de la pila")
	print("4.- Mostrar pila")
	print("5.- Salir")
	opcion = int(input())
	if opcion == 1:
		elem = input("Dame la cadena para añadir a la pila:")
		AddPila(elem,mipila)
	elif opcion == 2:
		print(SacarDeLaPila(mipila))
	elif opcion == 3:
		print("Longitud: ",LongitudPila(mipila))
	elif opcion == 4:
		EscribirPila(mipila)
	elif opcion == 5:
		break
	else:
		print("Opción incorrecta")


# Función LongitudCola: Recibe una lista (cola).
# Devuelve un contador con los elementos de la cola.

def LongitudCola(cola):
	return len(cola)

# Función EstaVaciaCola: Recibe una lista (cola).
# Devuelve un valor lógico indicando si la cola está vacía.

def EstaVaciaCola(cola):
	return len(cola) == 0

#Procedimiento AddCola: Recibe una lista (cola) y un elemento (cadena)
# Parámetro de entrada:La cola y el elemento.
# Valor devuelto: La cola
def AddCola(cad, cola):
	cola.append(cad)

#Función SacarCola: Recibe una lista (cola) y devuelve
# el elemento que se ha introducido en primer lugar, si no está vacía.
# Si está vacía, escribe un mensaje de error.
# Parámetro de entrada:La cola y el elemento.
# Dato devuelto: El elemento
def SacarDeLaCola(cola):
	if not EstaVaciaCola(cola):
		return cola.pop(0)
	else:
		print("No se puede sacar elemento. La cola está vacia")
		return ""


# Función EscribirCola: Recibe una lista (cola).
# Muestra los elementos de la cola.
# Parámetros de entrada: La cola
def EscribirCola(cola):
	for elem in cola:
		print(elem,end=" ")
	print()


# Realiza un programa principal que nos permita usar funciones para manipular pilas.
micola = []
while True:
	print("1.- Añadir elemento a la cola")
	print("2.- Sacar elemento de la cola")
	print("3.- Longitud de la cola")
	print("4.- Mostrar cola")
	print("5.- Salir")
	opcion = int(input())
	if opcion == 1:
		elem = input("Dame la cadena para añadir a la cola:")
		AddCola(elem,micola)
	elif opcion == 2:
		print(SacarDeLaCola(micola))
	elif opcion == 3:
		print("Longitud: ",LongitudCola(micola))
	elif opcion == 4:
		EscribirCola(micola)
	elif opcion == 5:
		break
	else:
		print("Opción incorrecta")
