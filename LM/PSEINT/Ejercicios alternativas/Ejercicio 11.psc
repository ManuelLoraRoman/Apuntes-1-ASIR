
Proceso Ejercicio_11
	
	Definir A,B,C como Real;
	
	Escribir Sin Saltar "Escribe el lado A del tri�ngulo: ";
	
	Leer A;
	
	Escribir Sin Saltar "Escribe el lado B del tri�ngulo: ";
	
	Leer B;
	
	Escribir Sin Saltar "Escribe el lado C del tri�ngulo: ";
	
	Leer C;
	
	Si (A ^ 2 + B ^ 2 = C ^ 2) O (A ^ 2 + C ^ 2 = B ^ 2) O (B ^ 2 + C ^ 2 = A ^ 2) Entonces
		
		Escribir "El tri�ngulo es rect�ngulo.";
		
	SiNo
		
		Si A = B Y A <> C O A = C Y A <> B O B = C Y A <> B Entonces
			
			Escribir "El tri�ngulo es is�sceles.";
			
		SiNo
			
			Si A = B y A = C Entonces
				
				Escribir "El tri�ngulo es equil�tero.";
				
			SiNo
				
				Escribir "El tri�ngulo es escaleno.";
				
			FinSi
			
		FinSi
		
	FinSi
	
FinProceso
