
Proceso Ejercicio_17
	
	Definir dias,horas,n,m,sueldo,dinero,numtra como Real;
	
	Escribir Sin Saltar "Escribe el nº de trabajadores: ";
	
	Leer numtra;
	
	Escribir Sin Saltar "Escribe el sueldo base por día";
	
	Leer dinero;
	
	n <- 1;
	
	m <- 0;
	
	sueldo <- 0;
	
	Repetir
		
		sueldo <- sueldo + dinero;
		
		n <- n + 1;
		
	Hasta Que n = 8
	
	Escribir "El sueldo de un trabajador sería ", sueldo , " €.";
	
	Escribir "La empresa pagó por todos los trabajadores de ", sueldo * numtra , " €.";
	
FinProceso
