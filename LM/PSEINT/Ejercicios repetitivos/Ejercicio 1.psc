
Proceso Ejercicio_1
	
	Definir num,fact,c como Real;
	
	Escribir Sin Saltar "Escriba el número que quieres factorizar: ";
	
	Leer num;
	
	fact <- 1;
	
	c <- 1;
	
	Mientras c <= num Hacer
		
		fact <- fact * c;
		
		c <- c + 1;
		
	FinMientras
	
	Escribir "El factorial de ", num , " es " , fact , ".";
	
FinProceso
