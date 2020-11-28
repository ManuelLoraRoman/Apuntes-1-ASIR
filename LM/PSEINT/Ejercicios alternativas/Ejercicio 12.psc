
Proceso Ejercicio_12
	
	Definir ano como Real;
	
	Escribir "Escriba un año: ";
	
	Leer ano;
	
	Si (ano % 4 = 0) O (ano % 100 = 0 Y ano % 400 = 0) Entonces
		
		Escribir "El año indicado es bisiesto.";
		
	SiNo
		
		Escribir "El año indicado no es bisiesto.";
		
	FinSi
	
	
FinProceso
