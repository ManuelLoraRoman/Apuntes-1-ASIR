

//Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. 
//Crear un programa principal, que utilizando la función anterior, 
//vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media.
//El programa pedirá el número de días que se van a introducir.

Funcion temp <- TemperaturaMedia(tempmax,tempmin)
	
	Definir temp Como Real;
	
	temp <- (tempmax + tempmin)/2;
	
FinFuncion


Proceso Resultado
	
	Definir tempmaxima,tempminima,tempmedia,i,dias como Real;
	
	Escribir Sin Saltar "Escribe el nº de días: ";
	
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
