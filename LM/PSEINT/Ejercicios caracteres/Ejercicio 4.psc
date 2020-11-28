
Proceso Ejercicio_4
	
	Definir cad como Cadena;
	
	Definir n,L como Real;
	
	Escribir Sin Saltar "Escribe una cadena: ";
	
	Leer cad;
	
	n <- 0;
	
	L <- 0;
	
	Para n <- 0 Hasta Longitud(cad) Hacer
		
		Si Subcadena(cad,n,n) = " " Entonces
			
			L <- L + 1;
			
		SiNo
			
			L <- L + 0;
			
		FinSi
		
	FinPara
	
	Escribir "Hay ", L + 1 , " palabras";
	
FinProceso
