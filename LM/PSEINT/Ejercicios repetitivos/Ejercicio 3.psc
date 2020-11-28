
Proceso Ejercicio_3
	
	Definir num,sum,med,n como Real;
	
	Escribir Sin Saltar "Escribe un número: ";
	
	Leer num;
	
	sum <- num;
	
	n <- 1;
	
	Mientras num <> 0 Hacer
		
		Escribir Sin Saltar "Escribe otro número: ";
		
		Leer num;
		
		sum <- sum + num;
		
		n <- n + 1;
		
		med <- sum / n;
		
	FinMientras
	
	Escribir "La suma de todos los números sería ", sum , " y la media ", med , ".";
	
FinProceso
