
Proceso Ejercicio_12
	
	Definir ano como Real;
	
	Escribir "Escriba un a�o: ";
	
	Leer ano;
	
	Si (ano % 4 = 0) O (ano % 100 = 0 Y ano % 400 = 0) Entonces
		
		Escribir "El a�o indicado es bisiesto.";
		
	SiNo
		
		Escribir "El a�o indicado no es bisiesto.";
		
	FinSi
	
	
FinProceso
