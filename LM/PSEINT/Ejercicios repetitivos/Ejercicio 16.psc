
Proceso Ejercicio_16
	
	Definir numtra,n,dinero,sueldo como Real;
	
	Escribir Sin Saltar "Escribe el n� de trabajadores: ";
	
	Leer numtra;
	
	Escribir Sin Saltar "Salario por d�a: ";
	
	Leer dinero;
	
	n <- 0;
	
	sueldo <- 0;
	
	Repetir
		
		sueldo <- sueldo + dinero;
		
		n <- n + 1;
		
	Hasta Que n = 8
	
	Escribir "El sueldo de un trabajador ser�a ", sueldo , " �.";
	
	Escribir "La empresa pag� por todos los trabajadores de ", sueldo * numtra , " �.";
	
FinProceso
