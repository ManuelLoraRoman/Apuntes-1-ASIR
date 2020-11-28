
Proceso Ejercicio_12
	
	Definir dinero,n,total como Real;
	
	n <- 1;
	
	total <- 0;
	
	Repetir
		
		Escribir Sin Saltar "Dinero depositado en el mes ", n ," (€):";
		
		Leer dinero;
		
		total <- total + dinero;
		
		n <- n + 1;
		
	Hasta Que n = 13
	
	Escribir "El total de dinero ahorrado sería: " , total , " €.";
	
FinProceso
