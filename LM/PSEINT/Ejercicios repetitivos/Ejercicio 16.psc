
Proceso Ejercicio_16
	
	Definir numtra,n,dinero,sueldo como Real;
	
	Escribir Sin Saltar "Escribe el nº de trabajadores: ";
	
	Leer numtra;
	
	Escribir Sin Saltar "Salario por día: ";
	
	Leer dinero;
	
	n <- 0;
	
	sueldo <- 0;
	
	Repetir
		
		sueldo <- sueldo + dinero;
		
		n <- n + 1;
		
	Hasta Que n = 8
	
	Escribir "El sueldo de un trabajador sería ", sueldo , " €.";
	
	Escribir "La empresa pagó por todos los trabajadores de ", sueldo * numtra , " €.";
	
FinProceso
