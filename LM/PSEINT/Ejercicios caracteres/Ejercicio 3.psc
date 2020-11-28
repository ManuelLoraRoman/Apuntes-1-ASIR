
Proceso Ejercicio_3
	
	Definir cad,carac como Cadena;
	
	Definir n,L como Real;
	
	Escribir Sin Saltar "Escribe una cadena: ";
	
	Leer cad;
	
	Escribir Sin Saltar "Escribe un caracter: ";
	
	Leer carac;
	
	n <- 0;
	
	L <- 0;
	
	Para n <- 0 Hasta Longitud(cad) Hacer
		
		Si Subcadena(cad,n,n) = carac Entonces
			
			L <- L + 1;
			
		SiNo
			
			L <- L + 0;
			
		FinSi
		
	FinPara
	
	Escribir "Hay ", L , " caracteres iguales al dado";
	
FinProceso
