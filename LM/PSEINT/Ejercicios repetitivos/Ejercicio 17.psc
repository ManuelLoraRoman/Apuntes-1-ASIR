
Proceso Ejercicio_17
	
	Definir dias,horas,n,m,sueldo,dinero,numtra como Real;
	
	Escribir Sin Saltar "Escribe el n� de trabajadores: ";
	
	Leer numtra;
	
	Escribir Sin Saltar "Escribe el sueldo base por d�a";
	
	Leer dinero;
	
	n <- 1;
	
	m <- 0;
	
	sueldo <- 0;
	
	Repetir
		
		sueldo <- sueldo + dinero;
		
		n <- n + 1;
		
	Hasta Que n = 8
	
	Escribir "El sueldo de un trabajador ser�a ", sueldo , " �.";
	
	Escribir "La empresa pag� por todos los trabajadores de ", sueldo * numtra , " �.";
	
FinProceso
