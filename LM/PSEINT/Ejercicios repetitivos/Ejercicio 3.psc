
Proceso Ejercicio_3
	
	Definir num,sum,med,n como Real;
	
	Escribir Sin Saltar "Escribe un n�mero: ";
	
	Leer num;
	
	sum <- num;
	
	n <- 1;
	
	Mientras num <> 0 Hacer
		
		Escribir Sin Saltar "Escribe otro n�mero: ";
		
		Leer num;
		
		sum <- sum + num;
		
		n <- n + 1;
		
		med <- sum / n;
		
	FinMientras
	
	Escribir "La suma de todos los n�meros ser�a ", sum , " y la media ", med , ".";
	
FinProceso
