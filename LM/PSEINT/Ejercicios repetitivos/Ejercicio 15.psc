
Proceso Ejercicio_15
	
	Definir pago,n,total como Real;
	
	pago <- 10;
	
	total <- 0;
	
	n <- 0;
	
	Repetir
		
		pago <- pago * 2;
		
		total <- pago + total;
		
		n <- n + 1;
		
	Hasta Que n = 21
	
	Escribir "Tiene que pagar un total de ", total , "€.";
	
FinProceso
