
Proceso Ejercicio_11
	
	Definir A,B,C como Real;
	
	Escribir Sin Saltar "Escribe el lado A del triángulo: ";
	
	Leer A;
	
	Escribir Sin Saltar "Escribe el lado B del triángulo: ";
	
	Leer B;
	
	Escribir Sin Saltar "Escribe el lado C del triángulo: ";
	
	Leer C;
	
	Si (A ^ 2 + B ^ 2 = C ^ 2) O (A ^ 2 + C ^ 2 = B ^ 2) O (B ^ 2 + C ^ 2 = A ^ 2) Entonces
		
		Escribir "El triángulo es rectángulo.";
		
	SiNo
		
		Si A = B Y A <> C O A = C Y A <> B O B = C Y A <> B Entonces
			
			Escribir "El triángulo es isósceles.";
			
		SiNo
			
			Si A = B y A = C Entonces
				
				Escribir "El triángulo es equilátero.";
				
			SiNo
				
				Escribir "El triángulo es escaleno.";
				
			FinSi
			
		FinSi
		
	FinSi
	
FinProceso
