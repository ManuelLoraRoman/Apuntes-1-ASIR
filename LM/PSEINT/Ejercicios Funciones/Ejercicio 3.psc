

//Crear una funci�n que calcule la temperatura media de un d�a a partir de la temperatura m�xima y m�nima. 
//Crear un programa principal, que utilizando la funci�n anterior, 
//vaya pidiendo la temperatura m�xima y m�nima de cada d�a y vaya mostrando la media.
//El programa pedir� el n�mero de d�as que se van a introducir.

Funcion temp <- TemperaturaMedia(tempmax,tempmin)
	
	Definir temp Como Real;
	
	temp <- (tempmax + tempmin)/2;
	
FinFuncion


Proceso Resultado
	
	Definir tempmaxima,tempminima,tempmedia,i,dias como Real;
	
	Escribir Sin Saltar "Escribe el n� de d�as: ";
	
	Leer dias;
	
	Para i <- 1 Hasta dias Hacer
		
		Escribir Sin Saltar "Dime la temp.max para el dia ", i , ": ";
		
		Leer tempmaxima;
		
		Escribir Sin Saltar "Dime la temp.min para el dia ", i , ": ";
		
		Leer tempminima;
		
		tempmedia <- TemperaturaMedia(tempminima,tempmaxima);
		
		Escribir "La temperatura media del dia ", i , " es: ", tempmedia, ".";
		
	FinPara
	
FinProceso
