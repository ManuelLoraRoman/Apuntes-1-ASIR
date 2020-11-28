
Proceso Ejercicio_9
	
	Definir base,expo,n,sol como Real;
	
	Escribir Sin Saltar "Escriba la base: ";
	
	Leer base;
	
	Escribir Sin Saltar "Escriba el exponente: ";
	
	Leer expo;
	
	n <- 0;
	
	sol <- 1;
	
	Repetir
		
		sol <- sol * base;
		
		n <- n + 1;
		
	Hasta Que n = expo
	
	Escribir "La potencia sería: ", sol , ".";
	
FinProceso
